# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#from pylab import *

R1 = 0.0199   # m
M1 = 4.00      # kg
R2 = 0.02   # m
M2 = 4      # kg
I = M1*R1**2 + M2*R2**2
g = 9.8     # m/sˆ2

theta0 = np.radians(30)    	# rad
omega0 = 0.0    		# rad/s
time = 1.20      		# s
dt = 0.01       		# s

# Numerical variables
n = int(round(time/dt))
theta = np.zeros(n, float)
omega = np.zeros(n, float)
t = np.zeros(n, float)

# Initialize
fig, ax = plt.subplots()
theta[0] = theta0
omega[0] = omega0
# Integration loop
for i in range(n-1):
    r = np.array([R2*np.cos(theta[i]), R2*np.sin(theta[i])])
    tauz = M1*g*np.sin(theta[i])*R1 - M2*g*np.sin(theta[i])*R2
    alpha = tauz/I
    omega[i+1] = omega[i] + alpha*dt
    theta[i+1] = theta[i] + omega[i+1]*dt
    t[i+1] = t[i] + dt
    if (np.mod(i, 2)==0):
        ax.plot(np.array([0, r[0]]), np.array([0, r[1]]),'-o')
        ax.set_xlabel('x [m]')
        ax.set_ylabel('y [m]')
        ax.axis([-R1, R1, -R1, R1])
        ax.set_aspect('equal')
