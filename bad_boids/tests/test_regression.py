
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

    boid_data = np.asarray(regression_data["before"])
    boids.update_boids(boid_data)
    assert np.all(abs(np.asarray(regression_data["after"]) - boid_data) < 1e-1)
