'''
Метеорит, находящийся под влиянием земного притяжения, из состояния покоя начинает прямолинейно падать на Землю с высоты h. Определите закон изменения скорости метеорита по мере его приближения к поверхности Земли и определите скорость его столкновения с нашей планетой.
'''
# F = (G * M1 * M2) / R^2
import numpy
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m1 = int(input('Введите массу метеорита'))
h0 = 44000
R = 6371
M =  5.972 * 10 ** 24
g = 9.88
h = numpy.arange(h0, R, 1)

G = (m1 * g * (h0 + R) ** 2) / m1 * M

def meteor(v, h):
	
	v = numpy.sqrt(2 * ((m1 * g * (h0 + R) ** 2) / m1 * M) * h)
	dvdh = v / h
	
	return dvdh 

solve = odeint(meteor, G, h)

plt.plot(t, solve[:,0])
plt.show()