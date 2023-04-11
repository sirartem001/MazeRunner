import pygame

import lab
import PygameLights
from support import *
from player import Player
from monstr import Monster
from wall import Wall
from settings import CELL_SIZE
from copy import copy


class Level:
    def __init__(self):
        self.maze = None
        self.player_sprites = None
        self.all_sprites = None
        self.monstr = None
        self.wall = []
        self.player = None

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # set up
        self.setup()

    def setup(self):
        # generating maze
        self.maze = lab.borders()

        # setting up camera and sprites
        self.all_sprites = CameraGroup()
        self.player = Player((150, 150), self.all_sprites, self.maze)
        self.all_sprites.set_focus(self.player)
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if not self.maze[i][j]:
                    self.wall.append(Wall((i * CELL_SIZE, j * CELL_SIZE), self.all_sprites))
                    self.all_sprites.sprites().append(self.wall[-1])
                    self.all_sprites.wall.append(self.wall[-1].rect)
        self.monstr = Monster((150, 150), self.all_sprites, self.maze, self.player)

    def run(self, dt):
        self.all_sprites.update(dt)
        self.display_surface.fill('black')
        self.all_sprites.custom_draw()


def by_y(sprite):
    return sprite.rect.y


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.wall = []
        self.focus = None
        self.display_surface = pygame.display.get_surface()
        # setting up light engine
        # self.Light = PygameLights.LIGHT(100, PygameLights.pixel_shader(100, (218, 122, 122), 100, 0))

    def set_focus(self, focus):
        self.focus = focus

    def custom_draw(self):
        sprites = self.sprites()
        surface_blit = self.display_surface.blit
        for spr in sorted(sprites, key=by_y):
            rect = copy(spr.rect)

            self.spritedict[spr] = surface_blit(spr.image, rect.move(540 - self.focus.pos.x, 360 - self.focus.pos.y))
            # self.display_surface.blit(sprite.image, sprite.rect)

        # light display
        # light_display = pygame.Surface((self.display_surface.get_size()))
        # light_display.blit(PygameLights.global_light(self.display_surface.get_size(), 0), (0, 0))
        # self.Light.main(self.wall)
