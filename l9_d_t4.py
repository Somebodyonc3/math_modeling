import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.0001)

def diff(fff, arg):
	t = arg
	y, p = fff

	dydx = p 
	dpdx = (4 * t ** 2 + 0.5) * (y / t ** 2) - p / t
	
	return dydx, dpdx

y0 = 3
dy0dt = 0

m0 = y0, dy0dt

solve = odeint(diff, m0, t)

plt.plot(t, solve[:, 1])
plt.plot(t, solve[:, 0])
plt.show()