import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colors

def seeds(initial_board):
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
                next_board[x][y] = 0
            else:
                if counts == 2:
                    next_board[x][y] = 1
                    
    return(next_board)