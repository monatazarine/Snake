import pygame

class Snake:
    def __init__(self):
        # We start with a list of coordinates for the body parts.
        self.body = [[325, 260], [310, 260], [295, 260]]
        self.width = 25
        self.height = 25
        self.color = (144, 8, 26)
        # Speed directions (0 means stopped, 1 means positive direction, -1 negative)
        self.speed_x = 0
        self.speed_y = 0
        self.speed = 20  # Speed of the snake
    def move(self):
        #Calculate where the new head position will be
        head = self.body[0]
        new_head = [head[0] + self.speed_x * self.speed, head[1] + self.speed_y * self.speed]
        if new_head != head:  # Only add a new head if the snake is moving
            self.body.insert(0, new_head)  # Add the new head to the front of the body
            # Remove the tail
            self.body.pop()
    def grow(self):
             # Add a new segment to the snake's body at the position of the last segment
             tail = self.body[-1]
             self.body.append([tail[0], tail[1]])  # Append a copy of the last segment
                
    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, self.color, (segment[0], segment[1], self.width, self.height))    


