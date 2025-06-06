# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:43:35 2024

@author: SA-Lenovo
"""

from gekko import GEKKO

#Initialize Model
m = GEKKO()

#define parameter
eq = m.Param(value=40)

#initialize variables
x1,x2,x3,x4 = [m.Var(lb=1, ub=5) for _ in range(4)]

#initial values
x1.value = 1
x2.value = 5
x3.value = 5
x4.value = 1

#Equations
m.Equation(x1*x2*x3*x4>=25)
m.Equation(x1**2+x2**2+x3**2+x4**2==eq)

#Objective
m.Minimize(x1*x4*(x1+x2+x3)+x3)

#Set global options
m.options.IMODE = 3 #steady state optimization

#Solve simulation
m.solve()

#Results
print('')
print('Results')
print('x1: ' + str(x1.value))
print('x2: ' + str(x2.value))
print('x3: ' + str(x3.value))
print('x4: ' + str(x4.value))

#%% compact version of the same problem
import numpy as np
m = GEKKO()
x = m.Array(m.Var,4,value=1,lb=1,ub=5)
x1,x2,x3,x4 = x                 # rename variables
x2.value = 5; x3.value = 5      # change guess
m.Equation(np.prod(x)>=25)      # prod>=25
m.Equation(m.sum([xi**2 for xi in x])==40) # sum=40
m.Minimize(x1*x4*(x1+x2+x3)+x3) # objective
m.solve()
print(x)