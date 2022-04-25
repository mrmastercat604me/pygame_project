import pygame

pygame.init()

#-----------------
# Changeable Variables
#-----------------
scrn_width = 900
scrn_height = 900
bckgrnd_color = (0,0,0)
#--------------------------

#--------------------------
# DO NOT CHANGE variables
#-------------------------
clock = pygame.time.Clock()
#-----------------------------

#---------
# Screen
#---------
screen = pygame.display.set_mode((scrn_width,scrn_height))
pygame.display.set_caption("Blastroids Pygame")
screen.fill(bckgrnd_color)
#-----------------------

#-------------
# game loop
#------------
running = True
while running:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        # if X is pressed, close
        if event.type == pygame.QUIT:
            running = False

        # if esc key pressed, close
        if keys[pygame.K_ESCAPE]:
            screen.fill((0,0,0))
            running = False

        
#----------------
pygame.QUIT

#------------------------
# CODE TO BE RAN WHEN PYGAME WINDOW CLOSED
#-----------------------------