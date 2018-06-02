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

def updatefig(frame):
    coord[1] = coord[1] + velocity[1] * 0.5 
    velocity[1] = velocity[1] - g 
    if coord[1] <= 236.:
        coord[1] = 236 
    circle.set_xdata(coord[0])
    circle.set_ydata(coord[1])
    return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=10000, init_func=init, interval=30, blit=True, repeat=False)
plt.show()
