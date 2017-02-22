
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import yaml
from os.path import join, dirname
from .funcs import initiate_array, middle, calc_distances, avoid_boids, match_boids

# create a boids class

class boids(object):

    def __init__(self, size = 50):
        self.size = size

    def initiate(self, init_data):
        self.positions = initiate_array(self.size, init_data['pos_low'], init_data['pos_high'])
        self.velocities = initiate_array(self.size, init_data['vel_low'], init_data['vel_high'])

    def update(self, params):

        ''' ___UPDATE VELOCITY___'''
        # fly towards middle
        middle(self.positions, self.velocities, params['middle_strength'])
        # calculate displacement and squared distance for use in avoid_boids, match_boids
        displacement, sq_distances = calc_distances(self.positions)
        # fly away from nearby boids
        avoid_boids(self.positions, self.velocities, sq_distances, displacement, params['avoid_dist'])
        # match velocity of nearby boids
        match_boids(self.positions, self.velocities, sq_distances, params['match_dist'], params['match_strength'])

        ''' ___UPDATE POSITIONS___'''
        self.positions += self.velocities


config = yaml.load(open(join(dirname(__file__), 'config.yaml')))
# instantiate a flock with appropriate parameters
flock = boids(50)
# initiate position and velocities of boids
flock.initiate(config['init_data'])
# update the position and velocities
flock.update(config['params'])

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(flock.positions[0],flock.positions[1])

def animate(frame):
    flock.update(config['params'])
    scatter.set_offsets((flock.positions[0],flock.positions[1]))

anim = animation.FuncAnimation(figure, animate, frames=200, interval=50)

if __name__ == "__main__":
    plt.show()
