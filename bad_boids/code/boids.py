
from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

def initiate_array(size, low, high):
    return [random.uniform(low, high) for x in range(size)]

no_boids = 50

# initialise (x,y) positions of boids uniformly
boids_x = initiate_array(no_boids, -450.0, 50.0)
boids_y = initiate_array(no_boids, 300.0, 600.0)
# initialise (x,y) velocities of boids uniformly
boid_x_velocities = initiate_array(no_boids, 0.0, 10.0)
boid_y_velocities = initiate_array(no_boids, -20.0, 20.0)

boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

# separate functions for updating positions and velocities
# change from list structures to numpy arrays
# does it make sense to treat x and y separately, or put
# them in the same array?
# stop for range, and use for x in array
# vectorisation of the code

def update_velocities(position, velocity):

    for item in velocity:
        item = item + ()


def update_boids(boids):
    xs,ys,xvs,yvs=boids
    # Fly towards the middle
    for i in range(no_boids):
        for j in range(no_boids):
            xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs)
    for i in range(no_boids):
        for j in range(no_boids):
            yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)
    # Fly away from nearby boids
    for i in range(no_boids):
        for j in range(no_boids):
                if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
                     xvs[i]=xvs[i]+(xs[i]-xs[j])
                     yvs[i]=yvs[i]+(ys[i]-ys[j])
    # Try to match speed with nearby boids
    for i in range(no_boids):
        for j in range(no_boids):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
    # Move according to velocities
    for i in range(no_boids):
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
    update_boids(boids)
    scatter.set_offsets((boids[0],boids[1]))

anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
