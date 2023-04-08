import pygame
from os import getcwd


def import_folder(path):
    surface_list = []
    for img in range(4):
        full_path = path + '/' + str(img) + '.png'
        image_serf = pygame.image.load(full_path).convert_alpha()
        surface_list.append(image_serf)
    return surface_list


image = pygame.image.load(getcwd() + '/graphics/wall.png')


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.image = image
        self.pos = pygame.math.Vector2(pos)
        self.rect = self.image.get_rect(center=(pos[0] + 50, pos[1] + 50))






