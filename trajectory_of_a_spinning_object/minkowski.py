# -*- coding: utf-8 -*-
"""
Created on Mon May 13 22:18:09 2024

Inspired by SA-Lenovo
"""

from scipy.spatial import ConvexHull
import numpy as np
import matplotlib.pyplot as plt

A = [(1,4),(1,1),(3,1),(3,4)]
B = [(0,3),(0,2),(2,2)]

points = np.asarray([(xA-xB, yA-yB) for xA, yA in A for xB, yB in B])
       
hull = ConvexHull(points)

plt.plot(points[:,0], points[:,1], 'o')
plt.plot(0, 0, 'ro')

for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

plt.plot(0, 0, 'ro')
plt.axhline(linewidth=2, color='r')
plt.axvline(linewidth=2, color='r')

plt.axis('equal')
plt.grid()
