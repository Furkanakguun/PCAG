# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:22:19 2016

@author: SA
"""

import matplotlib.pyplot as plt
import numpy as np

t,x,y=np.loadtxt('soccer.txt', usecols=[0,1,2], unpack=True)
n = len(t)
dt = t[1] - t[0]
r = np.zeros((n, 2), float)
r[:,0] = x
r[:,1] = y
fig, ax = plt.subplots()

ax.plot(r[:,0],r[:,1])
ax.axis('equal')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.grid(True, linestyle='-.')
plt.show()

# Displacement Calculations
fig, ax = plt.subplots()

for i in range(n-1):
    ax.plot(r[i,0], r[i,1],'o')
    dr = r[i+1,:] - r[i,:]
    ax.quiver(r[i,0], r[i,1], dr[0], dr[1], angles='xy',
           scale_units='xy', scale=1)
ax.axis('equal')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.grid(True, linestyle='-.')
plt.show()

# Velocity Calculations
fig, ax = plt.subplots()
v = np.zeros((n-1, 2),float)
for i in range(n-1):
    ax.plot(r[i,0], r[i,1],'o')
    v[i,:] = (r[i+1,:] - r[i,:])/dt
    ax.quiver(r[i,0], r[i,1], v[i,0], v[i,1], angles='xy',
           scale_units='xy', scale=1)
ax.axis('equal')
ax.set_xlabel(r'$v_x [m/s]$')
ax.set_ylabel(r'$v_y [m/s]$')
ax.grid(True, linestyle='-.')
# plt.show()
# Acceleration Calculations
#fig, ax = plt.subplots()
a = np.zeros((n-2, 2),float)
for i in range(n-2):
    ax.plot(r[i+1,0], r[i+1,1],'o')
    a[i,:] = (v[i+1,:] - v[i,:])/dt
    ax.quiver(r[i+1,0], r[i+1,1], a[i,0], a[i,1], color='r', angles='xy',
           scale_units='xy', scale=1)
ax.axis('equal')
ax.set_xlabel(r'$a_x [m/s^2]$')
ax.set_ylabel(r'$a_y [m/s^2]$')
ax.grid(True, linestyle='-.')
plt.show()