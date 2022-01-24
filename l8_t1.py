#Из эксперимента известно, что скорость размножения бактерий при достаточном запасе пищи пропорциональна их количеству. Определите закон увеличения бактерий и время, спустя которое их станет в 10 раз больше, относительно начального количества.
import numpy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# dn(t)/dt = kn(t)
n = 1
k = 2
t = numpy.arange(0, 10, 1)

def do_something(n, t):
	return k * n

solve = odeint(do_something, n, t)
plt.plot(t, solve[:,0])
plt.show()