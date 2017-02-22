
from .controller import Controller
from argparse import ArgumentParser
from matplotlib import pyplot as plt
import yaml
from os.path import dirname, join

def main():

    '''
    function will be executed at command line using 'boids' keyword
    '''

    config = yaml.load(open(dirname(__file__) + '/config.yaml'))
    parser = ArgumentParser()
    parser.add_argument('--size', '-s', type = int, default = config['size'])
    arguments = parser.parse_args()

    contl = Controller(size = arguments.size,
                       init_data = config['init_data'],
                       params = config['params'])

    anim = contl.go()
    plt.show()
