import pygame
from vector import Vector
from math import atan2, degrees, sin, cos, pi
from spritesheet_functions import SpriteSheet
class Broom(pygame.sprite.Sprite):
    #position = Vector(0,0)
    #rotation = 0 
    
    pushDist = 50   # Distance from the player the broom is pushed

    def __init__(self, player) -> None:
        self.position = Vector(player.rect.x, player.rect.y)
        # make sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = SpriteSheet("Sprite_Broom.png").get_image(0,20,275,509)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(100,200))
        self.ogimage = pygame.transform.scale(self.image,(100,200))
        self.ctr = 0 # current total rotation (where it is pointing)
        self.ctdr = 0 # current total desired rotation (where it should be pointing)
        
        ###testing if i can do pixel mask collision below
        self.mask = pygame.mask.from_surface(self.image)
        

    def update(self, player, mouseX, mouseY):
        self.rect.x = player.rect.x-(self.image.get_width())/2  +108/2 #+275/2
        self.rect.y = player.rect.y-(self.image.get_height())/2  +(95)# +509/2
        #self.position = Vector(player.rect.x, player.rect.y)
        
        #self.image = pygame.transform.rotate(self.image, )

        # inspired by code found on https://www.folkstalk.com/tech/python-calculate-angle-between-two-points-with-code-examples/
        self.ctdr = 270-degrees(atan2(player.rect.centery-mouseY, player.rect.centerx-mouseX)) #degrees(atan((mouseY-player.rect.y)/(mouseX-player.rect.x)))+90
        self.image = pygame.transform.rotate(self.ogimage,int(self.ctdr))###self.rotation = #self.ctr-self.ctdr#+= (degrees(atan((mouseY-player.rect.y)/(mouseX-player.rect.x)))+90)
        
        self.ctdr *= pi/180
        
        #print(self.ctdr)
        #print(sin(self.ctdr))
        #print(cos(self.ctdr))
        self.rect.x += self.pushDist*sin(self.ctdr)
        self.rect.y += self.pushDist*cos(self.ctdr)
        ###testing if i can do pixel mask collision below
        #self.rect = pygame.transform.rotate(self.ogimage,int(self.ctdr))

        ###testing if i can do pixel mask collision below
        self.mask = pygame.mask.from_surface(self.image)
        #print(self.mask)

        
        #self.rect.centerx, self.rect.centery = player.rect.x, player.rect.y
        #self.ctr = 360-(degrees(atan2(player.rect.y-mouseY, player.rect.x-mouseX))+180)#self.ctr-self.ctdr(degrees(atan((mouseY-player.rect.y)/(mouseX-player.rect.x)))+90)
        # works for only some of the angles-- need to try it in game and put in if statement accounting for arctan's range being only 1pi
        #print(f"A: {self.ctdr}, px: {player.rect.x}, py: {player.rect.y}, mx: {mouseX}, my: {mouseY}")#\nD: {self.ctdr}")