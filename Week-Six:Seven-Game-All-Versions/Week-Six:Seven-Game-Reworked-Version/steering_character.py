
import pygame
from moving_ball_2d import MovingBall
from vector import Vector
import random
import math


class BeakBall (MovingBall):

    beak_tip = Vector(0,20)
    max_acceleration = 200.0

    speedlimit = Vector(500,500)

    steering = []

    def draw (self, window):
        pygame.draw.circle(window, self.color, (int(self.p.x),int(self.p.y)),self.r)
        speed = self.v.length()
        if speed != 0:
            self.beak_tip = self.v.normalize() * 20
        pygame.draw.line(window,self.color,(int(self.p.x),int(self.p.y)),(self.p.x+self.beak_tip.x,self.p.y+self.beak_tip.y), 3)

        for vec in self.steering:
            arrowvec = Vector(0,0)
            arrowvec = arrowvec + vec
            arrowvec = arrowvec + self.p
            pygame.draw.line(window,pygame.color.Color("red"),(int(self.p.x),int(self.p.y)),(arrowvec.x,arrowvec.y),2)


    def __str__ (self):
        return str(self.p)+", "+str(self.v)+", "+str(self.a) 


    def apply_steering (self):
        for s in self.steering:
            self.v = self.v + s


    def wander(self,weight):
        '''
        pick a random target some radius away from me
        and seek it
        '''

        x_target = random.randint(0,1024/2)
        y_target = random.randint(0,768)

        target = Vector(x_target,y_target)

        #find difference between my location and target location 
        desired_direction = (target - self.p).normalize()
        #multiply direction by max speed
        max_speed = self.speedlimit.length()
        desired_velocity = desired_direction * max_speed
        ## first find the "error" between current velocity and desired velocity, and then multiply that error 
        ## by the weight, and then add it to steering inputs
        self.steering += [(desired_velocity - self.v)*weight]
        

    def loop(self,weight):
        '''
        agent should move in a corkskrew motion
        '''
        print("loop: implement me")

        my_velocity = self.v

        if self.v.length() < 1:

            x_component = random.random()
            y_component = random.random()

            self.v = Vector(x_component,y_component)

            self.v.normalize()

            max_speed = self.speedlimit.length() * 0.0001

            self.v = max_speed * self.v


        perp_velocity = Vector(-self.v.y,self.v.x)

        #find difference between my location and target location 
        desired_direction = perp_velocity
        #multiply direction by max speed
        max_speed = self.speedlimit.length()
        desired_velocity = desired_direction * max_speed
        ## first find the "error" between current velocity and desired velocity, and then multiply that error 
        ## by the weight, and then add it to steering inputs
        self.steering += [(desired_velocity)*weight] 



    def freeze(self):
        '''
        stop, hammertime
        '''
        self.v = 0

    def freeze(self):
        self.v.y = 0 
        self.v.x = 0

        print("freeze: implement me")
        



