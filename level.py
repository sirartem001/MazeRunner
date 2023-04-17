import pygame

import lab
import PygameLights
from support import *
from player import Player
from monstr import Monster
from wall import Wall
from exit import Exit
from floor import Floor
from settings import *
from copy import copy


class Level:
    def __init__(self):
        self.maze = None
        self.player_sprites = None
        self.all_sprites = None
        self.monstr = None
        self.crow = False
        self.wall = []
        self.player = None
        self.state = True
        self.exit = None
        self.chace = False
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
                else:
                    self.all_sprites.sprites().append((Floor((i * CELL_SIZE, j * CELL_SIZE), self.all_sprites)))
        self.monstr = Monster((150, 150), self.all_sprites, self.maze, self.player)
        self.exit = Exit(self.maze, self.all_sprites)

    def check_death(self):
        if self.player.pos.x - self.monstr.pos.x < MIN_LEN \
                and self.player.pos.y - self.monstr.pos.y < MIN_LEN:
            self.state = 3

    def check_win(self):
        if abs(self.player.pos.x - self.exit.pos.x) < 25 \
                and abs(self.player.pos.y - self.exit.pos.y) < 25:
            self.state = False




    def run(self, dt):
        self.all_sprites.update(dt)
        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.chace)
        # self.check_death()
        self.check_win()


def by_y(sprite):
    if type(sprite).__name__ != "Floor":
        return sprite.rect.y
    return 0


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.wall = []
        self.focus = None
        self.display_surface = pygame.display.get_surface()
        # setting up light engine
        self.LightGreen = PygameLights.LIGHT(1000, PygameLights.pixel_shader(1000, (130, 255, 255), 1, False))
        self.LightRed = PygameLights.LIGHT(1000, PygameLights.pixel_shader(1000, (255, 100, 100), 1, False))

    def set_focus(self, focus):
        self.focus = focus

    def custom_draw(self, chace):
        sprites = self.sprites()
        surface_blit = self.display_surface.blit
        wall = []
        for spr in sorted(sprites, key=by_y):
            rect = copy(spr.rect)
            if type(spr).__name__ == "Wall":
                wall.append(rect.move(540 - self.focus.pos.x, 360 - self.focus.pos.y))
            self.spritedict[spr] = surface_blit(spr.image, rect.move(540 - self.focus.pos.x, 360 - self.focus.pos.y))
            # self.display_surface.blit(sprite.image, sprite.rect)

        # light display
        light_display = pygame.Surface((self.display_surface.get_size()))
        light_display.blit(PygameLights.global_light(self.display_surface.get_size(), 0), (0, 0))
        if not chace:
            self.LightGreen.main(wall, light_display, 540, 360)
        else:
            self.LightRed.main(wall, light_display, 540, 360)
        self.display_surface.blit(light_display, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
