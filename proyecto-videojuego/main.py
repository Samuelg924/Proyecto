import pygame, time
from sys import exit

class Main:
	def __init__(self):
		self.escenario = Escenario()
		self.character = Character()

	def draw_elemets(self):
		self.escenario.draw_scenario()
		self.character.draw_character()
		self.globe_dialog = pygame.image.load("proyecto-videojuego/resources/globe_dialog.png").convert_alpha()

	def move(self, direction):
		self.escenario.move_scenario(direction)
		self.character.move_character(direction)

	def check_wall_collision(self):
		if self.character.character_rect.centery <= self.escenario.wall_rect.bottom:	
			return True
		return False

	def wall_interaction(self):
		if self.character.character_rect.colliderect(self.escenario.wall_door_rect):
			self.globe_dialog_rect = self.globe_dialog.get_rect(bottomleft = self.character.character_rect.topright)
			screen.blit(self.globe_dialog, self.globe_dialog_rect)

class Escenario:
	def __init__(self):
		self.city_ground = pygame.image.load("proyecto-videojuego/resources/City_ground2.png").convert_alpha()
		self.city_background = pygame.image.load("proyecto-videojuego/resources/Background2.png").convert_alpha()
		self.wooden_floor = pygame.image.load("proyecto-videojuego/resources/Wooden_floor.png").convert_alpha()
		self.brick_wall = pygame.image.load("proyecto-videojuego/resources/Brick_wall.png").convert_alpha()
		self.brick_wall_door = pygame.image.load("proyecto-videojuego/resources/Brick_wall_door.png").convert_alpha()
		self.floor_x_pos = 0
		self.background_x_pos = 0
		self.wall_list = []

	def draw_scenario(self):
		self.ground, self.background = self.actual_scenario()

		for row in range(floor_cells):
			for col in range(floor_cells- 2):
				self.floor_rect = self.wooden_floor.get_rect(topleft = (row * 150 + self.background_x_pos, col * 150))
				screen.blit(self.wooden_floor, self.floor_rect)
		
		for row in range(int(floor_cells / 2)):
			self.blank = 3
			if row != self.blank:
				self.wall_rect = self.brick_wall.get_rect(topleft = (row * 300 + self.background_x_pos, 0))
				screen.blit(self.brick_wall, self.wall_rect)
			else:
				self.wall_door_rect = self.brick_wall_door.get_rect(topleft = (self.blank * 300 + self.background_x_pos, 0))
				screen.blit(self.brick_wall_door, self.wall_door_rect)

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
floor_cells = 10

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Project 9")
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
	if main.check_wall_collision():
		direction[1] = 1
		main.character.character_y_pos += 3
		direction[1] = 0
	main.wall_interaction()

	pygame.display.update()
	clock.tick(60)