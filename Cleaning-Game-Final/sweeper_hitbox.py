"""
Derived from code provided at
http://programarcadegames.com/

Edited heavily by: Nolan Kelley
"""

# Use this file to calculate collision for the player.

import pygame


from spritesheet_functions import SpriteSheet
from vector import Vector

class PlayerHitbox(pygame.sprite.Sprite):

    
    def __init__(self, startHealth):

        # Set player stats
        self.pspeed = 1             #Movement speed
        self.score = 0              #Player score
        self.health = startHealth   #Health

        # Invincibility frames
        self.iframes = 0
        self.invincible = False

        # Boolean and frames for mushroom effect
        self.mushframes = 0
        self.mush = False

        # Boolean for cleaning
        self.cleaning = False

        #timer variables for walk speed
        self.stall = 0
        self.stallcap = 3

        #direction facing (True = right, False = left)
        self.face = True

        #boolean statements for smoother controlls
        self.goingRight = False
        self.goingLeft = False
        self.goingUp = False
        self.goingDown = False

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        
        self.v = Vector(0,0)

        # Sprite hitbox will be based on
        hitbox = SpriteSheet("Sprite_Sweeper_Hitbox.png").get_image(6, 102, 75, 51)

        # Set the image the player starts with
        self.image = hitbox

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        # Center and Radius for Roomba targeting methods
        self.p = Vector(self.rect.centerx,self.rect.centery)
        self.r = (self.rect.width + self.rect.height)/4         # about

    def simulate(self,room):
        """ Calculate collision. """
        ## NOTE USE self.rect for position
        
        #Slows movement when cleaning
        if self.cleaning:
            if self.stall >= self.stallcap:
                self.stall = 0
                self.rect.x += self.v.x
                self.rect.y += self.v.y
            else:
                self.stall += 1
        else:
            self.rect.x += self.v.x
            self.rect.y += self.v.y
        

        platforms = room.walls

        # For roomba targeting
        self.p = Vector(self.rect.centerx,self.rect.centery)

        # Collisions checked here:
        for p in platforms:
            if pygame.sprite.collide_rect(self,p):
                # Check to make sure it's not a wall collision
                if (self.rect.x + self.rect.width > p.rect.x + 3
                    and self.rect.x < p.rect.x + p.rect.width - 3):
                    # Check if on top of platform
                    if p.rect.y + (p.rect.height/3) > self.rect.y + self.rect.height > p.rect.y:
                        if self.rect.y + self.rect.height > p.rect.y + 1:
                            self.rect.y -= abs(self.rect.y + self.rect.height - p.rect.y -1)
                    # Check if below platform
                    elif p.rect.y + (p.rect.height/1.5 ) < self.rect.y < p.rect.y + p.rect.height:
                        self.v.y = 0
                        self.rect.y += 1
                # Check to make sure it's not a floor/celing collision
                if (self.rect.y < p.rect.y + p.rect.height - 3
                and self.rect.y + self.rect.height > p.rect.y + 3):
                    # Check if hit wall
                    if (self.rect.x + self.rect.width > p.rect.x 
                    and self.rect.x < p.rect.x + p.rect.width):
                        self.rect.x -= self.v.x # Prevents button mashing through walls
                        self.v.x *= 0
        
        # Cleans messes
        for m in room.messes:
            if self.cleaning:
                if pygame.sprite.collide_rect(self,m):
                    m.pTimer += 1
                    print(m.pTimer)
                else:
                    m.pTimer = 0
            else:
                m.pTimer = 0
        
        # Loses points over time
        if self.score > 0 and self.health > 0:
            self.score -= 0.004

        self.simIframes()
        self.simMushframes()
        self.hurt(room)
            
        #print(self.stall)

    # For taking damage
    def hurt(self,room):
        for r in room.roombas:
            if pygame.sprite.collide_mask(r, self) and r.i != 0 and self.invincible == False:
                self.health -= 1
                self.iframes = 100
                if r.i == 5:
                    self.mushframes = 600
    
    # Removes invincibility after a time
    def simIframes(self):
        print(self.iframes)
        if self.iframes > 0:
            self.iframes -= 1
            self.invincible = True
        else:
            self.invincible = False

    # Removes mush effect after a time
    def simMushframes(self):
        if self.mushframes > 0:
            self.mushframes -= 1
            self.mush = True
        else:
            self.mush = False
    
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits A key. """
        self.v.x = -self.pspeed
        if self.mush:
            self.v.x = self.pspeed
        self.face = False
        self.goingLeft = True
        

    def go_right(self):
        """ Called when the user hits D key. """
        self.v.x = self.pspeed
        if self.mush:
            self.v.x = -self.pspeed
        self.face = True
        self.goingRight = True
        

    def go_up(self):
        """ Called when user hits W key. """
        self.v.y = -self.pspeed
        if self.mush:
            self.v.y = self.pspeed
        self.goingUp = True
       

    def go_down(self):
        """ Called when user hits S key. """
        self.v.y = self.pspeed
        if self.mush:
            self.v.y = -self.pspeed
        self.goingDown = True

    # Player movement stopping
    def stop_left(self):
        """ Called when the user lets off A. """
        self.goingLeft = False
        #print('left false')
        if self.goingRight == False:
            #print('stop horiz')
            self.v.x = 0 
#        else:
#            self.v.x = -self.v.x
#            self.face = True

    def stop_right(self):
        """ Called when the user lets off D. """
        self.goingRight = False
        #print('right false')
        if self.goingLeft == False:
            #print('stop horiz')
            self.v.x = 0
#        else:
#            self.v.x = -self.v.x
#            self.face = False

    def stop_up(self):
        """ Called when the user lets off W. """
        self.goingUp = False
        #print('up false')
        if self.goingDown == False:
            #print('stop vert')
            self.v.y = 0

    def stop_down(self):
        """ Called when the user lets off S. """
        self.goingDown = False
        #print('down false')
        if self.goingUp == False:
            #print('stop vert')
            self.v.y = 0
        