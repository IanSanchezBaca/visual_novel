import pygame, sys, os

# os.environ['SDL_VIDEODRIVER'] = 'windlib'

# os.environ["DISPLAY"]
os.environ["SDL_VIDEODRIVER"] = "dummy"


# import the pygame module
# pygame.init()
# pygame.display.list_modes()
  
# Define the background colour
# using RGB color coding.
background_colour = (234, 212, 252)
  
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((300, 300))
  
# Set the caption of the screen
pygame.display.set_caption('Geeksforgeeks')
  
# Fill the background colour to the screen
screen.fill(background_colour)
  
# Update the display using flip
pygame.display.flip()
  
# Variable to keep our game loop running
running = True
  
# game loop
while running:
    
# for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False