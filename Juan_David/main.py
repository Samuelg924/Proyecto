import pygame,os, time, random

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space invaders")

#load images
RED_SPACE_SHIP = pygame.image.load("Juan_David/assets/pixel_ship_red_small.png")
GREEN_SPACE_SHIP = pygame.image.load("Juan_David/assets/pixel_ship_green_small.png")
BLUE_SPACE_SHIP = pygame.image.load("Juan_David/assets/pixel_ship_blue_small.png")

# player ship
YELLOW_SPACE_SHIP = pygame.image.load("Juan_David/assets/pixel_ship_yellow.png")

# lasers
RED_LASERS = pygame.image.load("Juan_David/assets/pixel_laser_red.png")
GREEN_LASERS = pygame.image.load("Juan_David/assets/pixel_laser_green.png")
BLUE_LASERS = pygame.image.load("Juan_David/assets/pixel_laser_blue.png")
YELLOW_LASERS = pygame.image.load("Juan_David/assets/pixel_laser_yellow.png")

# background
BG = pygame.transform.scale(pygame.image.load("Juan_David/assets/background-black.png"), (WIDTH, HEIGHT))

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0,0))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
main()