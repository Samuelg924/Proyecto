import pygame
from sys import exit

class Scenario:
	def __init__(self, background = "", floor = "", wall = "", wall_door = ""):
		self.background = background
		self.floor = floor
		self.wall = wall
		self.wall_door = wall_door
		self.character_surface1 = character_surface3
		self.character_surface2 = pygame.transform.scale(character_surface2, (64, 295))
		self.background_character1 = character_background1
		self.background_character2 = character_background1

		self.character_rect1 = self.character_surface1.get_rect(center = (window_width / 3, window_height / 3))
		self.character_rect2 = self.character_surface2.get_rect(center = ((window_width / 3) * 2, window_height / 3))
		self.background_character_rect1 = self.background_character1.get_rect(center = (window_width / 3, window_height / 3))
		self.background_character_rect2 = self.background_character2.get_rect(center = ((window_width / 3) * 2, window_height / 3))

	def draw_scenario0(self):
		screen.blit(self.background, (0, 0))

	def draw_scenario1(self):
		if button_selection_character1.pressed:
			button_selection_character2.status = False

		if button_selection_character2.pressed:
			button_selection_character1.status = False

		if button_selection_character1.status:
			self.background_character1 = character_background2
			self.background_character2 = character_background1

		if button_selection_character2.status:
			self.background_character2 = character_background2
			self.background_character1 = character_background1

		screen.blit(self.background, (0, 0))
		screen.blit(self.background_character1, self.background_character_rect1)
		screen.blit(self.background_character2, self.background_character_rect2)
		screen.blit(self.character_surface1, self.character_rect1)
		screen.blit(self.character_surface2, self.character_rect2)
	
	def draw_scenario2(self):
		screen.blit(self.wall, (0, 0))

class Character:
	def __init__(self, character_surface_number):
		if character_surface_number == 1: self.character = character_image_list3[character_index]
		if character_surface_number == 2: self.character = character_image_list2[character_index]
		self.character_x_pos = 250
		self.character_y_pos = 600

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
		self.status = False

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
				self.status = True
			else:
				self.dynamic_elecation = self.elevation + 0.5
				if self.pressed == True:
					print(self.status)
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.font_color = (255, 255, 255)

	def change_scenario(self):
		if self.pressed == True:
			return 1
		else:
			return 0

# Funciones

def animate(direction, character_index, counter):
	if direction == [1, 0] or direction == [1, -1] or direction == [1, 1]:
		if character_index < 3:
			if not counter and character_index == 2:
				_character_index = character_index - 1
			else:
				_character_index = character_index + 1
				counter = True
		else:
			_character_index = character_index - 1
			counter = False
	
	elif direction == [-1, 0] or direction == [-1, -1] or direction == [-1, 1]:
		if character_index < 6:
			if not counter and character_index == 5:
				_character_index = character_index - 1
			else:
				_character_index = character_index + 1
				counter = True
		else:
			_character_index = character_index - 1
			counter = False
		
	elif direction == [0, 1]:
		if character_index < 9:
			if not counter and character_index == 8:
				_character_index = character_index - 1
			else:
				_character_index = character_index + 1
				counter = True
		else:
			_character_index = character_index - 1
			counter = False

	elif direction == [0, -1]:
		if character_index < 12:
			_character_index = character_index + 1
		else:
			_character_index = character_index - 1
			counter = False

	else:
		_character_index = 0
	return _character_index, counter

# Variables de juego

direction = [0, 0]
floor_cells = 10
character_move_status = False
scene_number = 0
character_index = 0
counter = True

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
background_flatlands = pygame.transform.scale(pygame.image.load("proyecto-videojuego/resources/Background3.jpg").convert_alpha(), (window_width, window_height))
wall_brick_tile = pygame.image.load("proyecto-videojuego/resources/BRick_wall.png").convert_alpha()
marco_boton_blanco = pygame.image.load("proyecto-videojuego/resources/Marco_boton_blanco.png").convert_alpha()
marco_boton_gris = pygame.image.load("proyecto-videojuego/resources/Marco_boton_gris.png").convert_alpha()
character_surface1 = pygame.image.load("proyecto-videojuego/resources/Character-test.png").convert_alpha()
character_surface2 = pygame.image.load("proyecto-videojuego/resources/Character-test2.png").convert_alpha()
character_surface3 = pygame.image.load("proyecto-videojuego/resources/Character-test3.png").convert_alpha()
character_background1 = pygame.image.load("proyecto-videojuego/resources/Character_background.png").convert_alpha()
character_background2 = pygame.image.load("proyecto-videojuego/resources/Character_background2.png").convert_alpha()

# Variables adicionales (Pygame)

gui_font = pygame.font.Font("proyecto-videojuego/resources/Burgundy.otf", 40)

# Variables de juego (Python)

character_image_list1 = [
	character_surface1,
	character_surface1,
	character_surface1,
	character_surface1,
	character_surface1,
	character_surface1
]

character_image_list2 = [
	character_surface2,
	character_surface2,
	character_surface2,
	character_surface2,
	character_surface2,
	character_surface2
]

character_image_list3 = [
	character_surface3,
	character_surface3,
	character_surface3,
	character_surface3,
	character_surface3,
	character_surface3
]


# USEREVENT

animation_tick = pygame.USEREVENT + 10
pygame.time.set_timer(animation_tick, 800)

# Botones

button_start = Button('START', 300, 120, [window_width / 2, (window_height / 3) * 2], 5, marco_boton_blanco, marco_boton_gris)
button_selection_character1 = Button('SELECT', 300, 120, [window_width / 3, (window_height / 4) * 3], 5, marco_boton_blanco, marco_boton_gris)
button_selection_character2 = Button('SELECT', 300, 120, [(window_width / 3) * 2, (window_height / 4) * 3], 5, marco_boton_blanco, marco_boton_gris)
button_selection_character_confirm = Button('Confirm', 230, 80, [window_width / 2, (window_height / 10) * 9.15], 5, marco_boton_blanco, marco_boton_gris)

# Classes

character = Character(character_surface1)

# Main Loop

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d and character_move_status == True:
				direction[0] = 1
				character_index = 1
			if event.key == pygame.K_a and character_move_status == True:
				direction[0] = -1
				character_index = 4
			if event.key == pygame.K_w and character_move_status == True:
				direction[1] = -1
				character_index = 10
			if event.key == pygame.K_s and character_move_status == True:
				direction[1] = 1
				character_index = 7
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

		if character_move_status:
			if event.type == animation_tick:
				character_index, counter = animate(direction, character_index, counter)
				print(character_index)

	screen.fill((0, 0, 0))

	if scene_number == 0:
		background = background_ciudad_azul
		scenario = Scenario(background = background)
		scenario.draw_scenario0()
		button_start.draw()
		scene_number = scene_number + button_start.change_scenario()

	elif scene_number == 1:
		background = background_flatlands
		scenario = Scenario(background = background)
		scenario.draw_scenario1()
		button_selection_character1.draw()
		button_selection_character2.draw()

		if button_selection_character1.status:
			character = Character(1)

		if button_selection_character2.status:
			character = Character(2)

		if button_selection_character1.status or button_selection_character2.status:
			button_selection_character_confirm.draw()
			if button_selection_character_confirm.status:
				scene_number = 2
	
	elif scene_number == 2:
		wall = wall_brick_tile
		character_move_status = True
		scenario = Scenario(wall = wall)
		character.draw_character()
		character.move_character(direction)
		scenario.draw_scenario2()

	pygame.display.update()
	clock.tick(60)