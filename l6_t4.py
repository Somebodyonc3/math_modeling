import numpy as np
import math as mt
import matplotlib.pyplot as plt

phi0 = 0.01
phi1 = 8 * np.pi

N = int(input('Введи как минимум 1000: '))

graphic = int(input('Пожалуйста введите: 1 - для логарифмической спирали, 2 - для арихмедовой спирали, 3 - для спирали жезл, 4 - для розы '))

phi = np.linspace(phi0 , phi1, N)

b = 0.02

if graphic == 1:
  
  r = np.exp(b * phi)

elif graphic == 2:

  k = float(input('Введите число:'))
  r = k * phi

elif graphic == 3:
  
  k = float(input('Введите число:'))
  r = k / np.sqrt(phi)

elif graphic == 4:

  k = float(input('Введите число (пж не вводи отрицательное):'))
  k = abs(k)
  r = np.sin(k * phi)

x = []
y = []

for i in range(N):
  
  x.append(r[i] * np.cos(phi[i]))
  y.append(r[i] * np.sin(phi[i]))

plt.plot(x,y)
plt.show()