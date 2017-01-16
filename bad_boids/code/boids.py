
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

# Deliberately terrible code for teaching purposes

def initiate_array(size, low, high):
    return low[:,np.newaxis] + np.random.rand(2, size)*(high[:,np.newaxis] - low[:,np.newaxis])

no_boids = 50

# initialise (x,y) positions of boids uniformly
positions = initiate_array(no_boids, np.array([-450.0,300.0]), np.array([300.0,600.0]))
velocities = initiate_array(no_boids, np.array([0.0,-20.0]), np.array([10.0,20.0]))

boids= np.asarray([positions[0], positions[1],velocities[0], velocities[1]])


# separate functions for updating positions and velocities
# change from list structures to numpy arrays
# does it make sense to treat x and y separately, or put
# them in the same array?
# stop for range, and use for x in array
# vectorisation of the code

def update_velocities(position, velocity):

    for item in velocity:
        item = item + ()


def update_boids(boids):

    positions, velocities = (boids[0:2], boids[2:4])

    # Fly towards the middle
    means = np.mean(positions,1)
    direction = positions - means[:,np.newaxis]
    velocities -= direction*0.01

    # Fly away from nearby boids
    displacement = positions[:, np.newaxis,:] - positions[:,:,np.newaxis]
    sq_displacement = displacement*displacement
    sq_distances = np.sum(sq_displacement, 0)
    crit_distance = 100
    close = sq_distances > crit_distance
    displacement_if_close = np.copy(displacement)
    displacement_if_close[0,:,:][close] = 0
    displacement_if_close[1,:,:][close] = 0
    velocities += np.sum(displacement_if_close,1)

    # Try to match speed with nearby boids
    for i in range(no_boids):
        for j in range(no_boids):
            if np.sum((positions[:,j]-positions[:,i])**2) < 10000:
                velocities[:,i] += (velocities[:,j]-velocities[:,i])*0.125/no_boids

    # Move according to velocities
    for i in range(no_boids):
        positions[:,i] += velocities[:,i]

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
    update_boids(boids)
    scatter.set_offsets((boids[0],boids[1]))

anim = animation.FuncAnimation(figure, animate, frames=200, interval=50)

if __name__ == "__main__":
    plt.show()
