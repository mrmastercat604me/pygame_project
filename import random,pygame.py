import random,pygame
class Enemy:
    def __init__(self):
        self.recycle()   # set the position & size initially

    def recycle( self ):
        # start or re-start an enemy position
        self.size = random.randint(10,40)
        self.xval = random.randint(0,700)
        self.yval = -self.size              # off the screen-top
        self.rect = pygame.Rect( self.xval, self.yval, self.size, self.size )

    def draw( self, screen ):
        pygame.draw.ellipse( screen, (255,255,0), self.rect )

    def create_enemy(self):
        global enemy_list
        new_enemy = Enemy()               # create a new Enemy
        enemy_list.append( new_enemy )    # add it to the list
    