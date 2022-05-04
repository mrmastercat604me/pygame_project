import pygame, sys, math, random

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

def main_menu():
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
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
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

def game():
    global color

    running = True
    click = False
    Velocity = 7
    laser_vel = 10
    
    if color == "yellow":
        shipimage = pygame.image.load("assets/pixel_ship_yellow.png")
        laser = pygame.image.load("assets/pixel_laser_yellow.png")
        laser_first = pygame.image.load("assets/pixel_laser_yellow.png")
    elif color == "green":
        shipimage = pygame.image.load("assets/pixel_ship_green_small.png")
        laser = pygame.image.load("assets/pixel_laser_green.png")
        laser_first = pygame.image.load("assets/pixel_laser_green.png")
    elif color == "red":
        shipimage = pygame.image.load("assets/pixel_ship_red_small.png")
        laser = pygame.image.load("assets/pixel_laser_red.png")
        laser_first = pygame.image.load("assets/pixel_laser_red.png")
    elif color == "blue":
        shipimage = pygame.image.load("assets/pixel_ship_blue_small.png")
        laser = pygame.image.load("assets/pixel_laser_blue.png")
        laser_first = pygame.image.load("assets/pixel_laser_blue.png")

    shipimage_rect= shipimage.get_rect()
    shipimage_rect.center = (400,400)

    enemyimage = pygame.image.load("assets/meteor1.png")
    enemyimage_rect= enemyimage.get_rect()
    enemyimage_rect.x = random.randint(20,780) 
    enemyimage_rect.y = random.randint(20,780)
    if enemyimage_rect.colliderect(shipimage_rect):
        enemyimage_rect.x = random.randint(20,780) 
        enemyimage_rect.y = random.randint(20,780)
    
    laser_rect = laser.get_rect()
    laser_rect.center = (-100,-100)

    lives = 3

    screen.fill((0,0,0))
    while running:
        
        def face_mouse(image,image_rect,correction_angle,surface):
            mx, my = pygame.mouse.get_pos()
            dx,dy =  mx - image_rect.centerx, my - image_rect.centery
            angle =  math.degrees(math.atan2(-dy, dx)) - correction_angle
            rot_image = pygame.transform.rotate(image,angle)
            rot_image_rect = rot_image.get_rect(center = image_rect.center)
            #DEBUG pygame.draw.rect(surface,(255,255,255),rot_image_rect,2)
            surface.blit(rot_image,rot_image_rect.topleft)

        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if key[pygame.K_a]:
                shipimage_rect.x -= Velocity
            if key[pygame.K_d]:
                shipimage_rect.x += Velocity
            if key[pygame.K_w]:
                shipimage_rect.y -= Velocity
            if key[pygame.K_s]:
                shipimage_rect.y += Velocity
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if lives <= 0:
                running = False

        if enemyimage_rect.colliderect(shipimage_rect):
            lives -= 1
            enemyimage_rect.x = random.randint(20,780) 
            enemyimage_rect.y = random.randint(20,780)

        screen.blit(Backgroundimage,Backgroundimage_rec)

        font = pygame.font.SysFont(None, 40)
        draw_text((f"Lives: {lives}"),font,(255,0,0),screen,0,0)
        font = pygame.font.SysFont(None, 75)

        screen.blit(enemyimage,enemyimage_rect)
        face_mouse(shipimage,shipimage_rect,90,screen)
        
        if click:
            laser_rect.center = shipimage_rect.center
            mx, my = pygame.mouse.get_pos()
            dx,dy = mx - laser_rect.centerx, my - laser_rect.centery

            angle = math.degrees(math.atan2(-dy,dx)) - 90 #correction angle
            laser = pygame.transform.rotate(laser_first,angle)
            laser_rect = laser.get_rect(center = laser_rect.center)
            print("Pew")
            click = False
        #DEBUG pygame.draw.rect(screen,(255,255,255),laser_rect,2)
        laser_rect.x += laser_vel
        laser_rect.y += laser_vel
        screen.blit(laser,laser_rect)

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