import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 20
t = np.linspace(0, years * seconds_in_year, frames)

def force(koeff1, koeff2, xa, xb, xc, ya, yb, yc, axis):     #рассчет силы взаимодейтствия

	G, ae1, M = 6.67e-11, 149e9, 1,98847e30
	dist = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 1.5
	d = [xa - xb, ya - yb]
	d1 = [xa - xc, ya - yc]
	ma = koeff1 * M
	mb = koeff2 * M
	F = (((- G * ma) / ma) * d[axis]) / dist) - (G * mb * d1[axis] / dist)
	return F


T1_x = force(1.06, 0.96, 0, 12.3 * 149e9, - 12.3 * 149e9, 0, 0, 0, 0)
T1_y = force(1.06, 0.96, 0, 12.3 * 149e9, - 12.3 * 149e9, 0, 0, 0, 1)

T2_x = force(0.96, 0.67, 12.3 * 149e9, 0, - 12.3 * 149e9, 0, 0, 0, 0)
T2_y = force(0.96, 0.67, 0, 12.3 * 149e9, - 12.3 * 149e9, 0, 0, 0, 1)

T3_x = force(0.67, 1.06, - 12.3 * 149e9, 0, 12.3 * 149e9, 0, 0, 0, 0)
T3_y = force(0.67, 1.06, - 12.3 * 149e9, 0, 12.3 * 149e9, 0, 0, 0, 1)

sol = odeint(force, , t)