##
## Author: Kristina Striegnitz
## Author: John Rieffel 
##
## Version: Fall 2022 
##
## A character shows a simple seek behavior that makes it move towards
## a target.
##

import pygame
import random

from vector import Vector
from steering_ball import SteeringBall
from moving_ball_2d import MovingBall
from world import World

def run_game():
    
    ## Initialize the pygame submodules and set up the display window.
    pygame.init()

    width = 1024
    height = 768
    my_win = pygame.display.set_mode((width,height))

    ## setting up the game world
    world = World (width, height)

    ## our character
    x = random.randint(0,width)
    y = random.randint(0,height)

    flock_lst = range(0,50)
    bird_lst = []
    for birds in flock_lst:
        x = random.randint(0,width)
        y = random.randint(0,height)
        r = 10
        m = 1
        color =  pygame.color.Color("darkorange")
        xv = random.randint(1,10)
        yv = random.randint(1,10)
        bird = SteeringBall(x,y,r,m,color,xv,yv)
        bird_lst.append(bird)
        
    print(bird_lst)

    ## the target
    target = MovingBall (150, 175, 20, float('inf'), pygame.color.Color("red"), 0, 0)
    
    ## setting up the clock
    clock = pygame.time.Clock()
    dt = 0
    
    ## The game loop starts here.

    keepGoing = True    
    while (keepGoing):

        dt = clock.tick()
        if dt > 500:
            continue

        ## Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
##            if event.type == pygame.MOUSEBUTTONDOWN:
##                mousepos = pygame.mouse.get_pos()
##                mousepos = Vector(mousepos[0],mousepos[1])
##                target.p = mousepos
        x_lst = []
        y_lst = []

        for beings in bird_lst:
            x_lst.append(beings.p.x)
            y_lst.append(beings.p.y)

        avg_x = sum(x_lst)/len(x_lst)
        avg_y = sum(y_lst)/len(y_lst)


        centroid = MovingBall (avg_x, avg_y, 20,0, pygame.color.Color("green"), 0, 0)



        mousepos = pygame.mouse.get_pos()
        mousepos = Vector(mousepos[0],mousepos[1])
        target.p = mousepos
        
        ## Simulate game world
        target.move (dt, world)
        target.collide_edge (world)

        for items in bird_lst:
            items.steering = []
            #items.seek(target,1.0/30)
            items.arrive(target,1.0/30)
            items.cohesion(1.0/70,centroid)
            items.separation(bird_lst,1.0/30)
            items.align(bird_lst,1/10)
            items.apply_steering()
            items.move(dt, world)
            items.collide_edge(world)
            
    
        
        ## Rendering
        # Draw frame
        my_win.fill(pygame.color.Color("gray14"))

        target.draw(my_win)
        for things in bird_lst:
            things.draw(my_win)

        centroid.draw(my_win)
            
       
    

        # Swap display
        pygame.display.update()

    ## The game loop ends here.

    pygame.quit()


## Start game
run_game()
