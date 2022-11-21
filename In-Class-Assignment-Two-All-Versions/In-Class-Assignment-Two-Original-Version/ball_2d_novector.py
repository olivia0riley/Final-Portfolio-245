##
## Author: Kristina Striegnitz, John Rieffel
##
## Version: Fall 2022 
##
## This file defines a simple ball class. The ball is stationary; we
## just get to define its position, size and color. This
## implementation uses the vector class.

import pygame
import random
from vector import Vector
import math

class Ball:

    #initialize state variables

    def __init__ (self, x, y, r, m, color):
        self.p = Vector(float(x), float(y))
        self.r = r
        self.m = float(m)
        self.color = color

    def setVelocity(self,inVelocityX,inVelocityY):
        self.velocityVec = Vector(inVelocityX,inVelocityY)


    def updatePosition(self):
        self.p.x = self.p.x + self.velocityVec.x
        self.p.y = self.p.y + self.velocityVec.y

    def setColor(self, color):
        self.color = color

    def randomizePosition(self, width, height):
        self.p.x = random.randint(self.r+5, width)
        self.p.y = random.randint(self.r+5, height)

    def bounce(self, width, height):
        randomColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if self.p.x + self.r >= width or self.p.x - self.r <= 0:
            self.velocityVec.x = -self.velocityVec.x
            self.setColor(randomColor)
        if self.p.y + self.r >= height or self.p.y - self.r <= 0:
            self.velocityVec.y = -self.velocityVec.y
            self.setColor(randomColor)

    def checkColision(self, other):
        distance = math.sqrt((self.p.x - other.p.x)**2 + (self.p.y - other.p.y)**2)
        if distance <= self.r + other.r+5:
            return True
        else:
            return False

    def bounceOff(self, other):
        if self.checkColision(other):
            self.velocityVec.x = -self.velocityVec.x
            self.velocityVec.y = -self.velocityVec.y
            other.velocityVec.x = -other.velocityVec.x
            other.velocityVec.y = -other.velocityVec.y

    def simulate(self, width, height):
        self.bounce(width, height)
        self.updatePosition()
    
    def AABB(self,other):

        collides = False

        if self.x > other.x:
            collides = True
        
        if collides == True:
            self.xv *= -1

        return collides


        
        



    def draw (self, window):
        #print "hello"
        #print self.p.x, " ", self.p.y, " ", self.r
        pygame.draw.circle(window, self.color, (int(self.p.x),int(self.p.y)),self.r)





