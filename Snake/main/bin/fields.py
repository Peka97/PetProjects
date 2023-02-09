import pygame

from .sprites import Grass, GroundTop, Ground


class GameFields(pygame.sprite.Group):
	def __init__(self):
		super().__init__()

		for x in range(0, 501, 50):
			for y in range(0, 451, 50):
				self.add(Grass(x, y))

		for x in range(0, 501, 50):
			self.add(GroundTop(x, 500))
			self.add(Ground(x, 550))

		self.filled_font = pygame.font.Font('./content/font_filled.ttf', 25)

	def update_score(self, score_count):
		score_surf = self.filled_font.render(f'Score {score_count}', True, (255, 255, 255))
		score_rect = score_surf.get_rect(topleft=(30, 535))
		return score_surf, score_rect
