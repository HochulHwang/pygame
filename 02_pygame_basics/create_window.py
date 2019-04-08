### create window with a exit button and set the caption(title bar) as Hello World!
import pygame, sys
from pygame.locals import *

pygame.init() # needed to call pygame function <- 'pygame.error: font not initialized'
DISPLAYSURF = pygame.display.set_mode((700,700)) # width and height of window (400px*300px) - input is () not int
pygame.display.set_caption('Hochul\'s window')

# main game loop
#     1. event handling
#     2. game state update
#     3. visualize game state on screen
while True:
    for event in pygame.event.get(): # returns lists of pygame.event.Event object in order (mouse click, keyboard, etc)
        if event.type == QUIT: # event.type-member variable, QUIT-pygame.locals.QUIT
            pygame.quit()
            sys.exit() # exits program, pygame.quit() should be called previously
        pygame.display.update()
