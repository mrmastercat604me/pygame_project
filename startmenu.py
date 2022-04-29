import pygame, sys

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((800,800),0,32)

font = pygame.font.SysFont(None, 75)

def draw_text(text, font, color, surface, x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)\

def rgbcoolkidsclub():
    running = True
    while running:
        draw_text('Blast Roids',font, (255, 255, 0), screen, 265, 100)
        #Delete
        #draw_text('Blast Roids',font, (0, 255, 255), screen, 265, 100)


click = False

def main_menu():
    while True:
        screen.fill((0,0,0))
        draw_text('Blast Roids',font, (255, 255, 0), screen, 250, 100)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(190, 300, 400, 70)
        button_2 = pygame.Rect(190, 400, 400, 70)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (150, 150, 30), button_1)
        pygame.draw.rect(screen, (150, 150, 30), button_2)
        click = False
        draw_text('Press To Start',font, (0, 0, 0), screen, 217, 310)
        draw_text('Options',font, (0, 0, 0), screen, 285, 410)
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

def game():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('game',font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('options',font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

main_menu()