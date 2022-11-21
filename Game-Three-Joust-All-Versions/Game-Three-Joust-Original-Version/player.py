"""
Derived from code provided at
http://programarcadegames.com/
"""
import pygame


from spritesheet_functions import SpriteSheet
from vector import Vector

class Player(pygame.sprite.Sprite):

    # -- Attributes
    # Set speed vector of player

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames = []


    # -- Methods
    def __init__(self):
        """ Constructor function """
        #This is ugly, but it came with the example code...

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.v = Vector(0,0)

        #direction facing (True = right, False = left)
        self.face = True
        
        self.jump_height = 35

        #boolean statements for smoother controlls
        self.goingRight = False
        self.goingLeft = False

        sprite_sheet = SpriteSheet("p1_walk.png")
        # Load all the images into a list
        image = sprite_sheet.get_image(0, 0, 66, 90)
        self.walking_frames.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        self.walking_frames.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        self.walking_frames.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        self.walking_frames.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        self.walking_frames.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        self.walking_frames.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        self.walking_frames.append(image)
        # Set the image the player starts with
        self.image = self.walking_frames[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """
        # Gravity etc
        self.simulate()

        # Move left/right
       
        frame = (self.rect.x // 30) % len(self.walking_frames)
        self.image = self.walking_frames[frame]
    
        if self.v.x != 0 or self.v.y != 0:
         if self.face == False:
          self.image = pygame.transform.flip(self.image, True, False)
           
        elif self.v.x == 0 and self.v.y == 0:
           if self.face == False:
            self.image = pygame.transform.flip(self.image, True, False)

        # Jump for the little guy 

        if self.rect.y <= 200:
            self.v.y += 9.8
        if self.rect.y >= 400:
            self.rect.y = 480 - self.rect.height
            self.v.y = 0
            


    def simulate(self):
        """ Calculate effect of gravity. """
        ## NOTE USE self.rect for position
        self.rect.x += self.v.x
        self.rect.y += self.v.y
    
    def jump (self):
        ''''
        Makes the player "jump" in the air
        '''
        self.v.y -= self.jump_height

        
        

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.v = Vector (-1,0)
        self.face = False
        self.goingLeft = True


    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.v = Vector(1,0)
        self.face = True
        self.goingRight = True

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.v = Vector(0,0)



if __name__ == "__main__":
    size = (640,480)
    screen = pygame.display.set_mode(size)
    p = Player()