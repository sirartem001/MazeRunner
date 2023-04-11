import numpy as np
import random

from settings import *

random.seed()

def borders():
    grid = make_maze()
    for i in range(LAB_SIZE + 2):
        grid[i][0] = False
        grid[0][i] = False
        grid[i][LAB_SIZE + 1] = False
        grid[LAB_SIZE + 1][i] = False
    return grid


def make_maze(w2=LAB_SIZE - 1, h2=LAB_SIZE - 1, w1=1, h1=1, grid=np.full((LAB_SIZE + 2, LAB_SIZE + 2), True)):
    wh = bool(random.getrandbits(1))
    if wh and not(w2 - w1 <= 2):
        w = int(random.random() * (w2 - w1) / 2 * 2 + 1 + w1)
        for i in range(h1, h2 + 1):
            grid[i][w] = False
        he = int(random.random() * (h2 - h1) + h1)
        grid[he][w] = True
        grid = make_maze(w - OFFSETT, h2, w1, h1, grid)
        grid = make_maze(w2, h2, w + OFFSETT, h1, grid)
        return grid
    if h2 - h1 <= 2:
        return grid
    h = int(random.random() * (h2 - h1) / 2 * 2 + 1 + h1)
    for i in range(w1, w2 + 1):
        grid[h][i] = False
    we = int(random.random() * (w2 - w1) + w1)
    grid[h][we] = True
    grid = make_maze(w2, h2, w1, h + OFFSETT, grid)
    grid = make_maze(w2, h - OFFSETT, w1, h1, grid)
    return grid

