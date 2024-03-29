import pygame
import sys
import json
from bullet import Bullet
from settings import Settings
from ship import Ship
from alien import Alien
from time import sleep
from gamestats import GameStats
from raindrop import Raindrop
from button import Button
from score import Board

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
        self.stats = GameStats(self)
        self.play_button = Button(self, "Play")
        self.make_difficulty_buttons()
        self.board = Board(self)
        pygame.display.set_caption("Space Invaders")

    """
    Function that runs the game
    """
    def rungame(self):
        while(True):
            self.check_events()
            if self.stats.game_active == True:
                self.ship.moveShip()
                self.update_bullets()
                self.update_alien()

            self.update_screen()

    """
    Responds to the keyboard and mouse presses
    For moving the ship up and down
    """
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.finish_game()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseposition = pygame.mouse.get_pos()
                self.check_play_button(mouseposition)
                self.check_difficulty_buttons(mouseposition)

    """
    Specifically to start a new game with P key
    """
    def start_gameP(self):
        self.stats.reset_stats()
        self.stats.game_active = True

        self.aliens.empty()
        self.bullets.empty()

        self.create_army()
        self.ship.newShip()

        pygame.mouse.set_visible(False)

    def make_difficulty_buttons(self):
        self.easy_button = Button(self, "Easy")
        self.medium_button = Button(self, "Medium")
        self.difficult_button = Button(self, "Difficult")

        self.easy_button.rect.top = (self.play_button.rect.top + 1.5 * self.play_button.rect.height)
        self.easy_button.update_msg_position()

        self.medium_button.rect.top = (self.easy_button.rect.top + 1.5 * self.easy_button.rect.height)
        self.medium_button.update_msg_position()

        self.difficult_button.rect.top = (self.medium_button.rect.top + 1.5 * self.medium_button.rect.height)
        self.difficult_button.update_msg_position()

    def check_difficulty_buttons(self, mouseposition):
        easy_button_clicked = self.easy_button.rect.collidepoint(mouseposition)
        medium_button_clicked = self.medium_button.rect.collidepoint(mouseposition)
        diff_button_clicked = self.difficult_button.rect.collidepoint(mouseposition)
        if easy_button_clicked:
            self.settings.difficulty_level = 'easy'
        elif medium_button_clicked:
            self.settings.difficulty_level = 'medium'
        elif diff_button_clicked:
            self.settings.difficulty_level = 'difficult'

    """
    Specifically for pressing down on the key
    """
    def check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.finish_game()
        elif event.key == pygame.K_w:
            self.shoot()
        elif event.key == pygame.K_p and not self.stats.game_active:
            mouseposition = pygame.mouse.get_pos()
            self.start_gameP()
            self.check_difficulty_buttons(mouseposition)

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
        self.check_collision()

    """
    Creates the fleet of aliens
    """
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

    """
    Helper method to create the fleet of aliens
    """
    def create_alien(self, number, row):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row
        self.aliens.add(alien)

    """
    Updates position of fleet
    """
    def update_alien(self):
        self.fleet_boundary()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.lose_ship()
        self.aliens_at_bottom()
    """
    Checks the boundary of the fleet
    """
    def fleet_boundary(self):
        for alien in self.aliens.sprites():
            if alien.boundary():
                self.change_direction()
                break

    """
    Changes the direction of the fleet
    """
    def change_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_speed
        self.settings.fleet_direction *= -1

    """
    Checks the collision between bullet and alien
    """
    def check_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.gamescore += self.settings.alien_points * len(aliens)
            self.stats.gamescore += self.settings.alien_points
            self.board.set_score()
            self.board.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self.create_army()
            self.settings.adjust_settings()
            self.stats.level += 1
            self.board.prep_level()
    """
    Method to handle when alien hits ship
    """
    def lose_ship(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.board.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self.create_army()
            self.ship.newShip()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    """
    Method to handle when alien hits bottom of screen
    """
    def aliens_at_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.lose_ship()
                break

    def check_play_button(self, mouseposition):
        button_clicked = self.play_button.rect.collidepoint(mouseposition)
        if button_clicked and not self.stats.game_active:
            self.settings.initsettings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.aliens.empty()
            self.bullets.empty()
            self.create_army()
            self.ship.newShip()
            pygame.mouse.set_visible(False)
            self.board.display_score()
            self.board.prep_level()
            self.board.prep_ships()
    """
    Updates the images on the screen and flips the screen
    """
    def update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.ship.createShip()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.board.display_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.difficult_button.draw_button()
        pygame.display.flip()

    def finish_game(self):
        save_high_score = self.stats.save_high_scores()
        if self.stats.highscore > save_high_score:
            with open('high_score.json', 'w') as f:
                json.dump(self.stats.highscore, f)

        sys.exit()
if __name__ == '__main__':
    ai = AlienGame()
    ai.rungame()
