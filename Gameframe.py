
import pygame
import random
pygame.init()


width = 800
height = 800
fps = 60
Velocity = 15
display_surface = pygame.display.set_mode((width, height))
Backgroundimage = pygame.image.load("background-black.png")
Backgroundimage_rec= Backgroundimage.get_rect()

shipimage = pygame.image.load("assets/pixel_ship_yellow.png")
shipimage_rec= shipimage.get_rect()

enemyimage = pygame.image.load("assets/meteor1.png")
enemyimage_rec= enemyimage.get_rect()
enemy_x_pos = random.randint(-100,100) 
enemy_y_pos = random.randint(-100,100)


Backgroundimage_rec.topleft=(0,0)
clock=pygame.time.Clock()

Backgroundimage_rec = Backgroundimage.get_rect()
Backgroundimage_rec.centerx = width//2
Backgroundimage_rec.centery = height//2
shipimage_rec.centerx = width//2
shipimage_rec.centery = height//2
enemyimage_rec.y = enemy_y_pos
enemyimage_rec.x = enemy_x_pos
if __name__ == "__main__":
        running = True
while running:
        
        #for event in 
        pygame.event.get()
        keys = pygame.key.get_pressed()
        surface = None
        if keys[pygame.K_LEFT]:
                surface = pygame.transform.rotate(display_surface, 1)
                #shipimage = pygame.transform.rotate(display_surface, shipimage, 1)
                #shipimage_rec=shipimage.get_rect()
                #shipimage_rec.centerx = width//2
                #shipimage_rec.centery = height//2
        if keys[pygame.K_ESCAPE]:
                running = False
        display_surface.fill((0,0,0))
        display_surface.blit(Backgroundimage,Backgroundimage_rec)
        if surface is not None:
                display_surface.blit(surface, (0, 0))
        display_surface.blit(enemyimage,enemyimage_rec)
        display_surface.blit(shipimage,shipimage_rec)
        pygame.display.update()
        if running == False:
                pygame.quit
pygame.display.update(Backgroundimage_rec)
clock.tick(fps)
pygame.quit()
