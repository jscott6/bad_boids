
from boids.code.boids import Boids
import numpy as np

'''
 we test each method of the class boids
 we omit testing of the method 'update' as this is effectively handled
 by the unit tests in test_funcs and the regression test together.

'''
def test_init():

    # test correct instantiation
    size = 50
    flock = Boids(size)
    assert flock.size == size


def test_initiate():

    # test initiated positions and velocities obey init_data
    test_range = [0.0, 1.0]
    init_data = {'pos_low': test_range,'pos_high': test_range,
                'vel_low': test_range, 'vel_high': test_range}

    size = 100
    flock = Boids(size)
    flock.initiate(init_data)

    assert np.shape(flock.positions) == (2, size)
    assert np.shape(flock.velocities) == (2,size)
    assert np.min(flock.positions) >= min(test_range)
    assert np.max(flock.positions) <= max(test_range)
    assert np.min(flock.velocities) >= min(test_range)
    assert np.max(flock.velocities) <= max(test_range)
