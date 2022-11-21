## 
## Authors: Nolan Kelley, Matt Adner, Olivia Riley
##

import pygame
import random
from vector import Vector

# For start screen
from alt_screen import AltScreen
from start_button import BobSprite

# For running state
from levels import Levels
from healthbar  import Healthbar
from sweeper import Player
from sweeper_hitbox import PlayerHitbox
from broom import Broom

# For end screens
from banner import Banner


def run_game(playthrough):
    ## Initialize the pygame submodules and set up the display window.
    pygame.init()
    
    # Value for testing
    testval = 1
    skip = False
    debbugMode = False

    # Set variables
    starthealth = 3
    setup = False
    timeAftDeath = 0

    # Create window
    width = 1024
    height = 749
    screen = pygame.display.set_mode([width,height])


    # Create player stuff
    player = Player()
    pHitbox = PlayerHitbox(starthealth)
    broom = Broom(player)
    healthbar = Healthbar(0, height-116, pHitbox.health)

    # Create Start State stuff
    sScreen = AltScreen(width,height,"start")
    sButton = BobSprite(363,400,2,"start_button")

    # Create Pause State stuff
    pScreen = AltScreen(width,height,"pause")
    pOrbs = BobSprite(0,0,2,"pause_orbs")

    # Create Win State stuff
    wScreen = AltScreen(width,height,"win")
    paButton = BobSprite(100,600,2,"play_again_button")
    qButton = BobSprite(600,585,-2,"quit_button")
    

    # Create end game stuff
    lose_banner = Banner(width)

    # Create Running State stuff
    #For drawing the player and broom
    pdraw = pygame.sprite.Group()
    pdraw.add(player)
    pdraw.add(broom)
    #For drawing healthbar
    hbdraw = pygame.sprite.Group()
    hbdraw.add(healthbar)
    #For drawing lose banner
    lbdraw = pygame.sprite.Group()
    lbdraw.add(lose_banner)

    #For drawing player hitbox (testing)
    pHitboxdraw = pygame.sprite.Group()
    pHitboxdraw.add(pHitbox)

    

    # Place player
    pHitbox.rect.x = width/2 - 50
    pHitbox.rect.y = height/1.5

    # All levels in the game
    levels = Levels(width,height,0,0) # You can change starting level/room here for testing

    ## a dictionary to remember which keys are pressed
    keymap = {}

    ## setting up the clock
    clock = pygame.time.Clock()
    dt = 0

    # Sets current level
    cLevel = levels.levels[levels.icl]
    # Sets current room
    cRoom = cLevel[0]


    ## Make sprite groups (for drawing)

    # First room
    bdraw = pygame.sprite.Group()
    bdraw.add(cRoom)

    # Roombas in first room
    rdraw = pygame.sprite.Group()
    for r in cRoom.roombas:
        rdraw.add(r)

    # Messes in first room
    mdraw = pygame.sprite.Group()
    for m in cRoom.messes:
        mdraw.add(m)
    
    # Start Screen
    ssdraw = pygame.sprite.Group()
    ssdraw.add(sScreen)
    #Start Button
    sbdraw = pygame.sprite.Group()
    sbdraw.add(sButton)

    # Pause Screen
    psdraw = pygame.sprite.Group()
    psdraw.add(pScreen)
    #Pause Orbs
    podraw = pygame.sprite.Group()
    podraw.add(pOrbs)

    # Win Screen
    wsdraw = pygame.sprite.Group()
    wsdraw.add(wScreen)
    

    #Play Again and Quit buttons
    wbdraw = pygame.sprite.Group()
    wbdraw.add(paButton)
    wbdraw.add(qButton)

    #Quit button

    # Sets the state the game is in
    gameState = "start_screen"

    

