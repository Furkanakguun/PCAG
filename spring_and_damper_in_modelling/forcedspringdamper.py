# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Initialize
timeFinal= 16.0   # This is how far the graph will go in seconds
steps = 10000     # Number of steps
dt = timeFinal/steps      # Step length 
t = np.linspace(0, timeFinal, steps+1)

# Creates an array with steps+1 values from 0 to timeFinal
# Allocating arrays for velocity and position
v = np.zeros(steps+1)
y = np.zeros(steps+1)

# Setting constants and initial values for vel. and pos.
k = 0.1
m = 0.01
v0 = 0.01
y0 = 2.00
freqNatural = (k/m)**0.5 # sqrt(k/m )
c = 0.00
F0 = 0.010
Wd = freqNatural
v[0] = v0    #Sets the initial velocity
y[0] = y0    #Sets the initial position

# Simulation loop 
# Numerical solution using Euler's
# Splitting the ODE into two first order ones
# v'(t) = -(k/m)*x(t) - (c/m)*v(t)
# x'(t) = v(t)
# Using the definition of the derivative we get
# (v(t+dT) - v(t))/dT on the left side of the first equation
# (x(t+dT) - x(t))/dT on the left side of the second 
# In the for loop t and dt will be replaced by i and 1
for i in range(0, steps):
    v[i+1] = (-k/m)*y[i]*dt + v[i]*(1-dt*c/m) + F0/m*np.cos(Wd*i*dt)*dt
    y[i+1] = y[i] + v[i+1]*dt 

fig, ax = plt.subplots()
ax.plot(t, y,'-g', label='Undampened')

# Damping set to 10% of critical damping
c = (2*(k*m)**0.5)*1 
for i in range(0, steps):
    v[i+1] = (-k/m)*y[i]*dt + v[i]*(1-dt*c/m) + F0/m*np.cos(Wd*i*dt)*dt
    y[i+1] = y[i] + v[i+1]*dt 

ax.plot(t, y, 'b-', label = '100% of crit. damping')
ax.set_xlabel('t [s]')
ax.set_ylabel('y [m]')
ax.legend(loc = 'upper right')
plt.show()