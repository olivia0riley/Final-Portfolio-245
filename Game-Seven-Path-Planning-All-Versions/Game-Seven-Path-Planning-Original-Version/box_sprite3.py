import pygame


class Box:

    xv = 0.0
    yv = 0.0

    def __init__ (self, x, y, w, h):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = pygame.color.Color("brown")


    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)

    
    def move (self):
        self.rect.x += self.xv;
        self.rect.y += self.yv;
    
    def setVelocity(self,newxv,newyv):
        '''New velocity, arguement is a velocity vector'''
        self.xv = newxv
        self.yv = newyv

    def setColor(self,newColor):
        self.color = pygame.color.Color(newColor)



    def collidesWithAABB(self,other):
        '''
        given another box, return True if we collide, False otherwise
        '''
        collides = True 

        sides = "none"

        if other.r > self.rect.x:
            other.xv *= -1

        

        return collides
        

      
        

    def bounce (self, width, height):
    
       if self.rect.x + self.rect.w > width:
          self.rect.x = width - self.rect.w
          self.xv *= -1
        
       elif self.rect.x < 0:
          self.rect.x = 0
          self.xv *= -1

       if self.rect.y < 0:
          self.rect.y = 0
          self.yv *= -1

       elif self.rect.y + self.rect.h > height:
          self.rect.y = height - self.rect.h
          self.yv *= -1


    def simulate (self, width, height):
        self.move()
        self.bounce(width, height)

    
    def get_bbox (self):
        """
        Calculates the screen coordinate of the bounding box.
        """
        return self.rect

        
#if __name__ == "__main__":
 #   b1 = Box(1,2,3,4)
  #  b2 = Box(1,2,3,4)