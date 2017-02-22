
from .boids import Boids
from .view import View

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
                                       frames=200, interval=50)
        return anim
