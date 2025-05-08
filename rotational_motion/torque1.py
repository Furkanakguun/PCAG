# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

R1 = 0.02   # m
M1 = 4      # kg
R2 = 0.02   # m
M2 = 4      # kg
Ro = 0.02
I = M1*R1**2 + M2*R2**2 # + (M1 + M2)*0.004**2
g = 9.8     # m/sˆ2
F = 10      # N

omega0 = 0.0            # rad/s
theta0 = np.radians(30)    # rad
time = 0.2             # s
dt = 0.01               # s
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
    tauz = F*R1

    #tauz = M1*g*np.sin(theta[i])*Ro - M2*g*np.sin(theta[i])*Ro
    alpha = tauz/I
    omega[i+1] = omega[i] + alpha*dt
    theta[i+1] = theta[i] + omega[i+1]*dt
    t[i+1] = t[i] + dt
    if (np.mod(i, 1)==0):
        ax.plot(np.array([0, r[0]]), np.array([0, r[1]]),'-o')
        ax.set_xlabel('x [m]')
        ax.set_ylabel('y [m]')
        ax.axis([0, R1, 0, R1])
        ax.set_aspect('equal')
plt.show()