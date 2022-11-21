## By Nolan
##
import pygame

from vector import Vector
from spritesheet_functions import SpriteSheet

#from rectangle import Rectangle

class Mess(pygame.sprite.Sprite):

    def __init__ (self, x, y, room):
        
        self.x = x
        self.y = y
        
        # Call the spritesheet constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = SpriteSheet("Sprite_Mess.png").get_image(0, 0, 100, 100)
        
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Center and Radius for Roomba targeting methods
        self.p = Vector (self.rect.centerx,self.rect.centery)
        self.r = (self.rect.width + self.rect.height)/4  

        #Timer for cleaned by player
        self.pTimer = 0 

        
        #Timers for cleaned by roombas (yes, I know)
        self.rTimerList = []
        i = 0
        for r in room.roombas:
            
            r.cTimeIndex = i
            self.rTimerList.append(0)
            i += 1




  
        