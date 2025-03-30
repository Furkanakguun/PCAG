# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sympy import symbols, diff, init_printing
from sympy.plotting import plot
v, a, t, g, y0 = symbols('v a t g y0', real = True)
init_printing(use_unicode=True) 
y = y0 - 0.5*g*t**2
print('Position : ', y)
v = diff(y, t)
print('Velocity : ', v)
a = diff(v, t)
print('Acceleration : ', a)
# Let's do some experiment
# Leave the ball from 10 meters on the earth
yexp = y.subs({y0:10, g: 9.8182})
plot(yexp, (t, 0, 5), ylim= [0, 10], ylabel='Position')

vexp = diff(yexp, t)
plot(vexp, (t, 0, 5), ylim= [-100, 0], ylabel='Velocity')
aexp = diff(vexp, t)
plot(aexp, (t, 0, 5), ylim= [-20, 0], ylabel='Acceleration')

