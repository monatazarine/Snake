import pygame
import sys
pygame.init()


class Egg:
    def __init__(self):
        self.radius = 10 #dimension 
        self.x = 400
        self.y = 100
        self.color = (255, 230, 150) 
    def draw(self, surface):
             pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


