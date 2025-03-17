import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
x = np.array([0.0, 3.4, 11.1, 21.3, 33.2, 45.8, 57.9])

fig, ax = plt.subplots()
ax.plot(t, x)
ax.set(xlabel='time [s]',\

ylabel='Distance [x]',
title='Distance vs Time Graph')

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='r', \
               
labelsize='medium', \
width=3)

plt.show()