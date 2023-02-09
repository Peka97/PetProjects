import pygame




class SnakeHeads(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('./content/head.png')
class SnakeBodies(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('./content/body.png')

class SnakeTails(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('./content/tail.png')


class Snakes:
	def __init__(self):
		pass