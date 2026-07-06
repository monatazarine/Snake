import pygame
import sys

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
 
screen.fill((0, 0, 0))

game_font = pygame.font.SysFont("Arial", 26, bold=True)
score_value = 0
WHITE = (255,255,255)
running = True
clock = pygame.time.Clock()

while running     :
             clock.tick(10)
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                         running = False
             keys = pygame.key.get_pressed()
             if keys[pygame.K_SPACE]:
                 score_value += 1
             screen.fill((0,0,0)   )   
             score_text = game_font.render(f"Score: {score_value}", True, WHITE)  
             screen.blit(score_text, (20, 20)) 
             pygame.display.update()
                 



pygame.quit()   
sys.exit()
