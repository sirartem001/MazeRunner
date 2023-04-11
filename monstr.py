import numpy

from copy import copy
from os import getcwd

from support import *
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from settings import CELL_SIZE


class PathFinder:
    def __init__(self, grid):
        self.obstacles = Grid(matrix=numpy.transpose(grid).tolist())
        self.finder = AStarFinder(diagonal_movement=DiagonalMovement.always)

    def pathfind(self, xs, ys, xe, ye):
        self.obstacles.cleanup()
        start = self.obstacles.node(int(xs / CELL_SIZE), int(ys / CELL_SIZE))
        end = self.obstacles.node(int(xe / CELL_SIZE), int(ye / CELL_SIZE))
        path, _ = self.finder.find_path(start, end, self.obstacles)
        return path


class Monster(pygame.sprite.Sprite):
    def __init__(self, pos, group, grid, player):
        super().__init__(group)
        # general setup
        self.animations = None
        self.grid = grid
        self.import_assets()
        self.status = 'go_right'
        self.frame_index = 0
        self.pl = player
        self.image = self.animations[self.status][int(self.frame_index)]
        self.pos = pygame.math.Vector2(pos)
        self.rect = self.image.get_rect(center=(pos[0] - 16, pos[1] - 16))
        self.rect.move(self.pl.pos)
        self.direction = pygame.math.Vector2()
        self.speed = 150
        self.pf = PathFinder(self.grid)

    def move(self, dt):
        path = self.pf.pathfind(self.pos.x, self.pos.y, self.pl.pos.x, self.pl.pos.y)
        self.path = path
        if len(path) > 1:
            if path[0][0] - path[1][0] < 0:
                self.direction.x = 1
            if path[0][0] - path[1][0] > 0:
                self.direction.x = -1
            if path[0][0] - path[1][0] == 0:
                self.direction.x = 0
            if path[0][1] - path[1][1] < 0:
                self.direction.y = 1
            if path[0][1] - path[1][1] > 0:
                self.direction.y = -1
            if path[0][1] - path[1][1] == 0:
                self.direction.y = 0
        elif len(path) <= 1:
            self.direction.y = 0
            self.direction.x = 0
        if int(self.pos.x / CELL_SIZE) == int(self.pl.pos.x / CELL_SIZE) \
            and int(self.pos.y / CELL_SIZE) == int(self.pl.pos.y / CELL_SIZE):
            self.direction = self.pl.pos - self.pos
        # normalizing a vector

        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        if self.direction.x > 0:
            self.status = "go_right"
        else:
            self.status = "go_left"
        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.animate(dt)
        self.move(dt)

    def import_assets(self):
        self.animations = {'go_left': [], 'go_right': []}
        for animation in self.animations.keys():
            full_path = getcwd() + '/graphics/CrowGod/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frame_index += dt * 6
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]
