import pygame
from os import getcwd
import random

random.seed()


class Floor(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.image = pygame.image.load(getcwd() + '/graphics/Floor/white_grass' +
                                       str(int(random.random() * 11) + 1).rjust(2, '0') + ".png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.pos = pygame.math.Vector2(pos)
        self.rect = self.image.get_rect(center=(pos[0] + 50, pos[1] + 50))
