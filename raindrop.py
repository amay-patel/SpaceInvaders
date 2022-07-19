import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """
    Raindrop class to use for the game background
    """
    def __init__(self, ai):
        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

    """
    Checks to see if the rain has dropped below the screen
    """
    def check_disappeared(self):
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    """
    Move the raindrop down the screen
    """
    def update(self):
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y