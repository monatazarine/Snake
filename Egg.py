import pygame
import random



class Egg:
    def __init__(self):
        self.radius = 15 #dimension 
        self.x = 400
        self.y = 100
        self.color = (255, 230, 150) 
    def reset(self):
        self.x = random.randint(0, 39) * 20  # Random x position within the grid  so it doesn't sit between cells.
        self.y = random.randint(0, 29) * 20  
    def draw(self, surface):
             pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


