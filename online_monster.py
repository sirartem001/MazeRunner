import pygame
from os import getcwd
from character import Character

from support import *
from settings import CELL_SIZE


class Online_monster(Character):
    anim_path = CRAW_GOD_ANIMATION_PATH
