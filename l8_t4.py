#Ускорение локомотива , начальная скорость которого равна v0, прямо пропорционально силе тяги F и обратно пропорционально массе поезда m. Сила тяги локомотива F(t) = b — k v(t), где v(t) — скорость локомотива в момент t, а b и k — постоянные величины. Определить зависимость силы тяги локомотива от времени t.
import numpy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#dv/dt = b - k * v / m
b = 100000
k = 10005
m = 30 * 10 ** 3
v = 0
t = numpy.arange(0, 10, 0.001)

def do_something(v, t):
	return (b - k * v) / m


solve = odeint(do_something, v, t)
plt.plot(solve[:,0], b - k * solve[:,0])
plt.show()