#На материальную точку массы m действует постоянная сила, сообщающая точке ускорение a0. Окружающая среда оказывает движущейся точке сопротивление, пропорциональное квадрату скорости движения со временем, коэффициент сопротивления равен γ. Определите закон изменения скорости со временем, если в начальный момент времени точка находилась в покое.
import numpy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# dv/dt = (V ** 2 * y + F) / m
m = 10
F = 200
y = 1.5
V = 10
t = numpy.arange(0, 100, 0.10)

def do_something(V, t):
	return (V ** 2 * - y + F) / m

solve = odeint(do_something, V, t)
plt.plot(t, solve[:,0])
plt.show()