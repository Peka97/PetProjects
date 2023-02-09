import pygame


def mainloop():
	pygame.init()
	game_over = False
	FPS = 30


	clock = pygame.time.Clock()

	while not game_over:

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


		clock.tick(FPS)
		# pygame.time.delay()
