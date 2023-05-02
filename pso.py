import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import random

image = plt.imread('optimum_in_the_right.png')
array = np.asarray(image)
plt.imshow(array)


particles = {}
particles['gbest'] = np.array([random.uniform(0, 500), random.uniform(0, 500)])
for i in range(50):
	particles[i] = {}
	particles[i]['v'] = random.uniform(0, 1)
	particles[i]['d'] = np.array([random.uniform(0, 1), random.uniform(0, 1)])
	particles[i]['pbest'] = np.array([random.uniform(0, 500), random.uniform(0, 500)])

def update_particle(particle, gbest, w=0.9, c1=0.5, c2=0.5):
    v = particle['v']
    d = particle['d']
    pbest_i = particle['pbest']
    
    # Calculate the new velocity
    r1 = np.random.rand()
    r2 = np.random.rand()
    v_new = w * v + c1 * r1 * np.subtract(pbest_i, d) + c2 * r2 * np.subtract(gbest, d)
    
    # Update the particle's velocity and direction
    particle['v'] = v_new
    velocity_magnitude = np.linalg.norm(v_new)
    velocity_direction = np.arctan2(v_new[1], v_new[0])
    particle['d'] = (d[0] + np.cos(velocity_direction) * velocity_magnitude, 
                     d[1] + np.sin(velocity_direction) * velocity_magnitude)
    
    # Update the particle's best position
    if objective_function(d) < objective_function(pbest_i):
        particle['pbest'] = d
        
    return particle

def objective_function(point, data=array):
    x, y = point
    x = int(x)
    y = int(y)
    # Make sure the point is within the bounds of the image
    if x < 0 or x >= data.shape[0] or y < 0 or y >= data.shape[1]:
        return np.inf
    # Return the pixel value at the corresponding index in the image
    print(min(data[x, y]))
    return min(data[x, y])

for j in range(500):
	for k in range(50):
		particles[k] = update_particle(particles[k], particles['gbest'])
		if objective_function(particles[k]['d']) < objective_function(particles['gbest']):
			particles['gbest'] = particles[k]['d']

print(particles['gbest'])

x, y = particles['gbest']

# Mark the best point on the image
plt.scatter(x, y, color='red', s=100)

# Show the image
plt.show()
