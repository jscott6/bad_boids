
from .boids import Boids
from .view import View
import yaml
from os.path import join, dirname
from matplotlib import pyplot as plt

class Controller(object):
    def __init__(self, size, init_data, params):
        self.flock = Boids(size)
        self.flock.initiate(init_data)
        self.view = View(self.flock)
        self.params = params

        def animate(frame):
            self.flock.update(self.params)
            self.view.update()

        self.animator = animate

    def go(self):
        from matplotlib import animation
        anim = animation.FuncAnimation(self.view.fig, self.animator,
                                       frames=200, interval=30)
        return anim


config = yaml.load(open(join(dirname(__file__), 'config.yaml')))

contl = Controller(size = config['size'],
                   init_data = config['init_data'],
                   params = config['params'])

anim = contl.go()


if __name__ == "__main__":
    plt.show()
