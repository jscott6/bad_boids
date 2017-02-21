
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


def middle(positions, velocities):

    # Fly towards the middle
    means = np.mean(positions,1)
    direction = positions - means[:,np.newaxis]
    velocities -= direction*0.01


def calc_sq_distances(positions):

    displacement = positions[:, np.newaxis,:] - positions[:,:,np.newaxis]
    sq_displacement = displacement*displacement
    sq_distances = np.sum(sq_displacement, 0)

    return (displacement,sq_distances)

def avoid_boids(positions, velocities, sq_distances, displacement):

    # Fly away from nearby boids
    crit_distance = 100
    close = sq_distances > crit_distance
    displacement_if_close = np.copy(displacement)
    displacement_if_close[0,:,:][close] = 0
    displacement_if_close[1,:,:][close] = 0
    velocities += np.sum(displacement_if_close,1)


def match_boids(positions, velocities, sq_distances):

    # Try to match speed with nearby boids
    velocity_deltas = velocities[:,np.newaxis,:] - velocities[:,:, np.newaxis]
    distant_boids = sq_distances > 10000
    velocity_deltas_if_close = np.copy(velocity_deltas)
    velocity_deltas_if_close[0,:,:][distant_boids] = 0
    velocity_deltas_if_close[1,:,:][distant_boids] = 0
    velocities -= np.mean(velocity_deltas_if_close,1)*0.125


def update_boids(boids):

    positions, velocities = (boids[0:2], boids[2:4])

    # update velocity

    middle(positions, velocities)
    displacement, sq_distances = calc_sq_distances(positions)
    avoid_boids(positions, velocities, sq_distances, displacement)
    match_boids(positions, velocities, sq_distances)

    # Move according to velocities
    positions += velocities

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
    update_boids(boids)
    scatter.set_offsets((boids[0],boids[1]))

anim = animation.FuncAnimation(figure, animate, frames=200, interval=50)

if __name__ == "__main__":
    plt.show()
