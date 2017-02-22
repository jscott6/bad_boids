
import numpy as np

def initiate_array(size, low, high):

    '''
    used to create position and velocity arrays
    '''

    np_low = np.array(low)
    np_high = np.array(high)
    return np_low[:,np.newaxis] + np.random.rand(2, size)*(np_high[:,np.newaxis] - np_low[:,np.newaxis])


def middle(positions, velocities, strength):

    '''
    Fly towards the middle
    '''

    means = np.mean(positions,1)
    direction = positions - means[:,np.newaxis]
    velocities -= direction*strength


def calc_distances(positions):

    '''
    returns boid displacements and sq_distances which are supplied to
    avoid_boids and match_boids
    '''

    displacement = positions[:, np.newaxis,:] - positions[:,:,np.newaxis]
    sq_displacement = displacement*displacement
    sq_distances = np.sum(sq_displacement, 0)

    return (displacement,sq_distances)

def avoid_boids(positions, velocities, sq_distances, displacement, dist):

    '''
    Fly away from nearby boids
    '''

    close = sq_distances > dist
    displacement_if_close = np.copy(displacement)
    displacement_if_close[0,:,:][close] = 0
    displacement_if_close[1,:,:][close] = 0
    velocities += np.sum(displacement_if_close,1)


def match_boids(positions, velocities, sq_distances, dist, strength):

    '''
    Try to match speed with nearby boids
    '''
    
    velocity_deltas = velocities[:,np.newaxis,:] - velocities[:,:, np.newaxis]
    distant_boids = sq_distances > dist
    velocity_deltas_if_close = np.copy(velocity_deltas)
    velocity_deltas_if_close[0,:,:][distant_boids] = 0
    velocity_deltas_if_close[1,:,:][distant_boids] = 0
    velocities -= np.mean(velocity_deltas_if_close,1)*strength
