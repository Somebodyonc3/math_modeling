import matplotlib.pyplot as plt
import numpy

Xa = int(input("Отрицательное пжпжпжпжп:"))
Xb = int(input('Равное по  модулю первому числу:'))
N = int(input())

'''
a = int(input()) 
b = int(input())
c = int(input())
'''

def parabola(a, b, c, k, Xa, Xb, N,  title = 'Парабола'):
  
  x = numpy.linspace(Xa, Xb, N)
  y = a * x ** 2 + b * x + c

  plt.plot(x, y, label = 'Парабола, Finally!')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title(title)
  plt.legend()
  plt.show()

#parabola(a, b, c, k, Xa, Xb, N)

k = int(input('Неравное нулю:'))

def hyperbola(k, Xa, Xb, title = 'Гипербола'):
 
  x1 = numpy.linspace(Xa,Xb, N)
  x1 = numpy.around(x1, decimals = 4)
  x1 = numpy.ma.masked_where(abs(x1) == 0.000001, x1)

  y1 = k / x1

  y3 = numpy.ma.masked_where(abs(x1) == 0.000001, y1)

  plt.plot(x1, y3, label = 'Гипербола, Ура!')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title(title)
  plt.legend()
  plt.show()

hyperbola(k, Xa, Xb) 
#разкомментируй чтоб увидеть Гиперболу и закоментируй параболу и наоборот