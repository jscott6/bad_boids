

class View(object):

    '''
    View class used in controller to animate results
    '''

    def __init__(self, flock):

        # initialise figure object
        from matplotlib import pyplot as plt
        self.fig = plt.figure()
        axes = plt.axes(xlim = (-500,1500), ylim = (-500,1500))
        self.flock = flock
        self.scatter = axes.scatter(self.flock.positions[0], self.flock.positions[1])


    def update(self):
        # update scatter points
        self.scatter.set_offsets((self.flock.positions[0], self.flock.positions[1]))
