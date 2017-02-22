
from bad_boids.code.funcs import *
import numpy as np
from numpy.testing import assert_array_equal

def test_initiate_array():

    low = [0.0, 0.0]
    high = [1.0, 1.0]
    size = 100

    test_array = initiate_array(size, low, high)

    assert np.shape(test_array) == (2,size)
    assert np.min(test_array) >= min(low)
    assert np.max(test_array) <= max(high)


def test_middle():

    positions = np.array([[-1.,1.],[-1.,1.]])
    velocities = np.zeros((2,2))
    strength = 0.1
    true_velocity = -positions*strength
    middle(positions, velocities, strength)
    assert_array_equal(velocities, true_velocity)


def test_calc_distances():

    positions = np.array([[-1.,1.],[-1.,1.]])
    true_displacement_1 = np.array([[0.,-2.],[0.,-2.]])
    true_displacement_2 = np.array([[2.,0.], [2.,0.]])
    true_sq_distance = np.array([[0.,8.], [8.,0.]])

    displacement, sq_distance = calc_distances(positions)

    assert np.shape(displacement) == (2,2,2)
    assert_array_equal(displacement[:,:,0], true_displacement_1)
    assert_array_equal(displacement[:,:,1], true_displacement_2)
    assert_array_equal(sq_distance, true_sq_distance)


def test_avoid_boids():

    positions = np.array([[0.,3.,4.],[0.,3.,4.]])
    dist = 4
    displacement, sq_distances = calc_distances(positions)
    velocities = np.zeros((2,3))
    avoid_boids(positions, velocities, sq_distances, displacement, dist)

    assert_array_equal(velocities, np.array([[0.,-1.,1.],[0.,-1.,1.]]))


def test_match_boids():

    positions = np.array([[0.,3.,4.],[0.,3.,4.]])
    dist = 4
    displacement, sq_distances = calc_distances(positions)
    velocities = np.array([[0.,0.,9.],[0.,0.,9.]])
    strength = 1.0
    match_boids(positions, velocities, sq_distances, dist, strength)

    assert_array_equal(velocities, np.array([[0.,3.,6.],[0.,3.,6.]]))
