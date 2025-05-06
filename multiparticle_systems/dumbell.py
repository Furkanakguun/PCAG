import numpy as np
import matplotlib.pyplot as plt

m = 0.1
k = 200.0
b = 0.2
h0 = 1.0
g = 9.8
time = 2
dt = 0.00001
n = int(round(time/dt))
t = np.zeros(n,float)
xA = np.zeros(n,float)
vA = np.zeros(n,float)
xB = np.zeros(n,float)
vB = np.zeros(n,float)
xA[0] = h0 + b
vA[1] = 0.0
xB[0] = h0
vB[1] = 0.0

for i in range(n-1):
    f = k*(xA[i] - xB[i] - b)
    fA = -f - m*g
    fB = f - m*g
    aA = fA/m
    vA[i+1] = vA[i] + aA*dt
    xA[i+1] = xA[i] + vA[i+1]*dt
    aB = fB/m
    vB[i+1] = vB[i] + aB*dt
    xB[i+1] = xB[i] + vB[i+1]*dt
    t[i+1] = t[i] + dt
    if (xB[i+1]<0.0) and (xB[i]>=0.0):
        vB[i+1] = abs(vB[i+1])
        
xcm = (xA+xB)*0.5
vcm = (vA+vB)*0.5
Kcm = 0.5*(2.0*m)*vcm**2
Kcmdelta = 0.5*m*(vA - vcm)**2+0.5*m*(vB-vcm)**2
Ug = xcm*(2.0*m)*g
Uk = 0.5*k*(xA - xB - b)**2
E = Kcm + Kcmdelta + Ug + Uk

fig, (ax1,ax2)= plt.subplots(2, 1,constrained_layout=True, sharex=True)

ax1.plot(t,xA,'-b',t,xB,'-r',t,xcm,':k')
ax1.set_xlabel('t [s]')
ax1.set_ylabel('x [m]');

ax2.plot(t,Kcm,'-b',t,Kcmdelta,'-r',t,Uk,'-y',t,E,':k')
ax2.set_xlabel('t [s]')
ax2.set_ylabel('E [J]')
plt.show()