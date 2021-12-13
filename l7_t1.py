#График Циклоиды

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-2 * np.pi, 2  * np.pi, 0.1) 
R = 3
def cykloida(t, R):

  x = R * np.cos(t)
  y = R * np.sin(t)

  plt.plot(x, y, ls = '--', lw = 3)

  plt.axis('equal')

  plt.show()
cykloida(t, R)