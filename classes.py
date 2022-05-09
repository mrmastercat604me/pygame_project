import pygame,math,sys

class Player():
    def __init__(self,color,pos,surface):
        self.color = color
        self.image = pygame.image.load(f'assets/pixel_ship_{self.color}.png')
        self.surface = surface
        self.velocity = 7
        self.click = False
        self.lives = 3
        self.status = "alive"
        self.score = 0
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.laser = Laser(self.color,(-100,-100),self.surface)


    def controls(self):
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                self.rect.y -= self.velocity
            if key[pygame.K_a]:
                self.rect.x -= self.velocity
            if key[pygame.K_s]:
                self.rect.y += self.velocity
            if key[pygame.K_d]:
                self.rect.x += self.velocity
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            # if event.type == pygame.MOUSEBUTTONUP:
            #     if event.button == 1:
            #         self.click = False
            if event.type == pygame.QUIT:
                pygame.quit()
            if key[pygame.K_ESCAPE]:
                self.status = "dead"
        if self.click:
            self.laser = Laser(self.color,self.rect.center,self.surface)
            print("PEW")
        self.click = False

    def render(self,correction_angle):
            mx, my = pygame.mouse.get_pos()
            dx,dy =  mx - self.rect.centerx, my - self.rect.centery
            angle =  math.degrees(math.atan2(-dy, dx)) - correction_angle
            rot_image = pygame.transform.rotate(self.image,angle)
            rot_image_rect = rot_image.get_rect(center = self.rect.center)
            #DEBUG pygame.draw.rect(surface,(255,255,255),rot_image_rect,2)
            self.surface.blit(rot_image,rot_image_rect.topleft)
            self.laser.run()

    def collision(self):
        pass

    def status(self):
        if self.lives <= 0:
            self.status = "dead"
        
    
    def run(self):
        self.controls()
        self.collision()
        self.render(90)


class Laser():
    def __init__(self,color,pos,surface):
        self.color = color
        self.image = pygame.image.load(f'assets/pixel_laser_{self.color}.png')
        self.surface = surface
        self.velocity = 10
        self.click = False
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.base = pygame.image.load(f'assets/pixel_laser_{self.color}.png')
        self.base_rect = self.base.get_rect()
        self.base_rect.center = (-100,-100)
    
    def face_mouse(self,correction_angle):
        mx, my = pygame.mouse.get_pos()
        dx,dy =  mx - self.rect.centerx, my - self.rect.centery
        angle =  math.degrees(math.atan2(-dy, dx)) - correction_angle
        rot_image = pygame.transform.rotate(self.image,angle)
        rot_image_rect = rot_image.get_rect(center = self.rect.center)
        #DEBUG pygame.draw.rect(surface,(255,255,255),rot_image_rect,2)
        self.surface.blit(rot_image,rot_image_rect.topleft)


    def collision(self):
        pass
    
    def run(self):
        self.face_mouse(90)
        self.collision()

class Meteor():
    def __init__(self,level,pos,surface):
        self.image = pygame.image.load(f'assets/meteor{level}')
        self.surface = surface
        self.level = level
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def collision(self):
        pass
