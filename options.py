import pygame, sys, math, random

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Blastroids Game')
screen = pygame.display.set_mode((800,800),0,32)

Backgroundimage = pygame.image.load("background-black.png")
Backgroundimage_rec= Backgroundimage.get_rect()
Backgroundimage_rec.topleft=(0,0)
Backgroundimage = pygame.transform.scale(Backgroundimage,(800,800))

blueship = pygame.image.load("pixel_ship_blue_small.png")
blueship_rec = blueship.get_rect()
blueship_rec.topright=(350, 250)
blueship = pygame.transform.scale(blueship,(200,200))

redship = pygame.image.load("pixel_ship_red_small.png")
redship_rec = redship.get_rect()
redship_rec.topright=(120, 250)
redship = pygame.transform.scale(redship,(200,200))

greenship = pygame.image.load("pixel_ship_green_small.png")
greenship_rec = greenship.get_rect()
greenship_rec.topright=(620, 250)
greenship = pygame.transform.scale(greenship,(200,200))

yellowship = pygame.image.load("pixel_ship_yellow.png")
yellowship_rec = yellowship.get_rect()
yellowship_rec.topright=(400, 488)
yellowship = pygame.transform.scale(yellowship,(200,200))

font = pygame.font.SysFont(None, 75)

def draw_text(text, font, color, surface, x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False

def options():
    running = True
    click = False
    while running:
        screen.fill((0,0,0))
        screen.blit(Backgroundimage,Backgroundimage_rec)
        draw_text('Options',font, (255, 0, 0), screen, 290, 100)
        mx, my = pygame.mouse.get_pos()
        button_3 = pygame.Rect(190, 300, 400, 70)
        button_4 = pygame.Rect(190, 400, 400, 70)
        button_3.centerx = 400
        button_4.centerx = 400
        pygame.draw.rect(screen, (150, 0, 30), button_3)
        pygame.draw.rect(screen, (150, 0, 30), button_4)
        draw_text('Cheat Codes',font, (0, 0, 0), screen, 240, 310)
        draw_text('Colors',font, (0, 0, 0), screen, 305, 410)
        if button_3.collidepoint((mx, my)):
            if click:
                cheat()
        if button_4.collidepoint((mx, my)):
            if click:
                colors()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
    

def cheat():
    running = True
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(300, 300, 150, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        if text == "bruh":
                            cheat1 = True
                        if text == "123":
                            cheat2 = True
                        if text == "hola":
                            cheat3 = True
                        if text == "10101":
                            cheat4 = True
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if event.key == K_ESCAPE:
                    running = False

        screen.fill((0,0,0))
        screen.blit(Backgroundimage,Backgroundimage_rec)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.update()
        mainClock.tick(60)

def colors():

    running = True
    click = False
    while running:
        screen.fill((0,0,0))
        screen.blit(Backgroundimage,Backgroundimage_rec)
        screen.blit(blueship, blueship_rec)
        screen.blit(redship, redship_rec)
        screen.blit(greenship, greenship_rec)
        draw_text('Colors',font, (0, 255, 0), screen, 317, 100)
        mx, my = pygame.mouse.get_pos()
        button_5 = pygame.Rect(190, 250, 200, 200)
        button_6 = pygame.Rect(190, 250, 200, 200)
        button_7 = pygame.Rect(190, 250, 200, 200)
        button_8 = pygame.Rect(190, 500, 200, 200)
        button_5.centerx = 150
        button_6.centerx = 400
        button_7.centerx = 650
        button_8.centerx = 400
        pygame.draw.rect(screen, (255, 0, 0), button_5)
        pygame.draw.rect(screen, (0, 0, 255), button_6)
        pygame.draw.rect(screen, (0, 255, 0), button_7)
        pygame.draw.rect(screen, (255, 255, 0), button_8)
        #draw_text('Red',font, (0, 0, 0), screen, 100, 350)
        #draw_text('Blue',font, (0, 0, 0), screen, 335, 350)
        #draw_text('green',font, (0, 0, 0),screen, 580, 350)
        if button_5.collidepoint((mx, my)):
            if click:
                red()
        if button_6.collidepoint((mx, my)):
            if click:
                blue()
        if button_7.collidepoint((mx, my)):
            if click:
                green()
        if button_8.collidepoint((mx, my)):
            if click:
                yellow()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.blit(blueship, blueship_rec)
        screen.blit(redship, redship_rec)
        screen.blit(greenship, greenship_rec)
        screen.blit(yellowship, yellowship_rec)
        pygame.display.update()
        mainClock.tick(60)


def red():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('red',font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def blue():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('blue',font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def green():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('green',font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def yellow():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('yellow',font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)