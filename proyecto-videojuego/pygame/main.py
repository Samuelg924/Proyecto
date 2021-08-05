import pygame
from sys import exit

class Main:
	def __init__(self):
		self.escenario = Escenario()
		self.character = Character()
		self.globe_dialog = pygame.image.load("proyecto-videojuego/resources/globe_dialog.png").convert_alpha()

	def draw_elements(self):
		if scene_number == 1:
			self.escenario.draw_scenario1()
		self.character.draw_character()

	def move(self, direction):
		self.escenario.move_scenario(direction)
		self.character.move_character(direction)

	def check_wall_collision(self):
		if self.character.character_rect.centery <= self.escenario.wall_rect.bottom:	
			return True
		return False

	def wall_interaction(self):
		if self.character.character_rect.colliderect(self.escenario.wall_door_rect1) or self.character.character_rect.colliderect(self.escenario.wall_door_rect2):
			self.globe_dialog_rect = self.globe_dialog.get_rect(bottomleft = self.character.character_rect.topright)
			screen.blit(self.globe_dialog, self.globe_dialog_rect)
			return True

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
		self.scene_number = scene_number

	def draw_scenario1(self):
		self.ground, self.background = self.actual_scenario()

		for row in range(floor_cells):
			for col in range(floor_cells- 2):
				self.floor_rect = self.wooden_floor.get_rect(topleft = (row * 150 + self.background_x_pos, col * 150))
				screen.blit(self.wooden_floor, self.floor_rect)
		
		for row in range(int(floor_cells / 2)):
			self.blank = 1
			self.blank2 = 3
			if row != self.blank and row != self.blank2:
				self.wall_rect = self.brick_wall.get_rect(topleft = (row * 300 + self.background_x_pos, 0))
				screen.blit(self.brick_wall, self.wall_rect)
			else:
				self.wall_door_rect1 = self.brick_wall_door.get_rect(topleft = (self.blank * 300 + self.background_x_pos, 0))
				self.wall_door_rect2 = self.brick_wall_door.get_rect(topleft = (self.blank2 * 300 + self.background_x_pos, 0))
				screen.blit(self.brick_wall_door, self.wall_door_rect1)
				screen.blit(self.brick_wall_door, self.wall_door_rect2)

	def actual_scenario(self):
		self.scenario_number = 1

		if self.scenario_number == 1:
			self.ground = self.city_ground
			self.background = self.city_background

			return self.ground, self.background

	def move_scenario(self, direction):
		if self.background_x_pos <= 0:
			if direction[0] == 1:
				self.floor_x_pos -= 0.9
				self.background_x_pos -= 0.4
			if direction[0] == -1:
				self.floor_x_pos += 0.9
				self.background_x_pos += 0.4
		else:
			self.background_x_pos -= 0.1

	def start_screen(self):
		self.background_camp = pygame.image.load("proyecto-videojuego/resources/Background3.jpg").convert_alpha()
		screen.blit(self.background_camp, (0, 0))

class Character:
	def __init__(self):
		self.character = pygame.transform.scale2x(pygame.image.load("proyecto-videojuego/resources/Character-test.png").convert_alpha())
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
	def __init__(self,text,width,height,pos,elevation):
		# Core attributes
		pos[0], pos[1] = pos[0] - width / 2, pos[1] - height / 2
		pos = (pos[0], pos[1])
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = (0, 0, 0)

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = (200, 200, 200)
		#text
		self.text_surf = gui_font.render(text,True, (255, 255, 255))
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = (90, 90, 90)
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					print("Changed")
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = (50, 50, 50)

# Variables de juego

direction = [0, 0]
floor_cells = 10
character_move_status = False
scene_number = 0

# Configuracion de ventana

window_width, window_height = 1280, 720

# Main loop

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Project 9")
clock = pygame.time.Clock()

# Variables adicionales (Pygame)

gui_font = pygame.font.Font(None,30)

# Classes

main = Main()
button1 = Button('PLAY', 300, 100, [window_width / 2, window_height / 2], 5)

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
			if event.key == pygame.K_e and main.wall_interaction() == True and character_move_status == True:
				character_move_status = False
				scene_number = 2
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
		main.escenario.start_screen()
		button1.draw()
		if button1.pressed == True:
			scene_number = 1
			character_move_status = True

	elif scene_number == 1:
		main.draw_elements()
		main.move(direction)

		if main.check_wall_collision():
			direction[1] = 1
			main.character.character_y_pos += 3
			direction[1] = 0

		main.wall_interaction()
	
	elif scene_number == 2:
		pass

	pygame.display.update()
	clock.tick(60)