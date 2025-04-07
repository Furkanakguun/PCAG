# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

#%% The first thing is to define the ray origin O and direction ê, where the unit vector
## Ray
O = np.array([0, 0])         # Origin pont
e_ = np.array([0.5, 0.5])    # Ray direction
e_ /= np.linalg.norm(e_)     # Unit vector of e_

#%% Next step is to define the sphere/circle center Cs and radius r
# Sphere
Cs = np.array([2, 0])        # Center of sphere
r = 1.5                      # Radius of sphere

#%% To find the ray intersection, the next step is define the oriented segment OC=Cs−O

OC_ = Cs - O  # Oriented segment from origin to center of the sphere

t = np.dot(OC_, e_)   # Vector projection of OC_ on e_

# Having the parameter t
Pe = O + e_*t                # Point on vector e_ projected from OC_
d = np.linalg.norm(Pe - Cs)  # Distance from the point Pe and the center of the sphere


# If d>r then there is no intersections
# If d=r then there is 1 intersection (tangent)
# if d<r there are 2 intersections

# Position of the intersections
if(d > r):
    print("No intersection!")

elif(d == r):
    Ps = Pe
    print(f'Intersection at {Ps}')

else:
    i = (r**2 - d**2)**0.5
    Ps1 = O + e_*(t - i)
    Ps2 = O + e_*(t + i)
    print(f'Intersections at {Ps1} and {Ps2}')
    
    
#%%

fig, ax = plt.subplots(figsize=(16, 10))

# Define x points to draw lines
x = np.array([0, 8])
colors = ["red", "green", "blue", "brown","orange"]

# Define angular coeficients
M = [0, 0.25, 0.5, 1, 1.5]

# Define sphere
Cs = [4, 2]
r = 2
Circle = plt.Circle(Cs, r, color="k", fill=0)
ax.add_artist(Circle)

# Draw intersections
for index, m in enumerate(M):
    y = m*x
    plt.plot(x, y, color=colors[index])
    plt.xlim([-0.1, 8])
    plt.ylim([-0.1, 5])
    
    # Define ray
    O = np.array([0, 0])
    e_ = np.array([1, m])
    e_ = e_/np.linalg.norm(e_)
    
    # Intersection
    OC_ = Cs - O
    t = np.dot(OC_, e_)
    Pe = O + e_*t
    d = np.linalg.norm(Pe - Cs)
    
    # Draw intersections
    if(d == r):
        Ps = Pe
        Circle = plt.Circle(Ps, 0.1, color=colors[index], fill=0)
        ax.add_artist(Circle)
    if(d < r):
        i = (r**2 - d**2)**0.5
        Ps1 = O + e_*(t - i)
        Circle = plt.Circle(Ps1, 0.1, color=colors[index], fill=0)
        ax.add_artist(Circle)
        Ps2 = O + e_*(t + i)
        Circle = plt.Circle(Ps2, 0.1, color=colors[index], fill=0)
        ax.add_artist(Circle)

plt.show()


