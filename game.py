import pygame
import random,math,sys
from classes import Meteor, Laser


def draw_text(text, font, color, surface, x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def game(surface,player,clock,background,background_rect):

    running = True

    meteors = []
    meteor = Meteor(0,(random.randint(0,800),random.randint(0,800)),surface)
<<<<<<< HEAD
=======
    meteor.collision_spawn(player.rect)
>>>>>>> fe2f92494a1828efa9235017a319d4b5db556e40
    meteors.append(meteor)
    
    lasers = []

    surface.fill((0,0,0))
    meteor = Meteor(0,(random.randint(0,800),random.randint(0,800)),surface)
    meteor.collision_spawn(player.rect)
    meteors.append(meteor)
    meteor = Meteor(0,(random.randint(0,800),random.randint(0,800)),surface)
    meteor.collision_spawn(player.rect)
    meteors.append(meteor)
    meteor = Meteor(0,(random.randint(0,800),random.randint(0,800)),surface)
    meteor.collision_spawn(player.rect)
    meteors.append(meteor)
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_m:
                    meteor = Meteor(0,(random.randint(0,800),random.randint(0,800)),surface)
                    meteor.collision_spawn(player.rect)
                    meteors.append(meteor)
        if player.status == "dead":
            running = False

        surface.blit(background,background_rect)

        font = pygame.font.SysFont(None, 40)
        draw_text((f"Lives: {player.lives}"),font,(255,0,0),surface,0,0)
        draw_text((f"Score: {player.score}"),font,(255,255,0),surface,690,0)

        player.run(events,lasers)

        for laser in lasers[:]:
            laser.update()
            if not surface.get_rect().collidepoint(laser.pos):
                lasers.remove(laser)
        for meteor in meteors[:]:
            meteor.update()
            if not surface.get_rect().collidepoint(meteor.pos):
                meteors.remove(meteor)
                meteor = Meteor(0,(random.randint(0,800),random.randint(0,800)),surface)
                meteor.collision_spawn(player.rect)
                meteors.append(meteor)
        for laser in lasers:
            laser.draw(surface)
        for meteor in meteors:
            meteor.draw(surface)
            if meteor.collision(player.rect):
                player.lives -= 1
                meteors.remove(meteor)
                meteor = Meteor(0,(random.randint(0,800),random.randint(0,800)),surface)
                meteor.collision_spawn(player.rect)
                meteors.append(meteor)
            for laser in lasers:
                if meteor.collision(laser.rect):
                    meteors.remove(meteor)
                    lasers.remove(laser)
                    meteor = Meteor(0,(random.randint(0,800),random.randint(0,800)),surface)
                    meteor.collision_spawn(player.rect)
                    meteors.append(meteor)
        

        pygame.display.update()
        clock.tick(60)
