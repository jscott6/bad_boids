

class View(object):
    def __init__(self, flock):
        from matplotlib import pyplot as plt
        self.fig = plt.figure()
        axes = plt.axes(xlim = (-500,1500), ylim = (-500,1500))
        self.flock = flock
        self.scatter = axes.scatter(self.flock.positions[0], self.flock.positions[1])


    def update(self):
        self.scatter.set_offsets((self.flock.positions[0], self.flock.positions[1]))
