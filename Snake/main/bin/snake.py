import pygame


class SnakeHeads(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		image = pygame.image.load('./content/head.png')
		image.set_colorkey((0, 0, 0))
		self.image = pygame.transform.scale(image, (25, 25)).convert()
		self.rect = self.image.get_rect(center=(250, 250))


class SnakeBodies(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		image = pygame.image.load('./content/body.png')
		image.set_colorkey((0, 0, 0))
		self.image = pygame.transform.scale(image, (25, 25)).convert()
		self.rect = self.image.get_rect(center=(250, 275))


class SnakeTails(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		image = pygame.image.load('./content/tail.png')
		image.set_colorkey((0, 0, 0))
		self.image = pygame.transform.scale(image, (25, 25)).convert()
		self.rect = self.image.get_rect(center=(250, 300))


class Snakes:
	def __init__(self):
		pass
