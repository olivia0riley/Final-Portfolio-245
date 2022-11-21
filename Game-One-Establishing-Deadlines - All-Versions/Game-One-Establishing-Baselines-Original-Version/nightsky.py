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
    x = random.randint(0,600)
    y = random.randint(0,480)
    radius = 1
    color = pygame.color.Color("Yellow")

    x2 = random.randint(0,600)
    y2 = random.randint(0,480)
    radius2 = 2
    color = pygame.color.Color("Yellow")

    x3 = random.randint(0,600)
    y3 = random.randint(0,480)
    radius3 = 3
    color = pygame.color.Color("Yellow")

    x4 = random.randint(0,600)
    y4 = random.randint(0,480)
    radius4 = 4
    color = pygame.color.Color("Yellow")

    x5 = random.randint(0,600)
    y5 = random.randint(0,480)
    radius5 = 1
    color = pygame.color.Color("Yellow")

    x6 = random.randint(0,600)
    y6 = random.randint(0,480)
    radius6 = 2
    color = pygame.color.Color("Yellow")

    x7 = random.randint(0,600)
    y7 = random.randint(0,480)
    radius7 = 3
    color = pygame.color.Color("Yellow")

    x8 = random.randint(0,600)
    y8 = random.randint(0,480)
    radius8 = 4
    color = pygame.color.Color("Yellow")

    x9 = random.randint(0,600)
    y9 = random.randint(0,480)
    radius9 = 1
    color = pygame.color.Color("Yellow")

    x10 = random.randint(0,600)
    y10 = random.randint(0,480)
    radius10 = 2
    color = pygame.color.Color("Yellow")

    x11 = random.randint(0,600)
    y11 = random.randint(0,480)
    radius11 = 3
    color = pygame.color.Color("Yellow")

    x12 = random.randint(0,600)
    y12 = random.randint(0,480)
    radius12 = 4
    color = pygame.color.Color("Yellow")

    x13 = random.randint(0,600)
    y13 = random.randint(0,480)
    radius13 = 1
    color = pygame.color.Color("Yellow")

    x14 = random.randint(0,600)
    y14 = random.randint(0,480)
    radius14 = 2
    color = pygame.color.Color("Yellow")

    x15 = random.randint(0,600)
    y15 = random.randint(0,480)
    radius15 = 3
    color = pygame.color.Color("Yellow")

    x16 = random.randint(0,600)
    y16 = random.randint(0,480)
    radius16 = 4
    color = pygame.color.Color("Yellow")

    x17 = random.randint(0,600)
    y17 = random.randint(0,480)
    radius17 = 1
    color = pygame.color.Color("Yellow")

    x18 = random.randint(0,600)
    y18 = random.randint(0,480)
    radius18 = 2
    color = pygame.color.Color("Yellow")

    x19 = random.randint(0,600)
    y19 = random.randint(0,480)
    radius19 = 3
    color = pygame.color.Color("Yellow")

    x20 = random.randint(0,600)
    y20 = random.randint(0,480)
    radius20 = 4
    color = pygame.color.Color("Yellow")

    # Game loop
    keep_going = True
    while (keep_going):

        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False


        my_win.fill(pygame.color.Color("black"))

        # Drawing the "stars"
        
        pygame.draw.circle(my_win, color, (x, y), radius)

        pygame.draw.circle(my_win, color, (x2, y2), radius2)

        pygame.draw.circle(my_win, color, (x3, y3), radius3)

        pygame.draw.circle(my_win, color, (x4, y4), radius4)

        pygame.draw.circle(my_win, color, (x5, y5), radius5)

        pygame.draw.circle(my_win, color, (x6, y6), radius6)

        pygame.draw.circle(my_win, color, (x7, y7), radius7)

        pygame.draw.circle(my_win, color, (x8, y8), radius8)

        pygame.draw.circle(my_win, color, (x9, y9), radius9)

        pygame.draw.circle(my_win, color, (x10, y10), radius10)

        pygame.draw.circle(my_win, color, (x11, y11), radius11)

        pygame.draw.circle(my_win, color, (x12, y12), radius12)

        pygame.draw.circle(my_win, color, (x13, y13), radius13)

        pygame.draw.circle(my_win, color, (x14, y14), radius14)

        pygame.draw.circle(my_win, color, (x15, y15), radius15)

        pygame.draw.circle(my_win, color, (x16, y16), radius16)

        pygame.draw.circle(my_win, color, (x17, y17), radius17)

        pygame.draw.circle(my_win, color, (x18, y18), radius18)

        pygame.draw.circle(my_win, color, (x19, y19), radius19)

        pygame.draw.circle(my_win, color, (x20, y20), radius20)

        # Swapping display

        pygame.display.update()
    # Ending game loop
    pygame.quit()

# Calling funciton

night_sky()
