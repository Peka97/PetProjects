import pygame

from .fields import GameFields
from .snake import SnakeHeads, SnakeBodies, SnakeTails
from .fruit import Fruits


class Game:
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((500, 600))
		self.icon = pygame.image.load('./content/icon.png')
		pygame.display.set_icon(self.icon)
		pygame.display.set_caption('Snake Game')

		self.game_over = False
		self.FPS = 30
		self.score_count = 0

		self.game_field = GameFields()
		self.objects = [SnakeHeads(), SnakeBodies(), SnakeTails(), Fruits()]

		self.clock = pygame.time.Clock()

	def blit_and_update(self):
		self.game_field.draw(self.screen)
		for obj in self.objects:
			self.screen.blit(obj.image, obj.rect)
		self.screen.blit(self.game_field.update_score(self.score_count)[0],
						 self.game_field.update_score(self.score_count)[1])
		pygame.display.update()
		self.clock.tick(self.FPS)

	def mainloop(self):

		while not self.game_over:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						pass
					elif event.key == pygame.K_s:
						pass
					elif event.key == pygame.K_a:
						pass
					elif event.key == pygame.K_d:
						pass
			self.blit_and_update()
# pygame.time.delay()
