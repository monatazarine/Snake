
import pygame
pygame.init()

WHITE = (255, 255, 255)
BUTTON_COLOR = (105, 232, 130)
BUTTON_HOVER_COLOR = (172, 250, 112)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#the Button (x, y, width, height)
button = pygame.Rect(325, 260, 150, 50)
#Button Text
button_text = pygame.font.SysFont(None, 36).render("Start", True, WHITE)
text_rect = button_text.get_rect(center=button.center)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #creates the window

pygame.display.set_caption("My First Pygame Window")
running = True
#Loop: Without it, the Python script would execute
# flash a window, and instantly close. The loop keeps the program running.
while running:
    
    # current mouse position
    mouse_pos = pygame.mouse.get_pos()
    
    
    
# Look for events $
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #  mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
              if button.collidepoint(mouse_pos):
                 print("Button clicked!")    
                 
    screen.fill((50, 50, 50))
    # Update the display to show changes
    if  button.collidepoint(mouse_pos):   
      pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button)  
    else: 
       pygame.draw.rect(screen, BUTTON_COLOR, button)
     #  blit = draw the Text on top/onto of the button
    screen.blit(button_text, text_rect)
    pygame.display.flip()
 
pygame.quit()   