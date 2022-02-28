import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a = np.arange(-1, 1, 0.0001)

def diff(m, a):

	x, y, z = m
	
	dxdt = 3 * x - y + z
	dydt = x + y + z
	dzdt = 4 * x - y + 4 * z 
	
	return dxdt, dydt, dzdt

x0 = -71
y0 = 1
z0 = -3

m0 = x0, y0, z0

solve = odeint(diff, m0, a)
plt.plot(a, solve[:, 0])
plt.plot(a, solve[:, 1])
plt.plot(a, solve[:, 2])

plt.show()