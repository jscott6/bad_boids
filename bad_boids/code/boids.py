
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
from funcs import initiate_array, middle, calc_distances, avoid_boids, match_boids

# create a boids class

class boids(object):

    def __init__(self, size = 50):
        self.size = size

    def initiate(self, init_data = {'pos_low': np.array([0.0, 0.0]),
                                    'pos_high': np.array([100.0, 100.0]),
                                    'vel_low': np.array([-10.0, -10.0]),
                                    'vel_high': np.array([10.0, 10.0])}):

        self.positions = initiate_array(self.size, init_data['pos_low'], init_data['pos_high'])
        self.velocities = initiate_array(self.size, init_data['vel_low'], init_data['vel_high'])

    def update(self, params = {'middle_strength': 0.01,
                               'avoid_dist': 100,
                               'match_dist': 10000,
                               'match_strength': 0.125}):

        # update velocity
        # fly towards middle
        middle(self.positions, self.velocities, params['middle_strength'])
        # calculate displacement and squared distance for use in avoid_boids, match_boids
        displacement, sq_distances = calc_distances(self.positions)
        # fly away from nearby boids
        avoid_boids(self.positions, self.velocities, sq_distances, displacement, params['avoid_dist'])
        # match velocity of nearby boids
        match_boids(self.positions, self.velocities, sq_distances, params['match_dist'], params['match_strength'])
        # Move according to velocities
        self.positions += self.velocities

# set initialisatin parameters for our flock
init_data =  {'pos_low': np.array([-450.0, 300.0]),
              'pos_high': np.asarray([50.0, 600.0]),
              'vel_low': np.asarray([0.0, -20.0]),
              'vel_high': np.asarray([10.0, 20.0])}

# instantiate a flock with appropriate parameters
flock = boids(size = 50)
# initiate position and velocities of boids
flock.initiate(init_data)
# update the position and velocities
flock.update()

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(flock.positions[0],flock.positions[1])

def animate(frame):
    flock.update()
    scatter.set_offsets((flock.positions[0],flock.positions[1]))

anim = animation.FuncAnimation(figure, animate, frames=200, interval=50)

if __name__ == "__main__":
    plt.show()
