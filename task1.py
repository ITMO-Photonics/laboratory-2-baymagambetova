import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

circle, = ax.plot([], [], 'bo', ms=20)
coord = np.array([5000.,9000.]) 
velocity = np.array([0.,0.]) 

def init():
    ax.set_xlim([0., 10000.])
    ax.set_ylim([0., 10000.])
    return circle, 

g = 9.8
def Euler(coord,velocity, g):           
    coord[1] = coord[1] + velocity[1] * 0.5
    velocity[1] = velocity[1] - g
    return coord

h = 3./6. 
def RungeKutta(coord, velocity, h, g):
    k1 = velocity [1]
    k2 = velocity[1] - g
    coord[1] = coord[1] + h * (k1 + k2) * 0.5
    velocity[1] = velocity[1] - 9.8
    return coord

def updatefig(frame):

    
    RungeKutta(coord, velocity, h, g)

    circle.set_xdata(coord[0])
    circle.set_ydata(coord[1])
    return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=10000, init_func=init, interval=30, blit=True, repeat=False)
plt.show()
