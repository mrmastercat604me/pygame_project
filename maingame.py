import pygame, sys, math, random
from classes import Player
from game import game
from options import options

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Blastroids Game')
screen = pygame.display.set_mode((800,800),0,32)

Backgroundimage = pygame.image.load("assets/background-black.png")
Backgroundimage_rec= Backgroundimage.get_rect()
Backgroundimage_rec.topleft=(0,0)
Backgroundimage = pygame.transform.scale(Backgroundimage,(800,800))


font = pygame.font.SysFont(None, 75)
color = "yellow"


def draw_text(text, font, color, surface, x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False
player = Player(color,(400,400),screen)
def main_menu():
    global color
    click = False
    while True:
        screen.fill((0,0,0))
        screen.blit(Backgroundimage,Backgroundimage_rec)
        draw_text('Blast Roids',font, (255, 255, 0), screen, 250, 100)
        #----------------------------------
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(190, 300, 400, 70)
        button_2 = pygame.Rect(190, 400, 400, 70)
        button_1.centerx = 400
        button_2.centerx = 400
        pygame.draw.rect(screen, (150, 150, 30), button_1)
        pygame.draw.rect(screen, (150, 150, 30), button_2)
        draw_text('Press To Start',font, (0, 0, 0), screen, 217, 310)
        draw_text('Options',font, (0, 0, 0), screen, 285, 410)
        if button_2.collidepoint((mx, my)):
            if click:
                #options(screen,Backgroundimage,Backgroundimage_rec,color)
                player.update(options(screen,Backgroundimage,Backgroundimage_rec))
                print(player.color)
        if button_1.collidepoint((mx, my)):
            if click:
                #player = Player(color,(400,400),screen)
                print(color)
                game(screen,player,mainClock,Backgroundimage,Backgroundimage_rec)
        click = False
        #----------------------------------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

main_menu()