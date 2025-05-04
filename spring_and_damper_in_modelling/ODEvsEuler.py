# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# simulation parameters
stime = 10.0 # time [s]
m = 1.0     # mass [kg]
k = 100.0   # spring stiffness [N/m]
v0 = 10.0   # initial volocity [m/s]
g = 9.8     # gravity [m/sˆ2]
dt = 0.1   # time step [s]
n = int(round(stime/dt))
tspan = np.linspace(0.0, stime, n)

# Numerical setup for Euler method
t = np.zeros(n,float)
y = np.zeros(n,float)
v = np.zeros(n,float)
# Initial values
y[0] = 0.0
v[0] = v0

# Euler integration loop 
for i in range(n-1):
    F = -k*y[i] - m*g
    a = F/m
    v[i+1] = v[i] + a*dt
    y[i+1] = y[i] + v[i+1]*dt
    t[i+1] = t[i] + dt

fig, ax = plt.subplots()
ax.plot(t, y,'-b')

# ODE initilization
# ODE function
def MassSpring(t, state, m, k, g):
    x = state[0]
    xd = state[1]
    # compute acceleration xdd
    F = -k*x - m*g
    xdd = F/m     # xdd = ((k*x)/m) – g
    # return the two state derivatives
    return [xd, xdd]

  
sol = solve_ivp(MassSpring, [tspan[0], tspan[-1]],
                            [0, v0], 
                             method = "RK45", 
                             t_eval=tspan, args=(m, k, g))

# %% Plot states
ax.plot(sol.t, sol.y[0],'-r')
ax.set_xlabel('t [s]')
ax.set_ylabel('y')
plt.title(f'Euler vs RK45\n time step : {dt}')
ax.legend(('$Euler$', '$RK45$ '))
plt.show()
