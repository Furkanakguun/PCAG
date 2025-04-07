# -*- coding: utf-8 -*-

import numpy as np
# Line of action
theta = np.radians(30)
# mass values
m1 = 10
m2 = 5
e = 0.9 # the coefficient of restitution 
v1pre = np.matrix([[8],
                [0]])
v2pre = np.matrix([[0],
                [0]])

R1 = np.matrix([[np.cos(theta), np.sin(theta)],
             [-np.sin(theta), np.cos(theta)]])

R2 = np.matrix([[np.cos(theta), -np.sin(theta)],
             [np.sin(theta), np.cos(theta)]])

v1p, v1n = R1*v1pre
v2p, v2n = R1*v2pre
                   
# Compute the post-collision velocities for the two spheres
v1pt, v2pt = np.multiply((1.0/(m1+m2)), np.matrix([[(m1-e*m2), m2*(1+e)],[m1*(1+e), (m2-e*m1)]])*np.vstack((v1p, v2p)))
# The final step in the process is to rotate the post-collision velocities
# back to the standard Cartesian coordinate system
v1post = R2*np.vstack((v1pt, v1n))
v2post = R2*np.vstack((v2pt, v2n))

print(v1post)
print(v2post)