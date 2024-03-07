import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colors

def move_ant(board, ant_position, ant_direction):

    if ant_direction == 'up':
        ant_position[1] += 1
    elif ant_direction == 'right':
        ant_position[0] += 1
    elif ant_direction == 'down':
        ant_position[1] -= 1
    elif ant_direction == 'left':
        ant_position[0] -= 1
    
    if board[ant_position[0]][ant_position[1]] == 0:
        board[ant_position[0]][ant_position[1]] = 1
        if ant_direction == 'up':
            ant_direction = 'right'
        elif ant_direction == 'right':
            ant_direction = 'down'
        elif ant_direction == 'down':
            ant_direction = 'left'
        elif ant_direction == 'left':
            ant_direction = 'up'

    else:
        board[ant_position[0]][ant_position[1]] = 0
        if ant_direction == 'up':
            ant_direction = 'left'
        elif ant_direction == 'left':
            ant_direction = 'down'
        elif ant_direction == 'down':
            ant_direction = 'right'
        elif ant_direction == 'right':
            ant_direction = 'up'
    return ant_direction


ant_direction = 'up'

def run_langton(board, ant_position):
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    im = plt.imshow(board, interpolation='none', cmap = plt.cm.gray, vmin=0, vmax=1)
    
    def animate(frame, ant_position):
        global ant_direction
        ant_direction = move_ant(board, ant_position, ant_direction)
        im.set_array(board)

        return im,

    anim = FuncAnimation(fig, animate, frames = 50, interval = 0.5, blit = True, fargs = (ant_position,))

    return anim