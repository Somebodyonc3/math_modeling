def force(v0, dist, koeff1, s, axis):

	G, ae1, M = 6.67e-11, 149e9, 1,98847e30
	dist = s * ae1
	m = koeff * M
	F = ((- G * mb + k * qa * qb / ma) * d[axis]) / dist
	return F