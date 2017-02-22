

class Controller(object):
    def __init__(self, size, init_data, params):
        self.flock = boids(50)
        self.view = View(self.flock.inititate(init_data))

        def animate(params):
            self.flock.update(params)
            self.view.update()

        self.animator = animate

    def go(self):
        from matplotlib import animation
        anim = animation.FuncAnimation(self.view.figure, self.animator, frames=200, interval=50)
        return anim()

    
