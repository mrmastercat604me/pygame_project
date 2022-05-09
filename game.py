import pygame
import random,math,sys


def draw_text(text, font, color, surface, x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def game(surface,player,clock,background,background_rect):

    running = True
    enemyimage = pygame.image.load("assets/meteor1.png")
    enemyimage_rect= enemyimage.get_rect()
    enemyimage_rect.x = random.randint(20,780) 
    enemyimage_rect.y = random.randint(20,780)
    if enemyimage_rect.colliderect(player.rect):
        enemyimage_rect.x = random.randint(20,780) 
        enemyimage_rect.y = random.randint(20,780)
    

    laser = pygame.image.load(f'assets/pixel_laser_{player.color}.png')
    laser_rect = laser.get_rect()
    laser_rect.center = (-100,-100)
    laser_first = pygame.image.load(f'assets/pixel_laser_{player.color}.png')
    laser_first_rect = laser_first.get_rect()
    laser_first_rect.center = (-100,-100)

    surface.fill((0,0,0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        if player.status == "dead":
            running = False


        #if enemyimage_rect.colliderect(player.rect):
        #    lives -= 1
       #     enemyimage_rect.x = random.randint(20,780) 
        #    enemyimage_rect.y = random.randint(20,780)



        if laser_rect.colliderect(enemyimage_rect):
            enemyimage_rect.x = random.randint(20,780)
            enemyimage_rect.y = random.randint(20,780)



        surface.blit(background,background_rect)

        font = pygame.font.SysFont(None, 40)
        draw_text((f"Lives: {player.lives}"),font,(255,0,0),surface,0,0)
        draw_text((f"Score: {player.score}"),font,(255,255,0),surface,690,0)
        font = pygame.font.SysFont(None, 75)

        player.run()
        surface.blit(enemyimage,enemyimage_rect)

        surface.blit(laser,laser_rect)
        pygame.display.update()
        clock.tick(60)
