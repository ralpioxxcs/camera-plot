import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d

from matplotlib.lines import Line2D
from matplotlib.collections import LineCollection

from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from mpl_toolkits.mplot3d import Axes3D

import util

def plotting(model, extrinsic):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_title('Extrinsic Parameter Plot')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-100, 100)
    ax.set_ylim(0, 300)
    ax.set_zlim(-150, 150)
    ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([1, 2, 1, 1])) # scaling

    create_camera_model(ax)
    create_board_model(ax, model, extrinsics)

    plt.show()

def create_camera_model(ax):
    origin = np.array([0, 0, 0])

    # camera axis:
    scale = 25
    axis_x = np.array([scale, 0, origin[2]])
    axis_y = np.array([0, scale, origin[2]])
    axis_z = np.array([0, 0, -scale])
    axis = [axis_x, axis_y, axis_z]

    for p in axis:
        ax.plot3D([origin[0], p[0]], [origin[1], p[1]],
                  [origin[2], p[2]], color='black')
    ax.text(origin[0], origin[1], origin[2], "Oc", color='black')
    ax.text(axis_x[0], origin[1], origin[2], "Xc", color='black')
    ax.text(origin[0], axis_y[1], origin[2], "Yc", color='black')
    ax.text(origin[0], origin[1], axis_z[2], "Zc", color='black')

    # camera frame
    ## image frame
    imagePlane = np.ones((4,5))
    width, height, f_scale = origin + [20,25,20]
    imagePlane[0:3, 0] = [-width, height, f_scale]
    imagePlane[0:3, 1] = [width, height, f_scale]
    imagePlane[0:3, 2] = [width, height, f_scale - (20*2)]
    imagePlane[0:3, 3] = [-width, height, f_scale - (20*2)]
    imagePlane[0:3, 4] = [-width, height, f_scale]
    ax.plot3D(imagePlane[0,:], imagePlane[1,:], imagePlane[2,:], color='red')

    ## camera frame
    frame_tl = np.array(imagePlane[0:3,0])
    frame_tr = np.array(imagePlane[0:3,1])
    frame_bl = np.array(imagePlane[0:3,2])
    frame_br = np.array(imagePlane[0:3,3])
    frame = [frame_tl, frame_tr, frame_bl, frame_br]
    for p in frame:
        ax.plot3D([origin[0], p[0]], [origin[1], p[1]],
                  [origin[2], p[2]], color='red')

    # origin = np.array([0,0,0])
    # v = np.array([origin+[-5, -5, -10], origin+[5, -5, -10],
    #               origin+[5, 5, -10],  origin+[-5, 5, -10], origin])
    # verts = [[v[0], v[1], v[4]], [v[0], v[3], v[4]],
    #          [v[2], v[1], v[4]], [v[2], v[3], v[4]], [v[0], v[1], v[2], v[3]]]

    # ax.add_collection3d(Poly3DCollection(
    #     verts, facecolors='magenta', linewidths=2, edgecolors='b', alpha=.25))

def create_board_model(ax, model, extrinsics):
    # checker board surface
    model = util.toHomogeneous(model)
    for index, E in enumerate(extrinsics):
        model_ext = np.dot(model,E)
        xs = model_ext[:,0]*100
        ys = model_ext[:,2]*100
        zs = model_ext[:,1]*100
        ax.plot_trisurf(xs,ys,zs)
        ax.text(xs[0]-10,ys[0]-10,zs[0]-10, index, fontsize=13)

