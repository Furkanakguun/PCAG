# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sympy import *
v, x, t, g= symbols('v x t g', real = True)
m= symbols('m', constant = True)
init_printing(use_unicode=True) 

v = integrate(-m*g, t)
print('Velocity : ', v)
x = integrate(v, t)
print('Position : ', x)
