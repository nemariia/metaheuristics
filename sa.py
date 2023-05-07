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
	# current solution, initially set to random
	current = np.array([random.uniform(0, 500), random.uniform(0, 500)])
	delta = []
	for i in range(10):
		x, y = current
		new = np.array([random.uniform(x-25, x+25), random.uniform(y-25, y+25)])
		delta.append(abs(objective_function(new) - objective_function(current)))
		current = new
	t = np.mean(delta) / math.log(2)
	print("initial temperature is ", t)
	bestV = 1
	bestS = []
	for i in range(10000):
		x, y = current
		# let the neiborhood be 50 px
		new = np.array([random.uniform(x-25, x+25), random.uniform(y-25, y+25)])
		print("pixel value ", objective_function(new))
		if objective_function(new) < objective_function(current):
			current = new
		if random.uniform(0, 1) < (math.e)**(-(objective_function(new) - objective_function(current))/t):
			current = new
		if objective_function(current) <= bestV:
			bestV = objective_function(new)
			bestS = current
		# linear cooling schedule
		t -= 0.01
	print(bestV, bestS)
	return bestS

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