# Olivia Riley
# Game One - Part 3
# September 12, 2022

import pygame
import random

# Creating funciton 

def night_sky():
    '''Displays night sky'''
    
    # Opening and setting up the display window
    pygame.init()

    width = 600
    height = 480
    my_win = pygame.display.set_mode((width, height))

     # Initializing "stars"
    num_stars = range (1,50)
    big_lst = []
    for stars in num_stars:
        little_lst = []
        x = random.randint(0,width)
        y = random.randint(0,height)
        radius = random.randint(1,4)
        little_lst.append(x)
        little_lst.append(y)
        little_lst.append(radius)
        big_lst.append(little_lst)


    # Game loop
    keep_going = True
    while (keep_going):

        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False


        my_win.fill(pygame.color.Color("black"))

        # Drawing the "stars"

        for lists in big_lst:
            pygame.draw.circle(my_win, pygame.color.Color("yellow"), ((lists[0]), (lists[1])), lists[2])
        
        # Swapping display

        pygame.display.update()

    # Ending game loop
    pygame.quit()

# Calling funciton

night_sky()
