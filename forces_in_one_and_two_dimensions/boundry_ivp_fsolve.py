import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve


# Define the function F with robust handling for s[1] == 0
def F(t, s):
    v = s[1]
    # Prevent division by zero with robust handling
    if np.abs(v) < 1e-6:  # Small threshold instead of directly checking == 0
        g = 9.8 / 1e-6  # Use the small value to approximate the division
    else:
        g = 9.8 / v
    return np.array([v, -g])


# Initial condition for y and the range of computation
y0 = 0
t_eval = np.linspace(0, 5, 100)  # Time evaluation points


def objective(v0):
    # Solve the IVP
    sol = solve_ivp(F, [0, 5], [y0, v0], t_eval=t_eval)
    y = sol.y[0]  # Extract y values (first row of `sol.y`)
    return y[-1] - 50  # The target is the difference from 50 at the final time


# Find the initial velocity v0 such that y[-1] == 50
v0, = fsolve(objective, 10)
print(f"Initial velocity v0: {v0}")
