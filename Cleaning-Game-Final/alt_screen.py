
import pygame

from spritesheet_functions import SpriteSheet
from vector import Vector

class AltScreen(pygame.sprite.Sprite):

    def __init__ (self, width, height, type):

        self.width = width
        self.height = height
        self.timescale = 1/1000

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.v = Vector(0,0)

        # Background images

        # Set background sprite based on type
        if type == "start":
            self.image = SpriteSheet("Sprite_Start_Background.png").get_image(0, 0, width, height - 4)
        if type == "pause":
            self.image = SpriteSheet("Sprite_Pause_Screen.png").get_image(0, 0, width, height + 6)
        if type == "win":
            self.image = SpriteSheet("Sprite_Win_Background.png").get_image(0, 0, width, height)

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    
if __name__ == "__main__":
    size = (1024,749)
    screen = pygame.display.set_mode(size)
    r = AltScreen(1024,749)
    

        
