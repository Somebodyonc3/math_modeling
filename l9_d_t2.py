import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0.01, 5, 0.0001)

def diff(fff, arg):
	t = arg
	y, a = fff

	dydt = a
	dadt = (a**2 - ((3 * y**2) / np.sqrt(t))) / y
	# dadt = 0
	
	return dydt, dadt

y0 = 1
dy0dt = 0

m0 = y0, dy0dt

solve = odeint(diff, m0, t)

plt.plot(t, solve[:, 1])
plt.plot(t, solve[:, 0])
plt.show()