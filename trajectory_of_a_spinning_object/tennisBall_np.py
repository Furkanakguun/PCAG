# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

g = 9.81      # Gravity [m/s^2]
nu = 1.5e-5   # Kinematical viscosity [m^2/s]
rho_f = 1.20  # Density of fluid [kg/m^3]
rho_s = 418   # Density of sphere [kg/m^3]
d = 67.0e-3   # Diameter of the sphere [m]
v0 = 50.0     # Initial velocity [m/s]
vfx = 0.0     # x-component of fluid's velocity
vfy = 0.0     # y-component of fluid's velocity
CD = 0.55     # CD is typically about 0.5 - 0.6
CL = 0.3      # CL is normally taken to be positive for backspin and negative for topspin. 


def rk4(func, z0, time):
    """The Runge-Kutta 4 scheme for solution of systems of ODEs.
    z0 is a vector for the initial conditions,
    the right hand side of the system is represented by func which returns
    a vector with the same size as z0 ."""

    z = np.zeros((time.size, z0.size))
    z[0, :] = z0

    for i, t in enumerate(time[0:-1]):
        dt = time[i+1] - time[i]
        dt2 = dt/2.0
        k1 = np.asarray(func(z[i, :], t))                 # predictor step 1
        k2 = np.asarray(func(z[i, :] + k1*dt2, t + dt2))  # predictor step 2
        k3 = np.asarray(func(z[i, :] + k2*dt2, t + dt2))  # predictor step 3
        k4 = np.asarray(func(z[i, :] + k3*dt, t + dt))    # predictor step 4
        z[i+1, :] = z[i, :] + dt/6.0*(k1 + 2.0*k2 + 2.0*k3 + k4)   # Corrector step
    return z


# tennis ball without lift
def f2(z, t):
    """4x4 system for golf ball with drag in two directions."""
    zout = np.zeros_like(z)
    C = 3.0*rho_f/(4.0*rho_s*d)
    vrx = z[2] - vfx
    vry = z[3] - vfy
    vr = np.sqrt(vrx**2 + vry**2)
    zout[:] = [z[2], z[3], -C*vr*(CD*vrx), C*vr*(-CD*vry) - g]
    return zout


# tennis ball with lift
def f3(z, t):
    """4x4 system for golf ball with drag and lift in two directions."""
    zout = np.zeros_like(z)
    C = 3.0*rho_f/(4.0*rho_s*d)
    vrx = z[2] - vfx
    vry = z[3] - vfy
    vr = np.sqrt(vrx**2 + vry**2)
    zout[:] = [z[2], z[3], -C*vr*(CD*vrx + CL*vry), C*vr*(CL*vrx - CD*vry) - g]
    return zout


# main program starts here
T = 3   # end of simulation
N = 60  # no of time steps
time = np.linspace(0, T, N+1)
N2 = 4
alfa = np.linspace(30, 15, N2)     # Angle of elevation [degrees]
angle = alfa*np.pi/180.0           # convert to radians

legends = []
line_color = ['k', 'm', 'b', 'r']
fig, ax = plt.subplots(figsize = (20, 8))# width, height in inches
 

# computing and plotting
# tennis ball with drag
for i in range(0, N2):
    z0 = np.zeros(4)
    z0[2] = v0*np.cos(angle[i])
    z0[3] = v0*np.sin(angle[i])
    z = rk4(f2, z0, time)
    ax.plot(z[:, 0], z[:, 1], '-', color=line_color[i])
    legends.append('angle=' + str(alfa[i]) + ', with drag')

# tennis ball with drag and lift
for i in range(0, N2):
    z0 = np.zeros(4)
    z0[2] = v0*np.cos(angle[i])
    z0[3] = v0*np.sin(angle[i])
    z = rk4(f3, z0, time)
    ax.plot(z[:, 0], z[:, 1], '.', color=line_color[i])
    legends.append('angle=' + str(alfa[i]) + ', with drag and with lift')
 
ax.legend(legends, loc='best', frameon=False)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.axis([0, 100, 0, 30])

plt.show()