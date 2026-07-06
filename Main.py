
import pygame
import sys
from Egg import Egg
from Snake import Snake

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #creates the window

pygame.display.set_caption("Snake Game")  

WHITE = (255, 255, 255)
ST_BUTTON_COLOR = (105, 232, 130)
ST_BUTTON_HOVER_COLOR = (172, 250, 112)
EX_BUTTON_COLOR = (255, 0, 0)
EX_BUTTON_HOVER_COLOR = (144, 8, 26)
SCREEN_BG_COLOR = (41,47,86)

# Frame rate limiter (keeps CPU cool)
CLOCK = pygame.time.Clock()
my_egg = Egg()  
my_snake = Snake()         

#the Button (x, y, width, height)
ST_button = pygame.Rect(325, 260, 150, 50)
EX_button = pygame.Rect(325, 320, 150, 50)
#Button Text
ST_button_text = pygame.font.SysFont(None, 36).render("Start", True, WHITE)
text_rect = ST_button_text.get_rect(center=ST_button.center)

EX_button_text = pygame.font.SysFont(None, 36).render("Exit", True, WHITE)
EX_text_rect = EX_button_text.get_rect(center=EX_button.center)



playing = False
running = True

def game_loop():
    global playing, running      

       
    while  playing:
           CLOCK.tick(60)  #controls the speed # : run at a maximum of 60 frames per second.
           
           screen.fill((0, 0, 0))
           for event in pygame.event.get():
              if event.type == pygame.QUIT:
                 playing = False
                 running = False
              if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_UP:
                    my_snake.speed_x = 0
                    my_snake.speed_y = -1 # Move Up
                 elif event.key == pygame.K_DOWN:
                    my_snake.speed_x = 0
                    my_snake.speed_y = 1  # Move Down
                 elif event.key == pygame.K_LEFT:
                    my_snake.speed_x = -1 # Move Left
                    my_snake.speed_y = 0
                 elif event.key == pygame.K_RIGHT:
                    my_snake.speed_x = 1  # Move Right
                    my_snake.speed_y = 0
                    
           my_snake.move()         
           #check if the snake has hit the wall
           hit_wall = not (0 <= my_snake.x < SCREEN_WIDTH and 0 <= my_snake.y < SCREEN_HEIGHT)    
           if hit_wall:
                playing = False
                print("Game Over!")   
                  
           if playing:
             screen.fill((0, 0, 0))
             my_egg.draw(screen)  
             my_snake.draw(screen)
             pygame.display.update()   



#Loop: Without it, the Python script would execute
# flash a window, and instantly close. The loop keeps the program running.
while running:
    CLOCK.tick(60)  
    # current mouse position
    mouse_pos = pygame.mouse.get_pos()
    
    
    
  # Look for events $
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #  mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
              if ST_button.collidepoint(mouse_pos):
                 print("Start button clicked!")  
                 playing = True
                 game_loop()    
              if EX_button.collidepoint(mouse_pos):
                 print("Exit button clicked!")
                 running = False  
                 
    screen.fill(SCREEN_BG_COLOR)
    # Update the display to show changes
    if  ST_button.collidepoint(mouse_pos):   
      pygame.draw.rect(screen, ST_BUTTON_HOVER_COLOR, ST_button)  
    else: 
       pygame.draw.rect(screen, ST_BUTTON_COLOR, ST_button)
    if  EX_button.collidepoint(mouse_pos):   
      pygame.draw.rect(screen, EX_BUTTON_HOVER_COLOR, EX_button)  
    else: 
       pygame.draw.rect(screen, EX_BUTTON_COLOR, EX_button)   
     #  blit = draw the Text on top/onto of the button
    screen.blit(ST_button_text, text_rect)
    screen.blit(EX_button_text, EX_text_rect)
    pygame.display.flip()
 
pygame.quit()   
sys.exit()