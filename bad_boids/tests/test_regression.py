
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

    positions = np.asarray(regression_data["before"][0:2])
    velocities = np.asarray(regression_data["before"][2:])
    boids.update_boids(positions, velocities)
    # check that positions match
    assert np.all(abs(np.asarray(regression_data["after"][0:2]) - positions) < 1e-1)
    # check that velocities match
    assert np.all(abs(np.asarray(regression_data["after"][2:]) - velocities) < 1e-1)
