import pygame

blueship = pygame.image.load("assets/pixel_ship_blue.png")
blueship_rec = blueship.get_rect()
blueship_rec.topright=(350, 250)
blueship = pygame.transform.scale(blueship,(200,200))

redship = pygame.image.load("assets/pixel_ship_red.png")
redship_rec = redship.get_rect()
redship_rec.topright=(120, 250)
redship = pygame.transform.scale(redship,(200,200))

greenship = pygame.image.load("assets/pixel_ship_green.png")
greenship_rec = greenship.get_rect()
greenship_rec.topright=(620, 250)
greenship = pygame.transform.scale(greenship,(200,200))

yellowship = pygame.image.load("assets/pixel_ship_yellow.png")
yellowship_rec = yellowship.get_rect()
yellowship_rec.topright=(400, 488)
yellowship = pygame.transform.scale(yellowship,(200,200))
