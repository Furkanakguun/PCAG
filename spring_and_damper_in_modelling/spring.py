# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Initialize
m = 1.0         # kg
k = 100.0       # N/m
v0 = 10.0       # m/s
t = 2.0         # s
g = 9.8         # m/sˆ2
# Numerical setup
dt = 1/60 # s
n = int(round(t/dt))
t = np.zeros(n, float)
y = np.zeros(n, float)
v = np.zeros(n, float)

# Initial values
y[0] = 0.0
v[0] = v0

# Simulation loop 
for i in range(n-1):
    F = -k*y[i] - m*g
    a = F/m
    v[i+1] = v[i] + a*dt
    y[i+1] = y[i] + v[i+1]*dt
    t[i+1] = t[i] + dt

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t,y,'-b')
ax2.plot(t,v,'-b')
ax1.set_ylabel('y [m]')
ax2.set_ylabel('v [m/s]')
ax2.set_xlabel('t [s]')
plt.show() 
