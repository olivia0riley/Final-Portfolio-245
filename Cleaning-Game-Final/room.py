
import pygame

from spritesheet_functions import SpriteSheet
from vector import Vector
from simple_platform import Box

class Room(pygame.sprite.Sprite):

    #just in case
    gravity = Vector (0,0)

    #list of backgrounds
    backgrounds = []

    def __init__ (self, width, height):

        self.width = width
        self.height = height
        self.timescale = 1/1000

        #lists of objects in rooms
        self.roombas = []
        self.messes = []
        self.doors = []
        
        # Wall list
        self.walls = pygame.sprite.Group()

        # Create the borders of the room
        #Left wall
        p1 = Box(pygame.color.Color("yellow"),0,0,height,90) 
        #Right wall
        p2 = Box(pygame.color.Color("blue"),width-100,0,height,100) 
        #Ceiling
        p3 = Box(pygame.color.Color("darkblue"),0,0,85,width) 
        #Floor
        p4 = Box(pygame.color.Color("green"),0,height-85,85,width) 

        # Adds platforms to walls
        self.walls.add(p1)
        self.walls.add(p2)
        self.walls.add(p3)
        self.walls.add(p4)


        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.v = Vector(0,0)

        # Background image
        background1 = SpriteSheet("Sprite_Room.png").get_image(0, 0, width, height)

        # Set image
        self.image = background1

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()


    def beat_level(self):
        if len(self.messes) < 1:
            return True
        else:
            return False
    
    def update(self):
        pass
    
if __name__ == "__main__":
    size = (1024,749)
    screen = pygame.display.set_mode(size)
    r = Room(1024,749)
    

        
