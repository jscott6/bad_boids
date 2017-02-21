
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

# create a boids class

class boids(object):

    def __init__(self,
                 size = 50,
                 data = {'pos_low': np.asarray(0.0, 0.0),
                         'pos_high': np.asarray(100.0, 100.0),
                         'vel_low': np.asarray(-10.0, -10.0),
                         'vel_high': np.asarray(10.0, 10.0)},
                 params = {'middle_strength': 0.01,
                            'avoid_dist': 100,
                            'match_dist': 10000,
                            'match_strength': 0.125
                            }):

                            self.size = size
                            self.data = data
                            self.params = params

    def initiate(self):
        self.positions = initiate_array(self.size, self.data['pos_low'], self.data['pos_high'])
        self.velocities = initiate_array(self.size, self.data['vel_low'], self.data['vel_high'])

    def update(self):
        update_boids(self.positions, self.velocities)



def initiate_array(size, low, high):
    return low[:,np.newaxis] + np.random.rand(2, size)*(high[:,np.newaxis] - low[:,np.newaxis])

no_boids = 50

# initialise (x,y) positions of boids uniformly
positions = initiate_array(no_boids, np.array([-450.0,300.0]), np.array([300.0,600.0]))
velocities = initiate_array(no_boids, np.array([0.0,-20.0]), np.array([10.0,20.0]))


def middle(positions, velocities, strength):

    # Fly towards the middle
    means = np.mean(positions,1)
    direction = positions - means[:,np.newaxis]
    velocities -= direction*strength


def calc_distances(positions):

    displacement = positions[:, np.newaxis,:] - positions[:,:,np.newaxis]
    sq_displacement = displacement*displacement
    sq_distances = np.sum(sq_displacement, 0)

    return (displacement,sq_distances)

def avoid_boids(positions, velocities, sq_distances, displacement, dist):

    # Fly away from nearby boids
    close = sq_distances > dist
    displacement_if_close = np.copy(displacement)
    displacement_if_close[0,:,:][close] = 0
    displacement_if_close[1,:,:][close] = 0
    velocities += np.sum(displacement_if_close,1)


def match_boids(positions, velocities, sq_distances, dist, strength):

    # Try to match speed with nearby boids
    velocity_deltas = velocities[:,np.newaxis,:] - velocities[:,:, np.newaxis]
    distant_boids = sq_distances > dist
    velocity_deltas_if_close = np.copy(velocity_deltas)
    velocity_deltas_if_close[0,:,:][distant_boids] = 0
    velocity_deltas_if_close[1,:,:][distant_boids] = 0
    velocities -= np.mean(velocity_deltas_if_close,1)*strength


def update_boids(positions, velocities):

    # update velocity
    # fly towards middle
    middle(positions, velocities, 0.01)

    # calculate displacement and squared distance for use in avoid_boids, match_boids
    displacement, sq_distances = calc_distances(positions)

    # fly away from nearby boids
    avoid_boids(positions, velocities, sq_distances, displacement, 100)

    # match velocity of nearby boids
    match_boids(positions, velocities, sq_distances, 10000, 0.125)

    # Move according to velocities
    positions += velocities

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(positions[0],positions[1])

def animate(frame):
    update_boids(positions, velocities)
    scatter.set_offsets((positions[0],positions[1]))

anim = animation.FuncAnimation(figure, animate, frames=200, interval=50)

if __name__ == "__main__":
    plt.show()
