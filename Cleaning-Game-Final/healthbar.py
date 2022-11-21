
import pygame
import random

from spritesheet_functions import SpriteSheet
from vector import Vector

class Healthbar(pygame.sprite.Sprite):

    frames = []

    stalltime = 2

    def __init__ (self, x, y, health):

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Create sprites
        health_0 = SpriteSheet("Sprite_Health_0.png").get_image(0, 0, 210, 120)
        health_1 = SpriteSheet("Sprite_Health_1.png").get_image(0, 0, 222, 120)
        health_2 = SpriteSheet("Sprite_Health_2.png").get_image(0, 0, 227, 120)
        health_3 = SpriteSheet("Sprite_Health_3.png").get_image(0, 0, 222, 120)
        
        # Create spritesheet
        self.frames.append(health_0)
        self.frames.append(health_1)
        self.frames.append(health_2)
        self.frames.append(health_3)

        # Sets image based on health
        self.image = self.frames[health]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # For death animation
        self.v = Vector(random.randint(-1,3), -2)
        self.va = 0.1
        self.stall = 0

        
    def update(self, health):
        if -1 < health < 4:
            self.image = self.frames[health]

        # Funny drop animation when player dies
        if health <= 0:
            self.stall += 1
            if self.stall > self.stalltime:
                self.rect.x += self.v.x
                self.rect.y += int(self.v.y)
                self.v.y += self.va
                self.stall = 0

        
    
if __name__ == "__main__":
    size = (1024,749)
    screen = pygame.display.set_mode(size)
    h = Healthbar(1024,749)
    

        
