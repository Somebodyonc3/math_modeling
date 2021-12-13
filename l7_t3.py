#Бабочка

import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
line, = plt.plot([], [], '--', color = 'green', label = 'line')
 
edge = 10
 
plt.axis('equal')
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
x = []
y = []
 
def animate(frame):
    t = frame
    d = numpy.exp(numpy.cos(t)) - 2 * numpy.cos(4 * t) + (numpy.sin(t / 12)) ** 5
    
    xn = numpy.sin(t) * d
    yn = numpy.cos(t) * d
 
    x.append(xn)
    y.append(yn)
    line.set_data(x, y)
 
ani = animation.FuncAnimation(fig,
                        animate,
                        frames = numpy.arange(0, 10, 0.1),
                        interval = 30)
 
ani.save('my.gif')
