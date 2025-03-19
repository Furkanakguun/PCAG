import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('Dropxy.dat', delimiter=',', usecols=[0,1],unpack=True )
n = len(x)

delta_t = 1/50 # 50 frames per second
time = np.linspace(0, (n-1)*delta_t, n)
vy = np.zeros(n-1, float)

for i in range(n-1):
    vy[i] = (y[i+1] - y[i])/delta_t
    ay = np.zeros(n-2, float)
for i in range(n-2):
    ay[i] = (vy[i+1] - vy[i])/delta_t


fig, (ax1,ax2,ax3)= plt.subplots(3, 1)
ax1.plot(time, y, 'o-')
ax1.set_ylabel('y[cm]')
ax2.plot(time[0:n-1],vy, '.-')
ax2.set_ylabel('vy [cm/s]')
ax3.plot(time[1:n-1],ay, '.-')
ax3.set_ylabel('ay [cm/sˆ2]')
ax3.set_xlabel('time (s)')

plt.show()