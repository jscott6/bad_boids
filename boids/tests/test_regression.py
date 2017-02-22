
# this code is modified from
# http://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch05construction/10boids.html
# citations: James Hetherington

from boids.code.boids import Boids
import pytest
from os.path import dirname, split, join
import yaml
import numpy as np



config = yaml.load(open(split(dirname(__file__))[0] + '/code/config.yaml'))

def test_bad_boids_regression():
    regression_data = yaml.load(open(join(dirname(__file__),'fixture.yaml')))
    flock = Boids(size = 50)
    flock.positions = np.asarray(regression_data["before"][0:2])
    flock.velocities = np.asarray(regression_data["before"][2:])
    flock.update(config['params'])
    # check that positions match
    assert np.all(abs(np.asarray(regression_data["after"][0:2]) - flock.positions) < 1e-1)
    # check that velocities match
    assert np.all(abs(np.asarray(regression_data["after"][2:]) - flock.velocities) < 1e-1)
