
import pygame

from spritesheet_functions import SpriteSheet
from vector import Vector

class BobSprite(pygame.sprite.Sprite):

    def __init__ (self, x, y, bobage, type):

        self.type = type

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Set image
        if type == "start_button":
            self.image = SpriteSheet("Sprite_Button_Start.png").get_image(0, 0, 320, 116)
        if type == "pause_orbs":
            self.image = SpriteSheet("Sprite_Pause_Orbs.png").get_image(0, 0, 1024, 752)
        if type == "play_again_button":
            self.image = SpriteSheet("Sprite_Button_Play_Again.png").get_image(0, 0, 320, 131)
        if type == "quit_button":
            self.image = SpriteSheet("Sprite_Button_Quit.png").get_image(0, 0, 320, 155)

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Variables for bob
        self.yOrigin = y
        self.v = bobage
        self.a = 0.5
        self.stall = 0
        


    def bob(self): #Bobs up and down
        
        self.stall += 0.1
        if self.stall >= 1:
            self.v += self.a
            #print(self.v)
            self.rect.y += self.v

            if self.rect.y >= self.yOrigin:
                #print(self.rect.y)
                self.a = -0.5
                if self.type == "pause_buttons":
                    self.a = -0.2
            
            if self.rect.y <= self.yOrigin:
                #print(self.rect.y)
                self.a = 0.5
                if self.type == "pause_buttons":
                    self.a = 0.2
            
            self.stall = 0
    
if __name__ == "__main__":
    size = (1024,749)
    screen = pygame.display.set_mode(size)
    r = BobSprite(1024,749)
    

        
