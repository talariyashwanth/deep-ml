import numpy as np
def orthogonal_projection(v, L):
	v = np.array(v)
	L = np.array(L)
	c = np.dot(v,L)
	d = np.dot(L,L)
	first = c / d 
	result = first * L
	return result.tolist()
	pass
