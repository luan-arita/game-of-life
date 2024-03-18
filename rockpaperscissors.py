import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colors
from matplotlib import animation

def board_rps(height):
    board = []
    #row1 = [0]*height
    #board.append(row1)
    row = []
    for i in range(height):
        if i < (height / 2):
            row = [1] * i + [0] * (height - 2 * i) + [2] * i
        else:
            row = [1] * (height // 2) + [2] * (height // 2)

        board.append(row)
    return(board)

def rps_logic(player1, player2):
    """0 = rock, 1 = """
    if player1 == player2:
        return 'draw'
    if player1 == 0 and player2 == 1:
        return 1
    elif player1 == 1 and player2 == 0:
        return 1
    if player1 == 0 and player2 == 2:
        return 0
    elif player2 == 0 and player1 == 2:
        return 0
    if player1 == 1 and player2 == 2:
        return 2
    elif player2 == 1 and player1 == 2:
        return 2


def next_board_state_rps(rps_board):
    width = len(rps_board[0])
    height = width
    next_board = [[0 for _ in range(width)] for _ in range(height)]

    for x, row in enumerate(rps_board):
        for y, item in enumerate(row):
            dx, dy = random.randint(-1, 1), random.randint(-1, 1)
            nx, ny = x + dx, y + dy
            if 0 <= nx < height and 0 <= ny < width:
                if rps_logic(rps_board[x][y], rps_board[nx][ny]) == 'draw':
                    next_board[x][y] = rps_board[x][y]
                else:
                    next_board[x][y] = rps_logic(rps_board[x][y], rps_board[nx][ny])
    return next_board


def run_forever_rps(init_state, next_state_func):
    
    fig = plt.figure(frameon = False)
    

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.box(on=None)
    plt.axis('off')
    plt.rc('grid', linestyle="-", color='white')
    cmap = colors.ListedColormap(['gold', 'orange', 'orangered'])
    bounds = [0, 1, 2, 3]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    im = plt.imshow(init_state,interpolation = 'nearest', cmap = cmap, norm = norm, aspect = 'equal')

    def update(frame):
        nonlocal init_state
        init_state = next_state_func(init_state)
        im.set_array(init_state)
        return im,

    anim = FuncAnimation(fig, update, frames = 200, interval = 1000/60, blit = True)

    return anim



def save_gif():
    f = r"c:\Users\Luan\Desktop\faculdade\Python\game-of-life\animation.gif" 
    writergif = animation.PillowWriter(fps=15) 
    anim.save(f, writer=writergif)
