##
## Author: Kristina Striegnitz
##
## Version: Fall 2011 
##
## A finite state controlled character wanders around the
## screen. While it is on the green part it wanders slowing; when it
## is on the red it starts running.
##

import pygame
import random

from vector import Vector
from fsm_character import FSMBeakBall
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

    instances = range(0,10)
    lst = []

    for birds in instances:
        r = random.randint(0,255)
        b = random.randint(0,255)
        g = random.randint(0,255)
        color = pygame.Color(r, g, b)
        x = random.randint(0,width)
        y = random.randint(0,height)
        r = 10
        m = 1
        xv = 0
        yv = 0
        birds = FSMBeakBall (x, y, r, m, color, xv, yv)
        lst.append(birds)
   
    #c = FSMBeakBall (x, y, 10, 1, pygame.color.Color("darkorange"), 0, 0)

    ## a dictionary to remember which keys are pressed
    keymap = {}

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


        ## Simulate game world

        for birdies in lst:
            birdies.fsm.update(world)
            birdies.execute_actions ()
            birdies.move(dt, world)
            birdies.collide_edge (world)

        
        ## Rendering
        # Draw frame
        pygame.draw.rect (my_win, pygame.color.Color("green"), (0,0,width/2,height))
        pygame.draw.rect (my_win, pygame.color.Color("red"), (width/2,0,width/2,height))

        for items in lst:
            items.draw(my_win)

        print(lst)

        # Swap display
        pygame.display.update()

    ## The game loop ends here.

    pygame.quit()


## Start game
run_game()
