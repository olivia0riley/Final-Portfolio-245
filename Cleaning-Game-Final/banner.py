
import pygame
import random

from spritesheet_functions import SpriteSheet
from vector import Vector

class Banner(pygame.sprite.Sprite):

    stalltime = 2

    def __init__ (self, swidth):


        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Set sprite
        self.image = SpriteSheet("Sprite_Lose_Banner.png").get_image(0, 0, 700, 655)

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.centerx = swidth/2
        self.rect.y = -self.rect.height

        # For death animation
        self.v = Vector(0, 0)
        self.va = 0.1
        self.stall = 0
        self.stop = False

        
    def drop(self):
        # Funny drop animation for when the player dies
        self.stall += 1
        if self.stop == False:
            if self.stall > self.stalltime:
                print(self.v.y)
                print(self.rect.y)
                self.rect.y += int(self.v.y)
                self.v.y += self.va
                if self.rect.y > -20:
                    self.rect.y -= int(self.v.y)
                    self.v.y *= -1/2
                    if abs(self.v.y) < 1:
                        self.stop = True
                self.stall = 0

        
    
if __name__ == "__main__":
    size = (1024,749)
    screen = pygame.display.set_mode(size)
    h = Banner(1024,749)
    

        
