# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:08:44 2016

@author: SA
"""
from pylab import loadtxt, linspace, zeros, figure, subplot, plot, ylabel, xlabel

x, y = loadtxt('Dropxy.dat', delimiter=',', usecols=[0,1], unpack=True )
n = len(x)
delta_t = 1/50      # 50 frames per second
time = linspace(0, (n-1)*delta_t, n)

vy = zeros(n-1, float);
for i in range(n-1):
    vy[i] = (y[i+1] - y[i])/delta_t;

ay = zeros(n-2, float);
for i in range(n-2):
    ay[i] = (vy[i+1] - vy[i])/delta_t;

figure(1)
subplot(3,1,1)
plot(time, y)
ylabel('y [cm]')
subplot(3,1,2)
plot(time[0:n-1],vy)
ylabel('vy [cm/s]')
subplot(3,1,3)
plot(time[1:n-1],ay)
xlabel('time [s]')
ylabel('ay [cm/sˆ2]')