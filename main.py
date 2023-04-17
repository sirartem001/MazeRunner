import pygame
import pygame_menu


import sys
from settings import *
from pygame_menu import themes
from level import Level


class Game:
	def __init__(self):
		self.level = None
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption('Labyrinth')
		self.clock = pygame.time.Clock()
		mainmenu = pygame_menu.Menu('Welcome', 600, 400,
									theme=themes.THEME_SOLARIZED)
		mainmenu.add.button('Play', self.start_the_game)
		mainmenu.add.button('Quit', pygame_menu.events.EXIT)
		mainmenu.mainloop(self.screen)

	def start_the_game(self):
		self.level = Level()
		self.run()

	def run(self):
		while True:
			if self.level.state:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
				dt = self.clock.tick() / 1000
				self.level.run(dt)
				pygame.display.update()


if __name__ == '__main__':
	game = Game()
