import pygame
import random
pygame.init()


width = 800
height = 800
fps = 60
Velocity = 15
display_surface = pygame.display.set_mode((width, height))
Backgroundimage = pygame.image.load("assets/background-black.png")
Backgroundimage_rec= Backgroundimage.get_rect()

shipimage = pygame.image.load("assets/pixel_ship_yellow.png")
shipimage_rect= shipimage.get_rect()

enemyimage = pygame.image.load("assets/meteor1.png")
enemyimage_rec= enemyimage.get_rect()
enemy_x_pos = random.randint(-100,100) 
enemy_y_pos = random.randint(-100,100)


Backgroundimage_rec.topleft=(0,0)
clock=pygame.time.Clock()

Backgroundimage_rec = Backgroundimage.get_rect()
Backgroundimage_rec.centerx = width//2
Backgroundimage_rec.centery = height//2
shipimage_rect.centerx = width//2
shipimage_rect.centery = height//2
enemyimage_rec.y = enemy_y_pos
enemyimage_rec.x = enemy_x_pos
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
        display_surface.blit(shipimage,shipimage_rect)
        pygame.display.update()
        if running == False:
                pygame.quit
pygame.display.update(Backgroundimage_rec)
clock.tick(fps)
pygame.quit()
