# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

I = plt.imread("red_spriteCG.png")

fig, ax= plt.subplots()
ax.imshow(I)
ax.axis('off'), ax.axis('equal')
plt.show()

Ibw = (I[:,:,0] + I[:,:,1] + I[:,:,2]) <= 2.9

fig, ax= plt.subplots()

ax.imshow(Ibw, cmap='gray', vmin=0, vmax=1)
ax.axis('off'), ax.axis('equal')

s = np.shape(Ibw)
x, y , m = 0, 0, 0 

for iy in range(s[0]):
    for ix in range(s[1]):
        if Ibw[iy, ix]:
            x += ix
            y += iy
            m += 1

xcm, ycm = x/m, y/m
ax.plot(xcm, ycm,'ro')
plt.show()