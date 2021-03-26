# Import modules
import pygame
from pygame.locals import *


salutation = "Hello World !"

# Initialize
pygame.init ()
size = (256, 128)
window = pygame.display.set_mode ( size )

hellofont = pygame.font.SysFont ( 'courier', 16, True, True )
hellosurf = hellofont.render ( salutation, 1, Color("white") )
hellorect = window.blit ( hellosurf, (16, 16) )
pygame.display.update ( hellorect )

# Loop
loop = True
while loop is True:

    for evnt in pygame.event.get ():

        if evnt.type is QUIT:
            loop = False

        if evnt.type is KEYDOWN:

            if evnt.key == K_ESCAPE:
                loop = False

            if evnt.key == K_RETURN:
                window.fill ( Color("black"), hellorect )
                pygame.display.update ( hellorect )

    pygame.time.wait(250) # waiting 250 milliseconds makes it not too hasty


# Quit
pygame.quit ()