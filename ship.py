import pygame


class Ship:
    def __init__(self, ai):
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.settings = ai.settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False

    def createShip(self):
        self.screen.blit(self.image, self.rect)

    def moveShip(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left == True and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x