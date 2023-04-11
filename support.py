import pygame


def import_folder(path):
    surface_list = []
    for img in range(4):
        full_path = path + '/' + str(img) + '.png'
        image_serf = pygame.image.load(full_path).convert_alpha()
        surface_list.append(image_serf)
    return surface_list












