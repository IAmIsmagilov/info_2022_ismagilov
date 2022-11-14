import pygame
from pygame.draw import *

pygame.init()
alpha=100
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (204, 204, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
BROWN = (104,29,29)
CHOCO = (60,19,33)
DARKDARKDARKGRAY = (32,32,32)
DARKDARKGRAY = (49,49,49)
DARKBROWN = (102, 0, 0)
LIGHTPINK = (192, 192, 192)
DARKGRAY = (96,96,96)
LIGHTDARKGRAY = (64,64,64)
GRAY2 = (119,81,81)
GHOST=(198,183,183)
FPS = 30
screen = pygame.display.set_mode((794, 1123))
screen.fill(GRAY)
size=(500,500)
blue_image = pygame.Surface(size, pygame.SRCALPHA)

def Building(k,x,y):
    rect(screen, BROWN, (30*k+x, 250*k+y,375*k, 550*k))
    polygon(screen, BLACK, ([0+x, 250*k+y], [435*k+x, 250*k+y], [385*k+x, 220*k+y], [50*k+x, 220*k+y]))
    rect(screen, GRAY2, (55*k+x, 250*k+y, 45*k, 190*k))
    rect(screen, GRAY2, (130*k+x, 250*k+y, 45*k, 200*k))
    rect(screen, GRAY2, (225*k+x, 250*k+y, 45*k, 195*k))
    rect(screen, GRAY2, (300*k+x, 250*k+y, 45*k, 190*k))
    rect(screen, CHOCO, (0*k+x, 450*k+y, 435*k, 70*k))
    rect(screen, CHOCO, (15*k+x,380*k+y,405*k,25*k))
    rect(screen, CHOCO, (5*k+x,405*k+y,10*k,70*k))
    rect(screen, CHOCO, (420*k+x,405*k+y,10*k,70*k))
    rect(screen, CHOCO, (50*k+x, 405*k+y,15*k,70*k))
    rect(screen, CHOCO, (120*k+x,405*k+y,15*k,70*k))
    rect(screen, CHOCO, (190*k+x,405*k+y,15*k,70*k))
    rect(screen, CHOCO, (260*k+x,405*k+y,15*k,70*k))
    rect(screen, CHOCO, (330*k+x,405*k+y,15*k,70*k))
    rect(screen, CHOCO, (380*k+x,405*k+y,15*k,70*k))
    rect(screen, DARKBROWN, (65*k+x,650*k+y,70*k,90*k))
    rect(screen, DARKBROWN, (175*k+x,650*k+y,70*k,90*k))
    rect(screen, YELLOW, (285*k+x,650*k+y,70*k,90*k))
    rect(screen, CHOCO,  (100*k+x, 150*k+y, 20*k, 70*k))
    rect(screen, CHOCO, (350*k+x,150*k+y,10*k,70*k))
    rect(screen, CHOCO, (70*k+x,160*k+y,7*k,70*k))
    rect(screen, CHOCO, (250*k+x,160*k+y,7*k,70*k))
    
def Ghost(k,x,y):
    circle(screen, GHOST, (640*k+x,720*k+y), 35*k)
    circle(screen, GHOST, (610*k+x,720*k+y), 35*k)
    circle(screen, GHOST, (650*k+x,760*k+y), 35*k)
    circle(screen, GHOST, (610*k+x,760*k+y), 35*k)
    circle(screen, GHOST, (605*k+x,770*k+y), 35*k)
    circle(screen, GHOST, (605*k+x,740*k+y), 35*k)
    circle(screen, GHOST, (635*k+x,770*k+y), 35*k)
    circle(screen, GHOST, (605*k+x,770*k+y), 35*k)
    circle(screen, GHOST, (600*k+x,750*k+y), 35*k)
    circle(screen, GHOST, (600*k+x,790*k+y), 35*k)
    circle(screen, GHOST, (590*k+x,780*k+y), 35*k)
    circle(screen, GHOST, (580*k+x,790*k+y), 35*k)
    circle(screen, GHOST, (635*k+x,790*k+y), 35*k)
    circle(screen, GHOST, (655*k+x,790*k+y), 35*k)
    circle(screen, GHOST, (630*k+x,670*k+y), 35*k)
    circle(screen, LIGHT_BLUE, (615*k+x,680*k+y), 8*k)
    circle(screen, LIGHT_BLUE, (645*k+x,680*k+y), 8*k)
    circle(screen, BLACK, (642*k+x,678*k+y), 3*k)
    circle(screen, BLACK, (612*k+x,678*k+y), 3*k)
    ellipse(screen, WHITE, (612*k+x,677*k+y,7*k,4*k))
    ellipse(screen, WHITE, (642*k+x,677*k+y,7*k,4*k))
    
rect(screen, BLACK,(0, 450, 794, 1123 - 450))
ellipse(screen, DARKGRAY, (0, 600, 400, 70))


#Building 1
k=0.5
Building(k,0,420)

#Building 2
alpha=100
Building(k,265,300)
ellipse(screen, (30,30,30), (400, 300, 300, 70))
#Building 3
alpha
Building(k,530,170)

ellipse(screen, DARKGRAY, (200, 400, 600, 60)) 
ellipse(screen, DARKGRAY, (300, 500, 400, 70))
#Ghost1
Ghost(k+0.2,170,350)

#Ghost2
Ghost(k,250,450)

#GHOST3
Ghost(k,350,350)

#Ghost4
Ghost(k-0.1,450,450)

#Ghost5
Ghost(k,-80,480)

#Ghost6
Ghost(k,-50,520)

circle(screen, YELLOW, (700,190), 50)
ellipse(screen, (78,78,78), (100, 200, 500, 70))
ellipse(screen, DARKGRAY, (400, 150, 300, 70))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            
pygame.quit()
