import pygame
from pygame.draw import *

pygame.init()
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill(WHITE)
circle(screen, YELLOW, (200, 200), 200)
circle(screen, GRAY, (200,200),200, 3)
rect(screen, BLACK, (100,300,200,50))
circle(screen, RED, (100,150), 50)
circle(screen, BLACK, (100,150), 20)
circle(screen, RED, (300,150), 40)
circle(screen, BLACK, (300,150), 15)
line(screen, BLACK, 
                 [10, 47], 
                 [175, 117], 25)
circle(screen, BLACK, (100,150), 50, 1)
circle(screen, BLACK, (300,150), 40, 1)
line(screen, BLACK, 
                 [370, 60], 
                 [225, 130], 25)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
