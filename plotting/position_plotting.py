import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

f = lambda t, s: np.dot(np.array([[0,1],[0,-9.8/s[1]]]), s)
t_span = np.linspace(0, 5, 100)

y0 = 0
v0 = 34.49999999999999

t_eval = np.linspace(0, 5, 100)
sol = solve_ivp(f, [0, 5], \
[y0, v0], t_eval = t_eval)

# Position Plotting
fig, ax = plt.subplots()
ax.plot(sol.t, sol.y[0], '-r')
ax.plot(5, 50, 'ro')
ax.set_xlabel('time [s]')
ax.set_ylabel('r [m]')

plt.show()