# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:52:11 2016

@author: SA
"""
from pylab import loadtxt, linspace, polyfit, polyder, polyval, corrcoef, figure, plot, legend, title, ylabel, xlabel

y = loadtxt('Dropxy.dat', delimiter=',', usecols=[1], unpack=True )
n = len(y)
delta_t = 1/50
time = linspace(0, (n-1)*delta_t, n)
# Fit 2nd Order Polynomial
y_poly = polyfit(time, y, 2)
# Evaluate 2nd Order Polynomial with time values 
y_val = polyval(y_poly, time)
correlation = corrcoef(time, y)[0,1]
print('R squared = {:2.2f}'.format(correlation**2))

figure(1)
plot(time, y, 'ko')
plot(time, y_val, ':r')
ylabel('y [cm]')
xlabel('time [s]')
legend(['Experiment', 'Polynomial Fit'])

figure(2)
plot(time, y_val - y, 'o:b')
title('Difference Poynomial Fit and Experiment')
ylabel('Difference [cm]')
xlabel('time [s]')

v_poly = polyder(y_poly)
a_poly = polyder(y_poly, 2)
v_val = polyval(v_poly, time)
a_val = polyval(a_poly, time)
#
figure(3)
plot(time, v_val, '-r')
ylabel('vy [cm/s]')
xlabel('time [s]')

figure(4)
plot(time, a_val, '-r')
ylabel('ay [cm/sˆ2]')
xlabel('time [s]')
