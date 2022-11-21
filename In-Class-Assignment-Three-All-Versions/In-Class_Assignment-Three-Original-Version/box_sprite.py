import pygame


class Box:

    xv = 0.0
    yv = 0.0

    def __init__ (self, x, y, w, h):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = pygame.color.Color("green")

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)

    def move (self):

        self.rect.x += self.xv;
        self.rect.y += self.yv;

    def set_speed (self, in_xv, in_yv):
        '''
        Changes speed of box object
        '''

        self.xv = in_xv
        self.yv = in_yv

    def set_color (self, color):
        self.color = pygame.color.Color (color)

    def collidesWithAABB(self,other):
        '''
        given another box, return True if we collide, False otherwise
        '''

        hit = True

        if other.rect.x > self.rect.x + self.rect.w:
            hit = False
        if other.rect.y > self.rect.y + self.rect.h:
            hit = False
        if other.rect.x + other.rect.w < self.rect.x:
            hit = False
        if other.rect.y + other.rect.h < self.rect.y:
            hit = False

        if hit == True:
            self.set_color("red")
        else:
            self.set_color("green")


        
    def bounce (self, width, height):
        '''
        Makes box object bouce off walls
        '''

        if self.rect.x + self.rect.w > width:
            self.rect.x = width - self.rect.w
            self.xv *= -1
        elif self.rect.x < 0:
            self.rect.x = 0 + self.rect.w
            self.xv *= -1
        if (self.rect.y + self.rect.h) > height:
            self.rect.y = height - self.rect.h
            self.yv *= -1
        elif self.rect.y < 0:
            self.rect.y = 0 + self.rect.h
            self.yv *= -1


    def simulate (self, width, height):
        self.move()
        self.bounce(width, height)

    
    def get_bbox (self):
        """
        Calculates the screen coordinate of the bounding box.
        """
        return self.rect
        
if __name__ == "__main__":
    b1 = Box(1,2,3,4)