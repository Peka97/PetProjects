import pygame


class Fruits(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		image = pygame.image.load('./content/fruit.png')
		image.set_colorkey((0, 0, 0))
		self.image = pygame.transform.scale(image, (25, 25)).convert()
		self.rect = self.image.get_rect(center=(25, 25))
