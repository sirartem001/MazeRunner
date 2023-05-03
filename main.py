import pygame


import sys
from settings import *
from level import Level


class Game:
	def __init__(self):
		self.level = None
		pygame.init()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.menu_img = pygame.image.load('graphics/menu.png')
		self.menu_img = pygame.transform.scale(self.menu_img, self.screen.get_rect().size)
		pygame.display.set_caption('Labyrinth')
		self.clock = pygame.time.Clock()
		self.run_menu()

	def start_the_game(self):
		self.level = Level()
		self.run()

	def run_menu(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				rect = self.menu_img.get_rect(center=self.screen.get_rect().center)
				self.screen.blit(self.menu_img, rect)
				pygame.display.update()
				keys = pygame.key.get_pressed()
				if keys[pygame.K_ESCAPE]:
					pygame.quit()
					sys.exit()
				if keys[pygame.K_s]:
					self.start_the_game()

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
			else:
				pygame.quit()
				sys.exit()


if __name__ == '__main__':
	game = Game()
