import numpy as np
import matplotlib.pyplot as plt


# Physical variables
g = 9.81        # gravity
time = 20.0     # Simulation Time
dt = 0.1        # (h) time step

# Numerical initialization
n = int(np.ceil(time/dt))
a = np.zeros(n,float)
v = np.zeros(n,float)
r = np.zeros(n,float)
t = np.zeros(n,float)

# Set initial values
r[0] = 80   # meters 
v[0] = 0    # initial velocity
a[:] = -g   # constant acceleretion

# Integration loop
for i in range(n-1):
    v[i+1] = v[i] + a[i]*dt
    r[i+1] = r[i] + v[i+1]*dt
    t[i+1] = t[i] + dt


# Acceleration Plotting
fig, ax = plt.subplots()
ax.plot(t, a,'-r')
ax.set_xlabel('time [s]')
ax.set_ylabel(r'$g [m/s^2]$')
plt.show()

# Velocity Plotting
fig, ax = plt.subplots()
ax.plot(t, v,'-r')
ax.set_xlabel('time [s]')
ax.set_ylabel(r'$v [m/s]$')
plt.show()

# Position Plotting
fig, ax = plt.subplots()
ax.plot(t, r, '-r')
ax.set_xlabel('time [s]')
ax.set_ylabel('r [m]')
plt.show()
