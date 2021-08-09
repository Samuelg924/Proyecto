import pygame
from sys import exit

class Scenario:
	def __init__(self, background = "", floor = "", wall = "", wall_door = ""):
		self.background = background
		self.floor = floor
		self.wall = wall
		self.wall_door = wall_door

	def draw_scenario0(self):
		screen.blit(self.background, (0, 0))

	def draw_scenario1(self):
		screen.blit(self.wall, (0, 0))

class Character:
	def __init__(self, character_surface):
		self.character = character_surface
		self.character_x_pos = 250
		self.character_y_pos = 767

	def draw_character(self):
		self.character_rect = self.character.get_rect(midbottom = (self.character_x_pos, self.character_y_pos))
		screen.blit(self.character, self.character_rect)

	def move_character(self, direction):
		if self.character_x_pos >= 0:
			if direction[0] == 1:
				self.character_x_pos += 2
				
			if direction[0] == -1:
				self.character_x_pos -= 2

			if direction[1] == 1:
				self.character_y_pos += 2
			
			if direction[1] == -1:
				self.character_y_pos -= 2
		else:
			self.character_x_pos += 0.1

class Button:
	def __init__(self, text, width, height, pos, elevation, surface1, surface2):

		# Core attributes

		pos[0], pos[1] = pos[0] - width / 2, pos[1] - height / 2
		pos = (pos[0], pos[1])
		self.surface1 = pygame.transform.scale(surface1, (width, height))
		self.surface2 = pygame.transform.scale(surface2, (width, height))
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
		self.font_color = (255, 255, 255)
		self.text = text

		# Top rectangle 

		self.top_rect = self.surface1.get_rect(topleft = pos)
		self.top_color = (0, 0, 0)

	def draw(self):

		# Text
		self.text_surf = gui_font.render(self.text,True, self.font_color)
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

		# Elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center

		screen.blit(self.surface1, self.top_rect)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			screen.blit(self.surface2, self.top_rect)
			self.font_color = (150, 150, 150)
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation + 0.5
				if self.pressed == True:
					print("Changed")
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.font_color = (255, 255, 255)

	def change_scenario(self):
		if self.pressed == True:
			return 1
		else:
			return 0

# Variables de juego

direction = [0, 0]
floor_cells = 10
character_move_status = False
scene_number = 0

# Configuracion de ventana

window_width, window_height = 1280, 720

# Main loop set

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Project 9")
clock = pygame.time.Clock()

# Blank surfaces

background = pygame.Surface((500, 500))
floor = pygame.Surface((500, 500))
wall = pygame.Surface((500, 500))
wall_door = pygame.Surface((500, 500))

# Carga de imagenes

background_ciudad_azul = pygame.transform.scale(pygame.image.load("proyecto-videojuego/resources/Background2.png").convert_alpha(), (window_width, window_height))
wall_brick_tile = pygame.image.load("proyecto-videojuego/resources/BRick_wall.png").convert_alpha()
marco_boton_blanco = pygame.image.load("proyecto-videojuego/resources/Marco_boton_blanco.png").convert_alpha()
marco_boton_gris = pygame.image.load("proyecto-videojuego/resources/Marco_boton_gris.png").convert_alpha()
character_surface = pygame.transform.scale2x(pygame.image.load("proyecto-videojuego/resources/Character-test.png").convert_alpha())

# Variables adicionales (Pygame)

gui_font = pygame.font.Font("proyecto-videojuego/resources/Burgundy.otf", 40)

# Classes

character = Character(character_surface)
button1 = Button('START', 300, 120, [window_width / 2, (window_height / 3) * 2], 5, marco_boton_blanco, marco_boton_gris)

# Main Loop

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d and character_move_status == True:
				direction[0] = 1	
			if event.key == pygame.K_a and character_move_status == True:
				direction[0] = -1	
			if event.key == pygame.K_w and character_move_status == True:
				direction[1] = -1
			if event.key == pygame.K_s and character_move_status == True:
				direction[1] = 1
			# if event.key == pygame.K_e and main.wall_interaction() == True and character_move_status == True:
			# 	character_move_status = False
			# 	scene_number = 2
			if event.key == pygame.K_RETURN and character_move_status == False:
				character_move_status = True
				scene_number = 1
			
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				direction[0] = 0
			if event.key == pygame.K_a:
				direction[0] = 0
			if event.key == pygame.K_s:
				direction[1] = 0
			if event.key == pygame.K_w:
				direction[1] = 0
	
	screen.fill((0, 0, 0))

	if scene_number == 0:
		background = background_ciudad_azul
		scenario = Scenario(background = background)
		scenario.draw_scenario0()
		button1.draw()
		scene_number = scene_number + button1.change_scenario()

	if scene_number == 1:
		wall = wall_brick_tile
		character_move_status = True
		scenario = Scenario(wall = wall)
		character.draw_character()
		character.move_character(direction)
		scenario.draw_scenario1()

	pygame.display.update()
	clock.tick(60)