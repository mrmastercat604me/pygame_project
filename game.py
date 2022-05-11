import pygame
import random,math,sys
from classes import Meteor


def draw_text(text, font, color, surface, x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def game(surface,player,clock,background,background_rect):

    running = True

    meteors = []
    meteor = Meteor(1,(random.randint(0,800),random.randint(0,800)),surface)
    meteors.append(meteor)

    surface.fill((0,0,0))

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
                    meteor = Meteor(1,(random.randint(0,800),random.randint(0,800)),surface)
                    meteors.append(meteor)
        if player.status == "dead":
            running = False

        surface.blit(background,background_rect)

        font = pygame.font.SysFont(None, 40)
        draw_text((f"Lives: {player.lives}"),font,(255,0,0),surface,0,0)
        draw_text((f"Score: {player.score}"),font,(255,255,0),surface,690,0)

        #surface.blit(enemyimage,enemyimage_rect)
        player.run(events)
        for meteor in meteors:
            meteor.render()
            if player.laser is not None:
                if meteor.collision(player.laser.rect):
                    meteors.remove(meteor)
                    meteor = Meteor(1,(random.randint(0,800),random.randint(0,800)),surface)
                    meteors.append(meteor)
            if meteor.collision(player.rect):
                player.lives -= 1
                meteors.remove(meteor)
                meteor = Meteor(1,(random.randint(0,800),random.randint(0,800)),surface)
                meteors.append(meteor)
        

        pygame.display.update()
        clock.tick(60)