## The game loop starts here.
    keepGoing = True
    while (keepGoing):
        
        dt = clock.tick()
        if dt > 500:
            continue



    ## START STATE STARTS HERE 
        while (gameState == "start_screen"):
            dt = clock.tick()
            if dt > 500:
                continue
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                    gameState = "end"
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()    
                    if mouse_x >= sButton.rect.x and mouse_x <= sButton.rect.x+sButton.rect.w and mouse_y >= sButton.rect.y and mouse_y <= sButton.rect.y+sButton.rect.h:
                        gameState = "pause"
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        debbugMode = True
                        gameState = "running"
                    
            if setup == True:
                # Place player
                pHitbox.rect.x = width/2 - 50
                pHitbox.rect.y = height/1.5
                
                # Sets stats
                pHitbox.score = 0

                #print("create level object")
                

                 # All levels in the game
                levels = Levels(width,height,0,0)

                # Sets current level
                cLevel = levels.levels[levels.icl]
                # Sets current room
                cRoom = cLevel[0]


                ## Make sprite groups (for drawing)

                # First room
                bdraw = pygame.sprite.Group()
                bdraw.add(cRoom)

                # Roombas in first room
                rdraw = pygame.sprite.Group()
                for r in cRoom.roombas:
                    rdraw.add(r)

                # Messes in first room
                mdraw = pygame.sprite.Group()
                for m in cRoom.messes:
                    mdraw.add(m)
                
                #print("setup = false")
                # Stop setup
                setup = False

            
            ## Simulate game world
            sButton.bob()

            ## Rendering
            # Draw Background
            screen.fill(pygame.color.Color("black"))

            # Draw Start Screen
            ssdraw.draw(screen)

            # Draw Start Button
            sbdraw.draw(screen)

            # Swap display
            pygame.display.update()
       


    ## PAUSE STATE STARTS HERE 
        while (gameState == "pause"):
            dt = clock.tick()
            if dt > 500:
                continue
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                    gameState = "end"
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameState = "running"
                
                #So if you can lift a movement key while paused
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:     
                        pHitbox.stop_left()
                    if event.key == pygame.K_d:
                        pHitbox.stop_right()
                    if event.key == pygame.K_w:    
                        pHitbox.stop_up()
                    if event.key == pygame.K_s:
                        pHitbox.stop_down()
                    
            
            ## Simulate game world
            pOrbs.bob()

            ## Rendering
            # Draw Background
            screen.fill(pygame.color.Color("black"))

            # Draw Start Screen
            psdraw.draw(screen)

            # Draw Start Button
            podraw.draw(screen)

            
            # Swap display
            pygame.display.update()
        
        

    ## RUNNUNG STATE STARTS HERE
        while (gameState == "running"):
            dt = clock.tick()
            if dt > 500:
                continue


            ## Handle events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                    gameState = "end"

                if event.type == pygame.MOUSEBUTTONDOWN and timeAftDeath > 400:
                    mouse_x, mouse_y = pygame.mouse.get_pos() 
                    # Starts game again
                    if mouse_x >= paButton.rect.x and mouse_x <= paButton.rect.x+paButton.rect.w and mouse_y >= paButton.rect.y and mouse_y <= paButton.rect.y+paButton.rect.h:
                        keepGoing = False
                        gameState = "end"
                        # Set caption
                        pygame.display.set_caption('Oof')
                        run_game(playthrough+1)
                    # Ends game
                    if mouse_x >= qButton.rect.x and mouse_x <= qButton.rect.x+qButton.rect.w and mouse_y >= qButton.rect.y and mouse_y <= qButton.rect.y+qButton.rect.h:
                        keepGoing = False
                        gameState = "end"
            
                if event.type == pygame.KEYDOWN and pHitbox.health > 0:
                    #state change
                    if event.key == pygame.K_p:
                        gameState = "pause"
                    #movement
                    if event.key == pygame.K_a:
                        pHitbox.go_left()
                    if event.key == pygame.K_d:
                        pHitbox.go_right()
                    if event.key == pygame.K_w:
                        pHitbox.go_up()
                    if event.key == pygame.K_s:
                        pHitbox.go_down()
                    #cleaning
                    if event.key == pygame.K_SPACE:
                        pHitbox.cleaning = True
                    
                    if debbugMode:
                        #testing
                        if event.key == pygame.K_t: #shows hitboxes of player and roombas
                            testval *= -1
                        if event.key == pygame.K_i: #gives player too many iframes
                            pHitbox.iframes += 1000000000
                        if event.key == pygame.K_m: #gives player too many mushframes
                            pHitbox.mushframes += 1000000000
                        if event.key == pygame.K_h: #damages player
                            pHitbox.health -= 1
                        if event.key == pygame.K_MINUS: #slows player
                            pHitbox.pspeed -= 1
                            print(pHitbox.pspeed)
                        if event.key == pygame.K_EQUALS: #speeds up player
                            pHitbox.pspeed += 1
                            print(pHitbox.pspeed)
                        if event.key == pygame.K_e: #skips current room
                            skip = True
                    
                if event.type == pygame.KEYUP:
                    #stop movement
                    if event.key == pygame.K_a:     
                        pHitbox.stop_left()
                    if event.key == pygame.K_d:
                        pHitbox.stop_right()
                    if event.key == pygame.K_w:    
                        pHitbox.stop_up()
                    if event.key == pygame.K_s:
                        pHitbox.stop_down()
                    #stop cleaning
                    if event.key == pygame.K_SPACE:
                        pHitbox.cleaning = False

            
            ## Simulate game world

            # Simulate player
            if testval == -1:
                pHitbox.invincible = True
            player.update(pHitbox)          #animate
            pHitbox.simulate(cRoom)         #physics
            if pHitbox.health > 0:
             broom.update(player, pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])#, player.p.x, player.p.y)
            healthbar.update(pHitbox.health)
            
            # Simulate Roombas
            for r in cRoom.roombas:    
                r.simulate(dt,pHitbox,broom,cRoom)
                if r.i == 0 and r.check_got(pHitbox):
                    if pHitbox.health > 0:
                        pHitbox.score += 3      # Increase score
                    rdraw.remove(r)
                    cRoom.roombas.remove(r)
                r.update()

            # Simulate Messes
            if pHitbox.health > 0:
                for m in cRoom.messes:

                    if m.pTimer >= 300:
                        pHitbox.score += 5      # Increase score
                        mdraw.remove(m)
                        cRoom.messes.remove(m)
                    #print(m.pTimer)
                    
                    else:
                        for r in cRoom.roombas:
                            if m.rTimerList[r.cTimeIndex] >= 300:
                                pHitbox.score -= 5      # Decrease score
                                mdraw.remove(m)
                                cRoom.messes.remove(m)


            ## Rendering
            # Draw Background
            screen.fill(pygame.color.Color("black"))

            # Draw Room
            bdraw.draw(screen)

            # Draw Walls (for testing)
            #cRoom.walls.draw(screen)

            # Draw Messes
            if len(mdraw) > 0:
                mdraw.draw(screen)

            # Draw Roombas
            rdraw.draw(screen)

            # Draw Roomba balls (for testing)
            for r in cRoom.roombas:
                if testval == -1:
                    r.drawBall(screen)
            
            # Draw Player and broom
            pdraw.draw(screen)

            # Draw hitbox (for testing)
            #pXitboxdraw.draw(screen)

            #Checks if player dies
            if pHitbox.health <= 0:
                
                # Draw and animate losebanner
                lose_banner.drop()
                lbdraw.draw(screen)

                timeAftDeath += 1
                # Draw Play Again and Quit Buttons
                if timeAftDeath > 400:
                    wbdraw.draw(screen) 
                

            # Draw Healthbar
            hbdraw.draw(screen)

            #Checks if beat level
            if cRoom.beat_level() or skip:
                
                skip = False

                # Updates level index
                levels.icl += 1

                # Gives player iframes
                pHitbox.iframes = 100

                # Checks if there is a next level
                if len(levels.levels) > levels.icl:
               
                    # Sets current level
                    cLevel = levels.levels[levels.icl]
                    # Sets current room
                    cRoom = cLevel[levels.icr]

                    # Allows for drawing background of room
                    bdraw = pygame.sprite.Group()
                    bdraw.add(cRoom)

                    # Allows for drawing Roombas in room
                    rdraw = pygame.sprite.Group()
                    for r in cRoom.roombas:
                        rdraw.add(r)

                    # Allows for drawing messes in room
                    mdraw = pygame.sprite.Group()
                    for m in cRoom.messes:
                        mdraw.add(m)
                else:
                    
                    # Adds multiple of health to score and displays final value
                    pHitbox.score += (pHitbox.health-1) * 10
                    pygame.display.set_caption('Final Score: ' + str(int(pHitbox.score*10)/10.0) + '0')
                    if debbugMode: 
                        pygame.display.set_caption('Final Score: ' + str(int(pHitbox.score*10)/10.0) + '0, but also you cheated.')
                    gameState = "win"
            
            if gameState != "win":
                # Display score and level
                if debbugMode:
                    if timeAftDeath > 0:
                        pygame.display.set_caption('Final Score: ' + str(int(pHitbox.score*10)/10.0) + '0' + '   ' + 'Level: ' + str(levels.icl) + ' |Debbug Mode|')
                    else:
                        pygame.display.set_caption('Score: ' + str(int(pHitbox.score*10)/10.0) + '0' + '   ' + 'Level: ' + str(levels.icl) + ' |Debbug Mode|')
                else:
                    if timeAftDeath > 0:
                        pygame.display.set_caption('Final Score: ' + str(int(pHitbox.score*10)/10.0) + '0' + '   ' + 'Level: ' + str(levels.icl))
                    else:
                        pygame.display.set_caption('Score: ' + str(int(pHitbox.score*10)/10.0) + '0' + '   ' + 'Level: ' + str(levels.icl))
            
            
            # Swap display
            pygame.display.update()
    
    ## WIN STATE STARTS HERE 
        while (gameState == "win"):
            dt = clock.tick()
            if dt > 500:
                continue
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                    gameState = "end"
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()    
                    # Starts game again
                    if mouse_x >= paButton.rect.x and mouse_x <= paButton.rect.x+paButton.rect.w and mouse_y >= paButton.rect.y and mouse_y <= paButton.rect.y+paButton.rect.h:
                        keepGoing = False
                        gameState = "end"
                        # Set caption
                        pygame.display.set_caption('Welcome back!')
                        if playthrough > 30:
                            pygame.display.set_caption('You really like this game, huh?')
                        if playthrough == 420:
                            pygame.display.set_caption('You really did this for the bit, huh?')
                        if playthrough > 9999:
                            pygame.display.set_caption('Jesus dude. Take a break, maybe.')
                        
                        run_game(playthrough+1)
                    # Ends game
                    if mouse_x >= qButton.rect.x and mouse_x <= qButton.rect.x+qButton.rect.w and mouse_y >= qButton.rect.y and mouse_y <= qButton.rect.y+qButton.rect.h:
                        keepGoing = False
                        gameState = "end"
                    
            
            ## Simulate game world
            paButton.bob()
            qButton.bob()

            ## Rendering
            # Draw Background
            screen.fill(pygame.color.Color("black"))

            # Draw Win Screen
            wsdraw.draw(screen)

            # Draw Play Again and Quit Buttons
            wbdraw.draw(screen)

            
            # Swap display
            pygame.display.update()

    ## The game loop ends here.

    pygame.quit()


## Start game
run_game(0)
