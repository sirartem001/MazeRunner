import pygame
import random

from support import *
from settings import CELL_SIZE, LAB_SIZE

random.seed()


class Exit(pygame.sprite.Sprite):
    def __init__(self, grid, group):
        super().__init__(group)
        x = None
        y = None
        while True:
            x = int(random.random() * LAB_SIZE)
            y = int(random.random() * LAB_SIZE)
            if grid[x][y]:
                break
        self.pos = pygame.math.Vector2(x * CELL_SIZE, y * CELL_SIZE)
        self.image = pygame.image.load("graphics/exit.png")
        self.rect = self.image.get_rect(center=(self.pos.x - 50, self.pos.y - 50))

