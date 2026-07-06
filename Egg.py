import pygame
import sys
import random

pygame.init()


class Egg:
    def __init__(self):
        self.radius = 10 #dimension 
        self.reset() #calls the reset method to set the initial position of the egg
        self.color = (255, 230, 150) 
        
    def reset(self):
        self.x = random.randint(self.radius, 800 - self.radius)
        self.y = random.randint(self.radius, 600 - self.radius)

    def draw(self, surface):
             pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


