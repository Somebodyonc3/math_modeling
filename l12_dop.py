#Как это делать 0_о
import numpy as np
import matplotlib.pyplot as plt

r = 12
N = 16
V = 10
x_0, y_0 = 15, 20

pi = np.pi

def krug(N, r, V, x_0, y_0):
	
	cx = []
	cy = []
	vx = []
	vy = []
	dvx = []
	dvy = []
	for i in range(N):
		
		alpha = (2 * pi * i) / N
		x, y = r * np.sin(alpha) + x_0, r * np.cos(alpha) + y_0
		v_x, v_y = V * np.sin(alpha + pi / 2) + x , V * np.cos(alpha + pi / 2) + y
		
		cx.append(x)
		cy.append(y)
		vx.append(v_x)
		vy.append(v_y)
		dvx.append(v_x - x)
		dvy.append(v_y - y)
	return cx, cy, vx, vy, dvx, dvy

cx, cy, vx, vy, dvx, dvy = krug(N, r, V, x_0, y_0)
plt.scatter(cx, cy)
for i in range(len(cx)):
	
	plt.arrow(cx[i], cy[i], dvx[i], dvy[i])

plt.scatter(vx, vy)
plt.axis('equal')
plt.show()