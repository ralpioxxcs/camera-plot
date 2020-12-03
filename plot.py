import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d

from matplotlib.lines import Line2D
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

from matplotlib import rc

rc('font', size=13)
rc('font', family='Serif')
rc('axes', labelsize=10)
rc('lines', markersize=5)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.set_title('Camera plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim(-50,50)
ax.set_ylim(-50,50)
ax.set_zlim(0,100)

# camera
origin = np.array([10, 10, 90])
v = np.array([origin+[-5, -5, -10], origin+[5, -5, -10],
              origin+[5, 5, -10],  origin+[-5, 5, -10], origin])
verts = [[v[0], v[1], v[4]], [v[0], v[3], v[4]],
         [v[2], v[1], v[4]], [v[2], v[3], v[4]], [v[0], v[1], v[2], v[3]]]

# board
data = [ [[0,0,0],[1,0,0],[2,0,0],[3,0,0],
         [0,1,0],[1,1,0],[2,1,0],[3,1,0],
         [0,2,0],[1,2,0],[2,2,0],[3,2,0],
         [0,3,0],[1,3,0],[2,3,0],[3,3,0]],
        [[0,0,10],[1,0,10],[2,0,10],[3,0,10],
         [0,1,10],[1,1,10],[2,1,10],[3,1,10],
         [0,2,10],[1,2,10],[2,2,10],[3,2,10],
         [0,3,10],[1,3,10],[2,3,10],[3,3,10]]
       ]
boards = np.array(data)

for item in boards:
    print(item)
    xs = item[:,0]*10
    ys = item[:,1]*10
    zs = item[:,2]*10
    ax.plot_trisurf(xs,ys,zs)

ax.plot3D([10,10], [10,10], [0,90], 'blue', marker='o', markersize=5)

ax.add_collection3d(Poly3DCollection(verts,
                                     facecolors='magenta', linewidths=2, edgecolors='b', alpha=.25))

plt.show()
