import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def dead_state(width, height):
    board = []
    for i in range(height):
        row = [0] * width
        board.append(row)
    return board

def random_number(probability):
    random_number = random.random()
    if random_number >= probability:
        return 0
    else:
        return 1

def random_state(width, height):
    state = dead_state(width, height)
    for x in range(0, height):
        for y in range(0, width):
            state[x][y] = random_number(0.5)
    return state

def render(board):
    width = len(board[0])
    height = len(board)
    print((width + 2) * '-')
    for row in board:
        print('|', end = '')
        for cell in row:
            print(u"\u2588" if cell == 1 else ' ', end = '')
        print('|')
    print((width + 2) * '-')

def next_board_state(initial_board):
    width = len(initial_board[0])
    height = len(initial_board)
    next_board = [[0 for _ in range(width)] for _ in range(height)]
    for x, row in enumerate(initial_board):
        for y, item in enumerate(row):
            counts = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    nx, ny = x + dx, y + dy
                    if dx == 0 and dy == 0:
                        continue
                    if 0 <= nx < height and 0 <= ny < width:
                        if initial_board[nx][ny] == 1:
                            counts += 1
        
            if initial_board[x][y]: #checks if the cell is alive   
                if counts <= 1:
                    next_board[x][y] = 0
                elif counts == 2 or counts == 3:
                    next_board[x][y] = 1
                elif counts > 3:
                    next_board[x][y] = 0
            else:
                if counts == 3:
                    next_board[x][y] = 1 
    return(next_board)

def load_board_state(file):
    f = open(file, 'r')
    state = []
    for line in f:
        state_row = []
        for character in line.strip():
            state_row.append(int(character))
        state.append(state_row)
    f.close()
    return state

def run_forever(init_state):
    next_state = init_state
    fig = plt.figure()

    plt.grid(True)
    plt.rc('grid', linestyle="-", color='white')

    im = plt.imshow(init_state, cmap = plt.cm.gray)

    def update(frame):
        nonlocal init_state
        init_state = next_board_state(init_state)
        im.set_array(init_state)
        return im,

    anim = FuncAnimation(fig, update, frames = 50, interval = 1000/60, blit = True)

    return anim

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


def start_animation():
    #board = random_state(200, 200)
    board = dead_state(100, 100)
    width = len(board[0])
    height = len(board)
    ant_position = [width // 2, height // 2]
    #board = load_board_state("pulsar.txt")
    #anim = run_forever(board)
    anim2 = run_langton(board, ant_position)
    plt.show()

start_animation()
