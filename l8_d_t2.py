import numpy
from scipy.integrate import odeint
import matplotlib.pyplot as plt

k = 340 * 10 ** (-8)
Esun = 1367 
t = numpy.arange(0, 24, 0.1)

def victoria(S, t):
	
	alpha = numpy.pi /12 * (t - 12)
	cosin = numpy.cos(alpha)
	if cosin < 0:
		cosin = 0
	R = numpy.sqrt(S / numpy.pi)
	E = S * k * Esun * cosin
	dsdt = R * E
	return dsdt

S_0 = 1600

solve = odeint(victoria, S_0, t)

plt.plot(t, solve[:,0])
plt.show()