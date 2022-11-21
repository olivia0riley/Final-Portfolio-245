## 
## Taken from Joust game
##

import pygame

class Box(pygame.sprite.Sprite):
    def __init__(self, color, x, y, height, width):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
  
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

        # For ease of copy and pasting code from old projects
        self.rect.x = x
        self.rect.y = y

        self.x = self.rect.x
        self.y = self.rect.y
        self.w = width
        self.h = height