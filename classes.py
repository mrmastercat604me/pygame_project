import pygame,math,sys

class Player():
    def __init__(self,color,pos,surface):
        self.color = color
        self.image = pygame.image.load(f'assets/pixel_ship_{self.color}.png')
        self.surface = surface
        self.velocity = 7
        self.lives = 3
        self.status = "alive"
        self.click = False
        self.score = 0
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.laser = None
        self.angle = 0


    def controls(self,events):
        click = False
        for event in events:
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                self.rect.y -= self.velocity
            if key[pygame.K_a]:
                self.rect.x -= self.velocity
            if key[pygame.K_s]:
                self.rect.y += self.velocity
            if key[pygame.K_d]:
                self.rect.x += self.velocity
            if event.type == pygame.QUIT:
                pygame.quit()
            if key[pygame.K_ESCAPE]:
                self.status = "dead"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    def render(self,correction_angle):
            mx, my = pygame.mouse.get_pos()
            dx,dy =  mx - self.rect.centerx, my - self.rect.centery
            self.angle =  math.degrees(math.atan2(-dy, dx)) - correction_angle
            rot_image = pygame.transform.rotate(self.image,self.angle)
            rot_image_rect = rot_image.get_rect(center = self.rect.center)
            #DEBUG pygame.draw.rect(surface,(255,255,255),rot_image_rect,2)
            self.surface.blit(rot_image,rot_image_rect.topleft)
            if self.laser is not None:
                self.laser.run()

    def collision(self):
        pass

    def get_status(self):
        if self.lives <= 0:
            self.status = "dead"
        else:
            self.status = "alive"

    def summon_laser(self):
        if self.click:
            self.laser = Laser(self.color,self.rect.center,self.surface)
            self.laser.degrees = self.angle
            self.laser.image = pygame.transform.rotate(self.laser.image,self.laser.degrees)
            self.laser.rect = self.laser.image.get_rect(center = self.laser.rect.center)
        self.click = False

    def run(self,events):
        self.controls(events)
        self.collision()
        self.get_status()
        self.summon_laser()
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
        self.degrees = 0

        self.base = pygame.image.load(f'assets/pixel_laser_{self.color}.png')
        self.base_rect = self.base.get_rect()
        self.base_rect.center = (-100,-100)
    
    def render(self):
        self.surface.blit(self.image,self.rect)


    def collision(self):
        pass
    
    def run(self):
        self.render()
        self.collision()


class Meteor():
    def __init__(self,level,pos,surface):
        self.image = pygame.image.load(f'assets/meteor{level}.png')
        self.surface = surface
        self.level = level
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def collision(self,rect):
        if self.rect.x >= 800:
            pass
        elif self.rect.x <= 0:
            pass
        elif self.rect.y >= 800:
            pass
        elif self.rect.y <= 0:
            pass
        else:
            pass
        if self.rect.colliderect(rect):
           return True
        return False
    def render(self):
        self.surface.blit(self.image,self.rect)

