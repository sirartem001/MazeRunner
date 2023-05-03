import pygame
from os import getcwd
from character import Character

from support import *
from settings import CELL_SIZE


class Player(Character):
    anim_path = HERO_ANIMATION_PATH
