# -*- coding: utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure()
ax = Axes3D(figure)


x = np.linspace(-5, 5, 10)
for i in x:
    y = np.linspace(-5, 5, 10)
    z = np.random.normal(1, 10, 10)
    ax.bar(y, z, i, zdir='y', color=['r', 'g', 'b', 'y'])


ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.show()