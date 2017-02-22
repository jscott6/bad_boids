

class View(object):
    def __init__(self, flock):
        from matplotlib import pyplot as plt
        self.figure = plt.figure()
        axes = plt.axes()
        self.flock = flock
        self.scatter = axes.scatter(flock.positions[0], flock.positions[1])


    def update(self):
        self.scatter.set_offsets((flock.positions[0], flock.positions[1]))
