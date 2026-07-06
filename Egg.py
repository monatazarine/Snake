import pygame
import random

pygame.init()


class Egg:
    def __init__(self):
        self.radius = 10 #dimension 
        self.x = 400
        self.y = 100
        self.color = (255, 230, 150) 
    def reset(self):
        self.x = random.randint(0, 780)  
        self.y = random.randint(0, 580)    
    def draw(self, surface):
             pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


