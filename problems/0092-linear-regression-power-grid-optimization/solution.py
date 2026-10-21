import numpy as np
import math

PI = 3.14159

def power_grid_forecast(consumption_data):
	detrend_data = []
	for i in range(1,11):
		fluctuation = 10 * math.sin((2 * PI * i)/10)
		detrend_data.append(consumption_data[i-1] - fluctuation)
	days = np.arange(1,11)
	ones = np.ones(10)
	X = np.column_stack((ones, days))

	y = np.array(detrend_data)

	X_t = X.T
	A = np.dot(X_t, X)
	B = np.dot(X_t, y)
	theta = np.dot(np.linalg.inv(A), B)

	day_15 = np.array([1,15])
	base_prediction = np.dot(day_15, theta)

	fluctuation_15 = 10 * math.sin((2 * PI * 25) / 10)
	actual_prediction = base_prediction + fluctuation_15

	final_prediction = math.ceil(actual_prediction * 1.05)

	return final_prediction
	pass