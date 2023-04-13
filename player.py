import pygame
from os import getcwd

from support import *
from settings import CELL_SIZE


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, maze):
        super().__init__(group)
        # general setup
        self.maze = maze
        self.animations = None
        self.import_assets()
        self.status = 'idle_down'
        self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]
        self.pos = pygame.math.Vector2(pos)
        self.rect = self.image.get_rect(center=pos)

        # movement attributes
        self.direction = pygame.math.Vector2()

        self.speed = 200

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'go_up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'go_down'
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            if self.direction.y == 1:
                self.status = 'go_downright'
            elif self.direction.y == -1:
                self.status = 'go_upright'
            else:
                self.status = 'go_right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            if self.direction.y == 1:
                self.status = 'go_downleft'
            elif self.direction.y == -1:
                self.status = 'go_upleft'
            else:
                self.status = 'go_left'
        else:
            self.direction.x = 0

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = 'idle_' + self.status.split('_')[1]

    def move(self, dt):

        # normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)
        self.collision(dt)
        self.get_status()
        self.animate(dt)

    def collision(self, dt):
        cell_y = int(self.pos.y / CELL_SIZE)
        v = pygame.Vector2(0, 0)
        cell_x = 0
        if not self.maze[int((self.pos.x + 15) / CELL_SIZE)][cell_y]:
            cell_x = int((self.pos.x + 15) / CELL_SIZE)
        else:
            cell_x = int((self.pos.x - 15) / CELL_SIZE)
        if not self.maze[cell_x][int((self.pos.y + 15) / CELL_SIZE)]:
            cell_y = int((self.pos.y + 15) / CELL_SIZE)
        else:
            cell_y = int((self.pos.y - 15) / CELL_SIZE)
        if not self.maze[cell_x][cell_y]:
            if self.pos.x < float(cell_x * CELL_SIZE + CELL_SIZE / 2) \
                    and self.direction.x != 0:
                v.x = -self.speed * dt
            elif self.pos.x >= float(cell_x * CELL_SIZE + CELL_SIZE / 2) \
                    and self.direction.x != 0:
                v.x = self.speed * dt
            if self.pos.y <= float(cell_y * CELL_SIZE + CELL_SIZE / 2) \
                    and self.direction.y != 0:
                v.y -= self.speed * dt
            elif self.pos.y > float(cell_y * CELL_SIZE + CELL_SIZE / 2) \
                    and self.direction.y != 0:
                v.y += self.speed * dt
            if v.magnitude() != 0:
                v.normalize()
            self.pos.x += v.x
            self.pos.y += v.y
            self.rect.x += v.x
            self.rect.y += v.y

    def import_assets(self):
        self.animations = {'idle_up': [], 'idle_down': [], 'idle_downleft': [], 'idle_downright': [], 'idle_left': [],
                           'idle_right': [], 'idle_upleft': [], 'idle_upright': [], 'go_up': [], 'go_down': [],
                           'go_downleft': [], 'go_downright': [], 'go_left': [], 'go_right': [], 'go_upleft': [], 'go_upright': []}
        for animation in self.animations.keys():
            full_path = getcwd() + '/graphics/Player/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frame_index += dt * 6
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]
