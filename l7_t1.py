#График Циклоиды

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-2*np.pi, 2*np.pi, 0.1)
R = 2

def cykloida(t, R):

  x = R * (t - np.sin(t) ** 3)
  y = R * (1 - np.cos(t) ** 3)

  plt.plot(x, y, lw = 3)

  plt.axis('equal')

  plt.show()

cykloida(t, R)

# График Астроиды

def astroida(t, R):

  x = R * np.cos(t) ** 3
  y = R * np.sin(t) ** 3

  plt.plot(x, y, lw = 3)

  plt.axis('equal')

  plt.show()

astroida(t, R)