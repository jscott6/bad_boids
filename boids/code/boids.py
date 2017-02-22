
from .funcs import *

# create a boids class

class Boids(object):

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
