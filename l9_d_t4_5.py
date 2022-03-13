import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

import matplotlib
matplotlib.use('TkAgg')

n = 1
alpha = 0

init_values_t4 = (
  (0, (1, 0), 'r'),
  (1, (0, 1), 'g'),
  (2, (0.00000025, 0), 'b')
)

def t5(ff, arg):
  x = arg
  y, u = ff
  k = n * (n + 2)
  dydx = u
  dudx = (x * u - k * y) / (1 - x ** 2)
  return dydx, dudx

def t4(ff, arg):
  x = arg
  y, u = ff
  dydx = u
  dudx = - ( u / x + (( x ** 2 - alpha ** 2) * y / x ** 2))
  return dydx, dudx

x_t4 = np.arange(0.001, 25, 0.001)
for a, ff, color in init_values_t4:
    alpha = a
    lbl = f'alpha = {a}'
    sol = odeint(t4, ff, x_t4)
    plt.plot(x_t4, sol[:, 0], label = lbl, color = color)

plt.legend()
plt.show()

x_t5 = np.arange(-0.9999999, 1, 0.0001)
for i in range(2,9):
    n = i
    lbl = f'n = {i}'
    sol = odeint(t5, (1, 0), x_t5)
    plt.plot(x_t5, sol[:, 0], label = lbl)

plt.legend()
plt.show()