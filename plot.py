import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d

from matplotlib.lines import Line2D
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.set_title('Camera plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim(0,150)
ax.set_ylim(0,150)
ax.set_zlim(0,150)

origin = np.array([30, 30, 90])

v = np.array([origin+[-5, -5, -10], origin+[5, -5, -10],
              origin+[5, 5, -10],  origin+[-5, 5, -10], origin])

verts = [[v[0], v[1], v[4]], [v[0], v[3], v[4]],
         [v[2], v[1], v[4]], [v[2], v[3], v[4]], [v[0], v[1], v[2], v[3]]]

ax.plot3D([30,30], [30,30], [0,90], 'blue', marker='o', markersize=5)

ax.add_collection3d(Poly3DCollection(verts,
                                     facecolors='magenta', linewidths=2, edgecolors='b', alpha=.25))

plt.show()
