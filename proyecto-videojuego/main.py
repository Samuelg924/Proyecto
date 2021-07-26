import pygame
from sys import exit

class Main:
	def __init__(self):
		self.escenario = Escenario()
		self.character = Character()

	def draw_elemets(self):
		self.escenario.draw_scenario()
		self.character.draw_character()

	def update(self):
		self.escenario.move_scenario()

class Escenario:
	def __init__(self):
		self.city_ground = pygame.image.load("proyecto-videojuego/resources/City_ground2.png").convert_alpha()
		self.city_background = pygame.image.load("proyecto-videojuego/resources/Background2.png").convert_alpha()
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

	def move_scenario(self, status, direction):
		if status == True:
			if direction == 1:
				self.floor_x_pos -= 0.9
				self.background_x_pos -= 0.4
			if direction == -1:
				self.floor_x_pos += 0.9
				self.background_x_pos += 0.4

class Character:
	def __init__(self):
		self.character = pygame.image.load("proyecto-videojuego/resources/Character-test.png").convert_alpha()
		self.character_x_pos = 250
		# self.character_rect = self.character.get_rect(midbottom = (self.character_x_pos, 767))

	def draw_character(self):
		screen.blit(self.character, (self.character_x_pos, 707))

	def move_character(self, status, direction):
		if status == True:
			if direction == 1:
				self.character_x_pos += 1
			
			if direction == -1:
				self.character_x_pos -= 1

scenario_status = False
scenario_direction = 0

charater_status = False
character_direction = 0

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
				scenario_status, scenario_direction = True, 1
				charater_status, charater_direction = True, 1
			if event.key == pygame.K_a:
				scenario_status, scenario_direction = True, -1
				charater_status, charater_direction = True, -1
			
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				scenario_status, scenario_direction = False, 0
				charater_status, charater_direction = False, 0
			if event.key == pygame.K_a:
				scenario_status, scenario_direction = False, 0
				charater_status, charater_direction = False, 0
	
	main.draw_elemets()
	main.escenario.move_scenario(scenario_status, scenario_direction)
	main.character.move_character(charater_status, character_direction)

	pygame.display.update()
	clock.tick(60)