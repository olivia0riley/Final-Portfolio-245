"""

Author: John Rieffel

Based off of 

Simpson College Computer Science Material

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame

from player import Player
from simple_platform import Box
from spritesheet_functions import SpriteSheet

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    HEIGHT = 480
    WIDTH = 640
    size = [WIDTH,HEIGHT]
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("Flame_Background.png")
    sound = pygame.mixer.Sound("Jumping_sound.wav")

    pygame.display.set_caption("demo with sprite sheets")

    active_sprite_list = pygame.sprite.Group()
    # Create the player

    
    player = Player()
    platform = Box(pygame.color.Color("black"),50,100) 
    platform2 = Box(pygame.color.Color("black"),50,100) 

    platform.rect.x = 400
    platform.rect.y = HEIGHT - platform.rect.h - 20

    platform2.rect.x = 175
    platform2.rect.y = HEIGHT - platform.rect.h - 20

    # Create all the levels

    player.rect.x = 100 
    player.rect.y = HEIGHT - player.rect.height
    active_sprite_list.add(player,platform,platform2)
    

    #Loop until the user clicks the close button.
    done = False

    # Storing original needed jump factors 

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                    sound.play()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: 
                    player.stop()
                if event.key == pygame.K_RIGHT:
                    player.stop()
        

        # Update the player.
        active_sprite_list.update()

        collide = False
        if pygame.sprite.collide_rect(player,platform):
            collide = True
        if collide == True: 
            player.rect.y = platform.rect.y - player.rect.h
        if pygame.sprite.collide_rect(player,platform2):
            collide = True
        if collide == True: 
            player.rect.y = platform2.rect.y - player.rect.h


        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        #current_level.draw(screen)
        screen.fill(pygame.color.Color("gray14")) 
        screen.blit(background,(0,0))
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
