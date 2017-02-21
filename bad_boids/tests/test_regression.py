
# this code is modified from
# http://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch05construction/10boids.html
# citations: James Hetherington

from bad_boids.code import boids
import pytest
import os
import yaml
import numpy as np

def test_bad_boids_regression():
    regression_data = yaml.load(open(
        os.path.join(os.path.dirname(__file__),
        'fixture.yaml')))

    '''
    regression_data = yaml.load(open("/Users/jamesscott/Documents/bad_boids/bad_boids/tests/fixture.yaml"))

    '''

    flock = boids(size = 50)
    flock.positions = np.asarray(regression_data["before"][0:2])
    flock.velocities = np.asarray(regression_data["before"][2:])
    flock.update()
    # check that positions match
    assert np.all(abs(np.asarray(regression_data["after"][0:2]) - flock.positions) < 1e-1)
    # check that velocities match
    assert np.all(abs(np.asarray(regression_data["after"][2:]) - flock.velocities) < 1e-1)
