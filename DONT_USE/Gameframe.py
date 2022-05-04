<<<<<<< HEAD
<<<<<<< HEAD:Gameframe.py
import pygame
import random
import math
=======
import pygame,random,math
>>>>>>> 8d3936aa91f330aeb22e6995694f719097632e8f:DONT_USE/Gameframe.py
=======
import pygame,random,math
>>>>>>> 8d3936aa91f330aeb22e6995694f719097632e8f
pygame.init()


width = 800
height = 800
fps = 60
<<<<<<< HEAD
<<<<<<< HEAD:Gameframe.py
Velocity = 10
=======
Velocity = 3
>>>>>>> 8d3936aa91f330aeb22e6995694f719097632e8f:DONT_USE/Gameframe.py
=======
Velocity = 3
>>>>>>> 8d3936aa91f330aeb22e6995694f719097632e8f
display_surface = pygame.display.set_mode((width, height))
Backgroundimage = pygame.image.load("assets/background-black.png")
Backgroundimage_rec= Backgroundimage.get_rect()

shipimage = pygame.image.load("assets/pixel_ship_yellow.png")
shipimage_rect= shipimage.get_rect()

def face_mouse(image,image_rect,correction_angle,surface):
    mx, my = pygame.mouse.get_pos()
    dx,dy =  mx - image_rect.centerx, my - image_rect.centery
    angle =  math.degrees(math.atan2(-dy, dx)) - correction_angle
    rot_image = pygame.transform.rotate(image,angle)
    rot_image_rect = rot_image.get_rect(center = image_rect.center)
    surface.blit(rot_image,rot_image_rect.topleft)
    pygame.display.update()


enemyimage = pygame.image.load("assets/pixel_ship_green_small.png")
enemyimage_rec= enemyimage.get_rect()
enemy_x_pos = random.randint(-100,100) 
enemy_y_pos = random.randint(-100,100)
def face_mouse(image,image_rect,correction_angle,surface):
    mx, my = pygame.mouse.get_pos()
    dx,dy =  mx - image_rect.centerx, my - image_rect.centery
    angle =  math.degrees(math.atan2(-dy, dx)) - correction_angle
    rot_image = pygame.transform.rotate(image,angle)
    rot_image_rect = rot_image.get_rect(center = image_rect.center)
    surface.blit(rot_image,rot_image_rect.topleft)
    pygame.display.update()

       

Backgroundimage_rec.topleft=(0,0)
clock=pygame.time.Clock()

Backgroundimage_rec = Backgroundimage.get_rect()
Backgroundimage_rec.centerx = width//2
Backgroundimage_rec.centery = height//2
shipimage_rect.centerx = width//2
shipimage_rect.centery = height//2
enemyimage_rec.y = enemy_y_pos
enemyimage_rec.x = enemy_x_pos
pygame.display.set_caption('blastroids')
font = pygame.font.Font('freesansbold.ttf', 32)
if __name__ == "__main__":
        running = True
while running:
        
        #for event in 
        for event in pygame.event.get():
            pygame.event.get()
        keys = pygame.key.get_pressed()
        surface = None
        #if keys[pygame.K_LEFT]:
        if keys[pygame.K_a]: #left
                shipimage_rect.x -= Velocity
        if keys[pygame.K_d]: #right
                shipimage_rect.x += Velocity
        if keys[pygame.K_w]: #up
                shipimage_rect.y -= Velocity
        if keys[pygame.K_s]: #down
                shipimage_rect.y += Velocity
        if keys[pygame.K_ESCAPE]:
                running = False
        if event.type == pygame.QUIT:
            running = False
        
        display_surface.fill((0,0,0))
        
        display_surface.blit(Backgroundimage,Backgroundimage_rec)
        if surface is not None:
                display_surface.blit(surface, (0, 0))
        display_surface.blit(enemyimage,enemyimage_rec)
<<<<<<< HEAD
<<<<<<< HEAD:Gameframe.py
        #display_surface.blit(shipimage,shipimage_rect)
        face_mouse(shipimage, shipimage_rect, 90, display_surface)
=======
        face_mouse(shipimage,shipimage_rect,90,display_surface)
>>>>>>> 8d3936aa91f330aeb22e6995694f719097632e8f:DONT_USE/Gameframe.py
=======
        face_mouse(shipimage,shipimage_rect,90,display_surface)
>>>>>>> 8d3936aa91f330aeb22e6995694f719097632e8f
        pygame.display.update()
        pygame.display.update(Backgroundimage_rec)
        clock.tick(fps)
pygame.quit()
