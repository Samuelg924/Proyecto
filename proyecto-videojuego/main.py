import pygame
from sys import exit

class Main:
	def __init__(self):
		self.escenario = Escenario()
		self.character = Character()

	def draw_elemets(self):
		self.escenario.draw_scenario()
		self.character.draw_character()
		self.escenario.draw_floor()

	def move(self, direction):
		self.escenario.move_scenario(direction)
		self.character.move_character(direction)

	def check_wall_collision(self):
		pass

class Escenario:
	def __init__(self):
		self.city_ground = pygame.image.load("proyecto-videojuego/resources/City_ground2.png").convert_alpha()
		self.city_background = pygame.image.load("proyecto-videojuego/resources/Background2.png").convert_alpha()
		self.wooden_floor = pygame.image.load("proyecto-videojuego/resources/Wooden_floor.png").convert_alpha()
		self.floor_x_pos = 0
		self.background_x_pos = 0

	def draw_scenario(self):
		self.ground, self.background = self.actual_scenario()

		screen.blit(self.background, (self.background_x_pos, 0))
		screen.blit(self.background, (self.background_x_pos - 1920, 0))

		screen.blit(self.ground, (self.floor_x_pos, 767))
		screen.blit(self.ground, (self.floor_x_pos + 710, 767))
		screen.blit(self.ground, (self.floor_x_pos - 710, 767))

	def actual_scenario(self):
		self.scenario_number = 1

		if self.scenario_number == 1:
			self.ground = self.city_ground
			self.background = self.city_background

			return self.ground, self.background

	def move_scenario(self, direction):
		if direction[0] == 1:
			self.floor_x_pos -= 0.9
			self.background_x_pos -= 0.4
		if direction[0] == -1:
			self.floor_x_pos += 0.9
			self.background_x_pos += 0.4

	def draw_floor(self):
		for row in range(floor_cells):
			self.floor_rect = self.wooden_floor.get_rect(topleft = (row * 300, 0))
			screen.blit(self.wooden_floor, self.floor_rect)

class Character:
	def __init__(self):
		self.character = pygame.transform.scale2x(pygame.image.load("proyecto-videojuego/resources/Character-test.png").convert_alpha())
		self.character_x_pos = 250
		self.character_y_pos = 767

	def draw_character(self):
		self.character_rect = self.character.get_rect(midbottom = (self.character_x_pos, self.character_y_pos))
		screen.blit(self.character, self.character_rect)

	def move_character(self, direction):
		if direction[0] == 1:
			self.character_x_pos += 2
			
		if direction[0] == -1:
			self.character_x_pos -= 2

		if direction[1] == 1:
			self.character_y_pos += 2
		
		if direction[1] == -1:
			self.character_y_pos -= 2

direction = [0, 0]
floor_cells = 5

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

main = Main()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				direction[0] = 1	
			if event.key == pygame.K_a:
				direction[0] = -1	
			if event.key == pygame.K_w:
				direction[1] = -1
			if event.key == pygame.K_s:
				direction[1] = 1
			
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				direction[0] = 0
			if event.key == pygame.K_a:
				direction[0] = 0
			if event.key == pygame.K_s:
				direction[1] = 0
			if event.key == pygame.K_w:
				direction[1] = 0
	
	main.draw_elemets()
	main.move(direction)

	pygame.display.update()
	clock.tick(60)