
import pygame
from moving_ball_2d import MovingBall
from vector import Vector


class SteeringBall (MovingBall):

    beak_tip = Vector(0,20)

    speedlimit = Vector(500,500)

    # All steering inputs
    steering = []

    def draw (self, window):
        # draw the body
        pygame.draw.circle(window, self.color, (int(self.p.x),int(self.p.y)),self.r)
        # draw the beak
        speed = self.v.length()
        if speed != 0:
            self.beak_tip = self.v.normalize() * 20
        pygame.draw.line(window,self.color,(int(self.p.x),int(self.p.y)),(self.p.x+self.beak_tip.x,self.p.y+self.beak_tip.y), 3)

        if self.drawvec:
            for vec in self.steering:
                arrowvec = Vector(0,0)
                arrowvec = arrowvec + vec
                arrowvec = arrowvec + self.p
                pygame.draw.line(window,pygame.color.Color("red"),(int(self.p.x),int(self.p.y)),(arrowvec.x,arrowvec.y),2)


    def __str__ (self):
        return str(self.p)+", "+str(self.v)+", "+str(self.a) 


    def apply_steering (self):
        ## add all steering inputs to current velocity vector
        for s in self.steering:
            self.v += s


    def seek (self, target, weight):

        #find difference between my location and target location 
        desired_direction = (target.p - self.p).normalize()
        #multiply direction by max speed
        max_speed = self.speedlimit.length()
        desired_velocity = desired_direction * max_speed
        ## first find the "error" between current velocity and desired velocity, and then multiply that error 
        ## by the weight, and then add it to steering inputs
        self.steering += [(desired_velocity - self.v)*weight]

        pass

    def arrive (self,target,weight):
        '''Builds on the seek method'''
        desired_direction = (target.p - self.p).normalize()
       
        max_speed = self.speedlimit.length()
        desired_velocity = desired_direction * max_speed
        
        distance_vector = target.p - self.p
        length = distance_vector.length()
        max_speed = self.speedlimit.length()

        if length <= 4 * (target.r + self.r):
            percent_speed = length / (4 * (target.r + self.r)) 
            desired_velocity = (max_speed * percent_speed) * desired_direction
            self.steering += [(desired_velocity - self.v)*weight]
        else: 
            self.seek(target,weight)

    def flee (self,target,weight):
        '''flees from given radius'''
        desrired_direction = (target.p - self.p).normalize()
        max_speed = self.speedlimit.length()
        desired_velocity = max_speed
        
        distance_vector = target.p - self.p
        length = distance_vector.length()
        max_speed = self.speedlimit.length()

        if length <= 4 * (target.r + self.r):
            change_direction = -1
            desired_direction = (target.p - self.p).normalize()
            desired_velocity = desired_direction * (max_speed * change_direction)
            self.steering += [(desired_velocity - self.v)*weight]
        else: 
            self.seek(target,weight)

    def cohesion (self, weight, centroid):
      
        desired_direction = (centroid.p - self.p).normalize()
    
        max_speed = self.speedlimit.length()
        desired_velocity = desired_direction * max_speed
   
        self.steering += [(desired_velocity - self.v)*weight]

    def separation (self, flocklst, weight):

        velocity_adjustment = Vector(0,0)
        radius_bird = 4 * (self.r)

        for other_bird in flocklst:

            # make sure other bird is not self

            # calculate distance to other bird 
            # if bird is too close, velocty_adjustment (flee from other bird)

            if other_bird != self:

                distance_vector = other_bird.p - self.p

                length = distance_vector.length() 

                if length <= radius_bird:
                    max_speed = self.speedlimit.length()
                    desired_direction = (other_bird.p - self.p).normalize()
                    desired_velocity = desired_direction * (max_speed * -1)
                    self.steering += [(desired_velocity - self.v)*weight]


    def align (self,flocklst,weight):
        
        # calculate the average of the velocity of all of the other boids in the flock not including itself
        # calculate the difference between the average velocity and our boids velocity 
        # adjust steering 
        # invoke after separation()

        sum_vel = Vector(0,0)

        for other_bird in flocklst:

            if other_bird != self:

                sum_vel += other_bird.v

        sum_vel = sum_vel/len(flocklst)

        self.steering += [(sum_vel)*weight]




        










            

