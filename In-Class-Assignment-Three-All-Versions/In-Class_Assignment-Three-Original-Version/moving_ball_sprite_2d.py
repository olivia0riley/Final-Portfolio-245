##
## Author: Kristina Striegnitz
##
## Version: Fall 2011 
##
## Updates: John Rieffel, Fall 2022
##
## This file defines a ball class that can move in two dimensions and
## can bounce off other balls.

from hashlib import new
import pygame
import math

from vector import Vector
from ball_2d import Ball


class MovingBall (Ball):

    v = Vector(0.0, 0.0)

    speedlimit = 500

    def __init__ (self, x, y, r, m, color, xv, yv):

        Ball.__init__(self, x, y, r, m, color)

        self.v = Vector(float(xv),float(yv))


    def simulate (self,width, height):
        self.move()

    def bounce_walls (self, width, height):

        if self.p.x + self.r > width:
            self.p.x = width - self.r
            self.v.x *= -1
        elif self.p.x - self.r < 0:
            self.p.x = 0 + self.r
            self.v.x *= -1
        if self.p.y + self.r > height:
            self.p.y = height - self.r
            self.v.y *= -1
        elif self.p.y - self.r < 0:
            self.p.y = 0 + self.r
            self.v.y *= -1


    def move (self):

        self.p = self.p + self.v


    def collide (self, other):
        """
        Checks whether two circles collide. If they do and are already
        intersecting, they get moved apart a bit. The return value is
        None, if there is no collision, and the vector pointing from
        the center of the first to the center of the second ball if
        there is a collision.
        """

        distance_vector = self.p - other.p

        if distance_vector.y < self.r and distance_vector.y > (-1 * self.r):
            self.p.x += 1.5
            other.p.x -= 1.5
            return distance_vector
        else: 
            return None

    def getResponse(self,other):
        '''
        Calculates the new velocity after a collision
        '''
                            # new velocity is 
                    # v1_normal' = v1_normal*(m1-m2)+2*m2*v2_normal
                    #              ----------------------------      
                    #                   m1 + m2
       
        pass 

    def bounce (self, response, n):
        '''
        given a response vector, 
        change's balls velocity according to the energy/momentum conserving equations
        '''
        pass

    def setVelocity(self,v):
        self.v = v

    def intersectsWithLineSegment(self,line):
        '''

        given a line, returns True if the ball intersects the line,
        False otehrwise

        a line is described as a tuple of two Vector objects

        Algorithm is described here
        https://www.baeldung.com/cs/circle-line-segment-collision-detection
        '''
        pass

    # only works on axis-aligned boxes
    def collidesWithAABB(self,box):
      '''
      given an AABB, returns true of the ball collides
      '''  
      hit = True

      if box.rect.x > self.p.x + self.r:
            hit = False
      if box.rect.y > self.p.y + self.r:
            hit = False
      if box.rect.x + box.rect.w < self.p.x:
            hit = False
      if box.rect.y + box.rect.h < self.p.y:
            hit = False
        
      print(hit)
