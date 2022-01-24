#Предприятие инвестирует в новое производство денежные средства, причем инвестиции уменьшаются со скоростью, прямо пропорциональной инвестируемым в данный момент времени средствам с коэффициентом пропорциональности 0,08. Найти закон изменения инвестиций со временем и объем инвестиций за 4 года, если в начальный момент времени инвестиции составили 1000 денежных единиц.
import numpy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#dn/dt = -0.08 * t * n
n = 1000
k = -0.08
t = numpy.arange(0, 10, 1)

def do_something(n, t):
	return  k * t * n

solve = odeint(do_something, n, t)
plt.plot(t, solve[:,0])
plt.show()