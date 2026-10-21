import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	x = np.array(X)
	y = np.array(y)

	X_t = np.transpose(x)
	A = np.dot(X_t, x)

	B = np.dot(X_t, y)

	C = np.linalg.inv(A)
	theta = np.dot(C,B)

	return np.round(theta, 4).tolist()