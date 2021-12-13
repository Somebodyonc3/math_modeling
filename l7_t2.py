#Расширяющаяся окружность

import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
line, = plt.plot([], [], '--', color = 'blue', label = 'line')
 
edge = 10
 
plt.axis('equal')
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
x = []
y = []

a = 0.254
S = numpy.arange(0, 2 * numpy.pi, 0.1)
sin_S = numpy.sin(S)
cos_S = numpy.cos(S)

def animate(frame):
    R = frame * a

    x = R * sin_S
    y = R * cos_S
 
    line.set_data(x, y)
 
ani = animation.FuncAnimation(fig,
                        animate,
                        frames = 100,
                        interval = 30)
 
ani.save('my2.gif')
