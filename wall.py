import pygame
from os import getcwd


image = pygame.image.load(getcwd() + '/graphics/wall.png')


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.image = image
        self.pos = pygame.math.Vector2(pos)
        self.rect = self.image.get_rect(center=(pos[0] + 50, pos[1] + 50))
