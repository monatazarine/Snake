
import pygame
import sys

pygame.init()


WHITE = (255, 255, 255)
ST_BUTTON_COLOR = (105, 232, 130)
ST_BUTTON_HOVER_COLOR = (172, 250, 112)
EX_BUTTON_COLOR = (255, 0, 0)
EX_BUTTON_HOVER_COLOR = (144, 8, 26)
SCREEN_BG_COLOR = (41,47,86)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Frame rate limiter (keeps CPU cool)
CLOCK = pygame.time.Clock()


#the Button (x, y, width, height)
ST_button = pygame.Rect(325, 260, 150, 50)
EX_button = pygame.Rect(325, 320, 150, 50)
#Button Text
ST_button_text = pygame.font.SysFont(None, 36).render("Start", True, WHITE)
text_rect = ST_button_text.get_rect(center=ST_button.center)

EX_button_text = pygame.font.SysFont(None, 36).render("Exit", True, WHITE)
EX_text_rect = EX_button_text.get_rect(center=EX_button.center)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #creates the window

pygame.display.set_caption("Snake Game")  

playing = False
running = True

def game_loop():
    global playing, running      
    
       
    while  playing:
           CLOCK.tick(60)  #controls the speed # : run at a maximum of 60 frames per second.
           
           screen.fill((0, 0, 0))
           pygame.display.update()   
          
           
           pygame.display.update()
           
           for event in pygame.event.get():
            if event.type == pygame.QUIT:
             playing = False  
             running = False
             


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