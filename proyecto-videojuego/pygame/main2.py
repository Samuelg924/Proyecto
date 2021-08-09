import pygame
from sys import exit

class Main:
	def __init__(self):
		# self.scenario = Scenario()
		pass

	def draw_elements(self):
		# self.scenario.draw_elements()
		pass

class Scenario:
	def __init__(self, _background):
		self.background = _background
		self.floor = floor
		self.wall = wall
		self.wall_door = wall_door

	def draw_elements(self):
		screen.blit(self.background, (0, 0))

class Button:
	def __init__(self,text,width,height,pos,elevation):

		# Core attributes

		pos[0], pos[1] = pos[0] - width / 2, pos[1] - height / 2
		pos = (pos[0], pos[1])
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		# Top rectangle 

		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = (0, 0, 0)

		# Bottom rectangle 

		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = (200, 200, 200)

		# Text
		self.text_surf = gui_font.render(text,True, (255, 255, 255))
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self):

		# Elevation logic 
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

# Variables adicionales (Pygame)

gui_font = pygame.font.Font(None,30)

# Classes

main = Main()
button1 = Button('PLAY', 300, 100, [window_width / 2, window_height / 2], 5)

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
	
	screen.fill((255, 255, 255))

	if scene_number == 0:
		background = background_ciudad_azul
		scenario = Scenario(background)
		scenario.draw_elements()

	pygame.display.update()
	clock.tick(60)