
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	usq = sum([u*u for u in L])
	dotp = sum([u*v for u,v in zip(L, v)])

	if usq == 0:
		return

	return [(dotp/usq) * u for u in L]
