import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import random
import math

image = plt.imread('optimum_in_the_right.png')
array = np.asarray(image)
plt.imshow(array)

def cooling():
	t = 50000
	current = np.array([random.uniform(0, 500), random.uniform(0, 500)])
	for i in range(t):
		x, y = current
		# let the neiborhood be 50 px
		new = np.array([random.uniform(x-25, x+25), random.uniform(y-25, y+25)])
		print("pixel value ", objective_function(new))
		if objective_function(new) == 0:
			current = new
			return current
		if objective_function(new) < objective_function(current):
			current = new
		if random.uniform(0, 1) < (math.e)**(-(objective_function(new) - objective_function(current))/t):
			current = new
		# linear cooling schedule
		t -= 1
	return current

def objective_function(s, data=array):
	x, y = s
	x = int(x)
	y = int(y)
	# Make sure the point is within the bounds of the image
	if x < 0 or x >= data.shape[0] or y < 0 or y >= data.shape[1]:
		return np.inf
	# Return the pixel value at the corresponding index in the image
	return min(data[x, y])

x, y = cooling()

# Mark the best point on the image
plt.scatter(x, y, color='red', s=100)

# Show the image
plt.show()