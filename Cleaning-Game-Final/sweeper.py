"""
Derived from code provided at
http://programarcadegames.com/

Edited heavily by: Nolan Kelley
"""

# This file only animates the player
import pygame


from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):

    # -- Attributes

    # This holds all the images for the animated walk left/right of our player
    walking_frames = []

    damage_animation_time = 50

    # -- Methods
    def __init__(self):

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Dictates how long each frame of walk cycle lasts
        self.walking_timer = 0

        # Timer for damage animation
        self.damTimer = 0
        
        # Define all sprites
        standing_sprite = SpriteSheet("Sprite_Sweeper_Standing.png").get_image(0, 0, 100, 158)
        walking_sprite_1 = SpriteSheet("Sprite_Sweeper_Walk_1.png").get_image(0, 0, 100, 141)
        walking_sprite_2 = SpriteSheet("Sprite_Sweeper_Walk_2.png").get_image(0, 0, 100, 172)
        self.empty_hitbox_sprite = SpriteSheet("Sprite_Sweeper_Hitbox_Empty.png").get_image(0, 0, 100, 158)
        
        # Walking loop
        self.walking_frames.append(walking_sprite_1)
        self.walking_frames.append(standing_sprite)
        self.walking_frames.append(walking_sprite_2)
        self.walking_frames.append(standing_sprite)

        # Set the image the player starts with
        self.image = standing_sprite

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        
    def update(self,hitbox):
        """ Position """
        self.rect.x = hitbox.rect.x - 8
        self.rect.y = hitbox.rect.y - 102

        """ Animations """

        # Moving left/right animation
        if hitbox.v.x != 0 or hitbox.v.y != 0:
            #increases the walking timer
            self.walking_timer += 0.01
            frame = (int(self.walking_timer)) % (len(self.walking_frames))
            self.image = self.walking_frames[frame]
            if hitbox.face == False:
                self.image = pygame.transform.flip(self.image, True, False)
           
        # Idle position
        elif hitbox.v.x == 0 and hitbox.v.y == 0:
            #resets the walikng timer
            self.walking_timer = 0
            self.image = self.walking_frames[1]
            if hitbox.face == False:
                 self.image = pygame.transform.flip(self.image, True, False)
        
        # Damage animation
        if hitbox.invincible:
            self.damTimer += 1
            # Shows normal animation half the time, damage frame other half
            if self.damTimer <= self.damage_animation_time/2:
                self.image = self.empty_hitbox_sprite

            if self.damTimer >= self.damage_animation_time:
                self.damTimer = 0
            
        else:
            self.damTimer = 0



if __name__ == "__main__":
    size = (1024,749)
    screen = pygame.display.set_mode(size)
    p = Player()