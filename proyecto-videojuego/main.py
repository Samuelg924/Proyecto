import pygame
from sys import exit

class Escenario:
	def __init__(self):
		self.ground = pygame.transform.scale2x(pygame.image.load("proyecto-videojuego/resources/grass_ground.png").convert_alpha())

	def draw_ground(self):
		screen.blit(self.ground, (0, 700))

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

floor_x_pos = 0

escenario = Escenario()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	escenario.draw_ground()

	pygame.display.update()
	clock.tick(60)