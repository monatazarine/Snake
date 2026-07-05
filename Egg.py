import pygame
import sys
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
pygame.display.set_caption("Testing the Egg Class")
class Egg:
    def __init__(self):
        self.radius = 10 #dimension 
        self.x = 400
        self.y = 100
        self.color = (255, 230, 150) 

my_egg = Egg()
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))        
    pygame.draw.circle(screen, my_egg.color, (my_egg.x, my_egg.y), my_egg.radius)
    pygame.display.update()

pygame.quit()
sys.exit()
