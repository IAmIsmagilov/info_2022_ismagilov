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
BROWN = (101,56,24)
CHOCO = (60,19,33)
FPS = 30
screen = pygame.display.set_mode((794, 1123))
screen.fill(GRAY)

def Building():
    rect(screen, BROWN, (30, 250, 375, 550))
    polygon(screen, BLACK, ([0, 250], [435, 250], [385, 220], [50, 220]))
    rect(screen, WHITE, (55, 250, 45, 190))
    rect(screen, WHITE, (130, 250, 45, 200))
    rect(screen, WHITE, (225, 250, 45, 195))
    rect(screen, WHITE, (300, 250, 45, 190))
    rect(screen, CHOCO, (0, 450, 435, 70))
    
rect(screen, BLACK, (0, 450, 794, 1123 - 450))
Building()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
