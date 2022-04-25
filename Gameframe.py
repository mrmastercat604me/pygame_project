import pygame

pygame.init()
width = 400
height = 400
fps = 60
Velocity = 15
display_surface = pygame.display.set_mode((width, height))
Background.image = pygame.image.load("background-black.png")
clock=pygame.time.Clock()

if __name__ == "__main__":
     running = True
     while running:
        
        #for event in 
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
                    running = False
        display_surface.fill((0,0,0))
       
pygame.display.update(Background.image)
clock.tick(fps)
pygame.quit()
