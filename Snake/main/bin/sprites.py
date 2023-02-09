import pygame


class Grass(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		image = pygame.image.load('./content/grass.png').convert()
		image.set_colorkey((255, 255, 255))
		self.image = pygame.transform.scale(image, (50, 50))
		self.rect = self.image.get_rect(topleft=(x, y))


class GroundTop(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		image = pygame.image.load('./content/ground_top.png').convert()
		image.set_colorkey((255, 255, 255))
		self.image = pygame.transform.scale(image, (50, 50))
		self.rect = self.image.get_rect(topleft=(x, y))


class Ground(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		image = pygame.image.load('./content/ground.png').convert()
		image.set_colorkey((255, 255, 255))
		self.image = pygame.transform.scale(image, (50, 50))
		self.rect = self.image.get_rect(topleft=(x, y))
