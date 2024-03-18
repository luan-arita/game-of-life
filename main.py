import random
#import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colors
from matplotlib import animation
import argparse
import langton, seeds, brians, rockpaperscissors


parser = argparse.ArgumentParser(description = "Conway's Game of Life")
parser.add_argument("-w", "--width", type = int, help = "Choose board's width.", default = 100)
parser.add_argument("-hs", "--height", type = int, help = "Choose board's height.", default = 100)
parser.add_argument("-g", "--game", type = int, choices = [1, 2, 3, 4, 5], default = 1, help = " Choose which cellular automata you want to run. 1 is the default Game of Life, 2 is Langton's Ant, 3 is Seeds, 4 is Brian's Brain and 5 is Rock Paper Scissors.")
parser.add_argument("-f", "--file", type=argparse.FileType('r'), default = None)

args = parser.parse_args()


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
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
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
    #f = open(file, 'r')
    state = []
    for line in file:
        state_row = []
        for character in line.strip():
            state_row.append(int(character))
        state.append(state_row)
    #f.close()
    return state

def run_forever(init_state, next_state_func):
    
    fig = plt.figure()

    plt.box(on=None)
    plt.axis('off')
    plt.rc('grid', linestyle="-", color='white')
    cmap = colors.ListedColormap(['black', 'white', 'deepskyblue'])
    bounds = [0, 1, 2, 3]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    im = plt.imshow(init_state,interpolation = 'nearest', cmap = cmap, norm = norm)

    def update(frame):
        nonlocal init_state
        init_state = next_state_func(init_state)
        im.set_array(init_state)
        return im,

    anim = FuncAnimation(fig, update, frames = 150, interval = 1000/30, blit = True)

    return anim

if args.file:
    board = load_board_state(args.file)
    if args.game == 1:
        anim = run_forever(board, next_board_state)
    elif args.game == 2:
        width = len(board[0])
        height = len(board)
        ant_position = [width // 2, height // 2]
        anim = langton.run_langton(board, ant_position)
    elif args.game == 3:
        anim = run_forever(board, seeds.seeds)
    elif args.game == 4:
        anim = run_forever(board, brians.brians_brain)
else:
    if args.game == 1:
        board = random_state(args.width, args.height)
        anim = run_forever(board, next_board_state)
    elif args.game == 2:
        board = dead_state(args.width, args.height)
        width = len(board[0])
        height = len(board)
        ant_position = [width // 2, height // 2]
        anim = langton.run_langton(board, ant_position)
    elif args.game == 3:
        board = random_state(args.width, args.height)
        anim = run_forever(board, seeds.seeds)
    elif args.game == 4:
        board = random_state(args.width, args.height)
        anim = run_forever(board, brians.brians_brain)
    elif args.game == 5:
        board = rockpaperscissors.board_rps(args.height)
        anim = rockpaperscissors.run_forever_rps(board, rockpaperscissors.next_board_state_rps)

#plt.show()

def save_gif():
    f = r"c:\Users\Luan\Desktop\faculdade\Python\game-of-life\animation.gif" 
    writergif = animation.PillowWriter(fps=15) 
    anim.save(f, writer=writergif)

save_gif()



