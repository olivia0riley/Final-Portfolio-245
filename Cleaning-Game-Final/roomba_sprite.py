## Author: Olivia Riley, Mathhew Abner, & Nolan Kelley

## Importing necessary modules

import pygame
import math 
import random

from spritesheet_functions import SpriteSheet
from vector import Vector 
from moving_ball_2d import MovingBall
from sweeper import Player
from room import Room
# for rotating sprites
from math import atan2, degrees

## Creating Class "Roomba"

class Roomba (MovingBall):

    # Holds images for the switch between kinds of roombas
    roomba_sprites = []
    # Index of which sprite is used and determiner of what the roomba does
    i = 0
    
    # -- Methods
    def __init__ (self, x, y, i):
        ''' 
        Constructor function 
        '''

        ## Steering ball variables
        self.steering = []

        # Calling the parent's parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.v = Vector(0,0)
        self.p = Vector(x,y)
        self.i = i

        # Broken
        if i == 0:
            imageWidth = 95
            imageHeight = 75
        # plain
        elif i == 1:
            imageWidth = 83
            imageHeight = 75
        # knife
        elif i == 2:
            imageWidth = 120
            imageHeight = 75
        # pan
        elif i == 3:
            imageWidth = 114
            imageHeight = 75
        # scan
        elif i == 4:
            imageWidth = 108
            imageHeight = 75
        # mush
        elif i == 5:
            imageWidth = 84
            imageHeight = 75

        self.width = imageWidth
        self.height = imageHeight
    
        # Defining all roomba sprites
        broken_roomba = SpriteSheet ("Sprite_Roomba_Broken.png").get_image(0,0,imageWidth,imageHeight)
        plain_roomba = SpriteSheet ("Sprite_Roomba_Plain.png").get_image(0,0,imageWidth,imageHeight)
        knife_roomba = SpriteSheet ("Sprite_Roomba_Knife.png").get_image(0,0,imageWidth,imageHeight)
        pan_roomba = SpriteSheet ("Sprite_Roomba_Pan.png").get_image(0,0,imageWidth,imageHeight)
        scan_roomba = SpriteSheet ("Sprite_Roomba_Scan.png").get_image(0,0,imageWidth,imageHeight)
        mush_roomba = SpriteSheet ("Sprite_Roomba_Mush.png").get_image(0,0,imageWidth,imageHeight)

        # Appending roomba types to roomba_sprite list
        self.roomba_sprites.append(broken_roomba)
        self.roomba_sprites.append(plain_roomba)
        self.roomba_sprites.append(knife_roomba)
        self.roomba_sprites.append(pan_roomba)
        self.roomba_sprites.append(scan_roomba)
        self.roomba_sprites.append(mush_roomba)
        

        # Set the roomba sprite based on the roomba index
        self.image = self.roomba_sprites[i]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.center = self.p.x, self.p.y
        self.facing = Vector(1,0)                       #last direction the roomba was facing
        

        # Sets radius
        self.r = self.rect.height/2

        # Sets mass
        if -1 < i < 5:
            self.m = float(1)

        # Set starting velocity
        if i == 1:
            sVel = 40
            x = random.randint(1,4)
            if x == 1:
                self.v = Vector(sVel,sVel)
            if x == 2:
                self.v = Vector(-sVel,sVel)
            if x == 3:
                self.v = Vector(-sVel,-sVel)
            if x == 4:
                self.v = Vector(sVel,-sVel)

        # Set max targeting speed
        self.speedlimit = Vector(100,100)

        # For rotating sprites
        self.ogimage = self.roomba_sprites[i]
        self.ctr = 0 # current total rotation (where it is pointing)
        self.ctdr = 0 # current total desired rotation (where it should be pointing)
        
    ## Steering ball methods 
    def apply_steering (self):
        ## add all steering inputs to current velocity vector
        for s in self.steering:
            self.v += s

    def seek (self, target, thresh_weight, weight):
        
        thresh = thresh_weight * (target.r + self.r)

        distance_vector = target.p - self.p
        #distnce from boid to target
        distance = distance_vector.length()
        #checks that the boid is within threshold of the target 
        
        #find difference between my location and target location 
        desired_direction = (distance_vector).normalize()
        #multiply direction by max speed
        max_speed = self.speedlimit.length()
        desired_velocity = desired_direction * max_speed

        if distance >= thresh:
            ## first find the "error" between current velocity and desired velocity, and then multiply that error 
            ## by the weight, and then add it to steering inputs
            self.steering += [(desired_velocity - self.v)*weight]
        
        else:   #Slows down when approaching object
            #velocity decreases until reaching the center
            arrive_velocity = desired_velocity * (distance/thresh)
            # Append velocity to the steering list
            self.steering += [arrive_velocity*weight]
        print(self.v)

    def seekList(self, list, thresh_weight, weight):
        closest_object = list[0]
        #Finds the closest boid
        for o in list:
            closest_dist = (closest_object.p - self.p).length()
            #distnce from predator to any boid
            distance = (o.p - self.p).length()
            if distance < closest_dist:
                closest_object = o
        #updates closest distance
        closest_dist = (closest_object.p - self.p).length()
        
        #Chases the closest object
        self.seek(closest_object, thresh_weight, weight)

    def bounce_wall (self, pad):
        
        # Vectors from corners to ball
        vAE = Vector(self.p.x - pad.x,
        self.p.y - pad.y)
        vBE = Vector(self.p.x - (pad.x + pad.w),
        self.p.y - pad.y)
        vCE = Vector(self.p.x - pad.x,
        self.p.y - (pad.y + pad.h))
        vDE = Vector(self.p.x - (pad.x + pad.w),
        self.p.y - (pad.y + pad.h))

        # Vectors from corners to corners
        vAB = Vector(pad.w, 0)
        vBD = Vector(0, -pad.h)
        vDC = Vector(-pad.w, 0)
        vCA = Vector(0, pad.h)

        # Calculate ball distance to each wall
        dAB = abs(vAE.cross(vAB)) / vAB.length()
        dBD = abs(vBE.cross(vBD)) / vBD.length()
        dDC = abs(vDE.cross(vDC)) / vDC.length()
        dCA = abs(vCE.cross(vCA)) / vCA.length()

        # Check distance and reverse velocity
        if dAB <= self.r:
            #print ("could bounce bottom")
            if self.p.x > pad.x and self.p.x < pad.x + pad.w:
                self.p.y = pad.y - self.r
                self.v.y *= -1
                #print("bounce bottom")
                #return True
        if dBD <= self.r:
            #print ("could bounce left")
            if self.p.y > pad.y and self.p.y < pad.y + pad.h:
                self.p.x = pad.x + pad.w + self.r
                self.v.x *= -1
                #print("bounce left")
                ##return True
        if dDC <= self.r:
            #print ("could bounce top")
            if self.p.x > pad.x and self.p.x < pad.x + pad.w:
                self.p.y = pad.y + pad.h + self.r
                self.v.y *= -1
                #print("bounce top")
                #return True
        if dCA <= self.r:
            #print ("could bounce right")
            if self.p.y > pad.y and self.p.y < pad.y + pad.h:
                self.p.x = pad.x - self.r
                self.v.x *= -1
                #print("bounce right")
                #return True
        #return False


    ## Roomba methods
    def simulate(self, dt, pHitbox, broom, room):
        """ 
        Does everything
        """

        # Stuff everything but the broken roomba does
        if self.i == 0:
            pass
        else:
            self.check_break(broom)
            self.move(dt,room)
            self.clean_mess(room)       
            self.collide_edge(room)     # Collisions with window edges checked here (just in case):
            for w in room.walls:
                self.bounce_wall(w)     # Collisions with room walls checked here:
        
        # Calculates different Roomba behaviors
        self.behave(pHitbox,room)

        # Applies steering
        self.apply_steering()


    def update(self):
        ''' 
        "Animates" the Roombas
        '''
        if self.v.x != 0 or self.v.y != 0:
            self.facing = self.v

        # sets correct sprites
        self.ogimage = self.roomba_sprites[self.i]
        # also inspired by code found on https://www.folkstalk.com/tech/python-calculate-angle-between-two-points-with-code-examples/
        
        
        self.ctdr = 360-(degrees(atan2(self.facing.y, self.facing.x))) #degrees(atan((mouseY-player.rect.y)/(mouseX-player.rect.x)))+90
        self.image = pygame.transform.rotate(self.ogimage,int(self.ctdr))###self.rotation = #self.ctr-self.ctdr#+= (degrees(atan((mouseY-player.rect.y)/(mouseX-player.rect.x)))+90)

        # Set sprite position to ball position
        self.rect.center = self.p.x - 15, self.p.y - 20


    def behave (self,pHitbox,room):
        ''' 
        All different roomba behaviors
        '''
        #Broken Roomba
        if self.i == 0:
            self.v = Vector(0,0)

        #Plain Roomba
        if self.i == 1:
            pass

        #Knife Roomba
        if self.i == 2:
            self.seek(pHitbox,4,0.1)

        #Pan Roomba
        if self.i == 3:
            self.seekList(room.messes,4,0.1)

        #Scan Roomba
        if self.i == 4:
            bigList = room.messes
            bigList.append[pHitbox]
            self.seekList(bigList,4,0.1)
            pass

    def clean_mess(self, room):
        for m in room.messes:
            if pygame.sprite.collide_mask(self,m):
                #print(m.rTimer)
                m.rTimer += 1
            else:
                m.rTimer = 0

    def check_break(self, broom):
        if pygame.sprite.collide_mask(broom, self):
            self.i = 0             
            pass

    def check_got(self, pHitbox):
        if pygame.sprite.collide_mask(pHitbox, self):
            return True
        else:
            return False


if __name__ == "__main__":
    size = (640,480)
    screen = pygame.display.set_mode(size)
    p = Player()


