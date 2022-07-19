import pygame
import sys
from bullet import Bullet
from settings import Settings
from ship import Ship
from alien import Alien

"""
Class for the overall game
"""
class AlienGame:

    """
    Settings that we import from settings.py to set window size and caption
    """
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_army()
        pygame.display.set_caption("Space Invaders")

    """
    Function that runs the game
    """
    def rungame(self):
        while(True):
            self.check_events()
            self.ship.moveShip()
            self.update_bullets()
            self.update_screen()

    """
    Responds to the keyboard and mouse presses
    For moving the ship up and down
    """
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)

    """
    Specifically for pressing down on the key
    """
    def check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_w:
            self.shoot()

    """
    Specifically for pressing up on the key
    """
    def check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    """
    Shoots bullet
    """
    def shoot(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    """
    Update position of bullets and manages old bullets by deleting
    """
    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    """
    Updates the images on the screen and flips the screen
    """
    def update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.ship.createShip()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def create_army(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_aliens = self.settings.screen_length - (2 * alien_width)
        number_of_aliens = available_space_aliens // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space // (2 * alien_height)
        for row in range(number_rows):
            for number in range(number_of_aliens):
                self.create_alien(number, row)

    def create_alien(self, number, row):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row
        self.aliens.add(alien)

if __name__ == '__main__':
    ai = AlienGame()
    ai.rungame()