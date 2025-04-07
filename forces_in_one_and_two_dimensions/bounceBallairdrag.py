# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

m = 0.2                 # mass of the ball in kg
g = 9.81                # gravitational acceleration in m/sˆ2
alpha = np.radians(75)     # Initial angle in radian
v0 = 30                 # Initial velocity in m/s
y0 = 0                  # Initial position in meters
diam = 0.02             # diameter of the ball in meters
rho = 1.225             # air dansity in kg/m^3
D = 3.0*rho*diam**2     # drag coefficient
R = (diam/2)            # ball contact starts - equilibrium length of Spring
k = 1000.0              # stiffnes of the spring N/m
time = 10.0             # simulation time
dt = 0.001              # time step

#:Numerical initialization
n = int(np.ceil(time/dt))
a = np.zeros((n, 2), float)
v = np.zeros((n, 2), float)
r = np.zeros((n, 2), float)
t = np.zeros((n, 2), float)
# Set initial values
r[0,1] = y0                             # initial position of the ball
v[0,:] = v0*np.cos(alpha), v0*np.sin(alpha)   # initial velocity in i, j

# Integration loop
for i in range(n-1):
    if (r[i,1] < R):
        N = k*(R-r[i,1])*np.array([0,1])
    else:
        N = np.array([0,0])
    FD = - D*np.linalg.norm(v[i,:])*v[i,:]
    G = -m*g*np.array([0,1])
    Fnet = N + FD + G
    a = Fnet/m
    v[i+1,:] = v[i] + a*dt
    r[i+1,:] = r[i] + v[i+1]*dt
    t[i+1] = t[i] + dt

# Plotting the results
fig, ax = plt.subplots()
ax.plot(r[:,0],r[:,1], 'ro')
ax.axis([0, 50, 0, 50]), ax.axis('equal')
ax.set_xlabel('x [m]'), ax.set_ylabel('y [m]'), ax.grid(True)