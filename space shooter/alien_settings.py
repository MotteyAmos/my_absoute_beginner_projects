import pygame


class Settings:
    def __init__(self):
        # fleem per second
        self.FLP = 60
        self.ship_size = self.ship_width, self.ship_height = 60, 60
        # screen settings
        self.bg_size = self.screen_width, self.screen_height = 900, 500

        #background of the screen settings
        self.bg_img = pygame.image.load("game_background.jpg")
        self.bg_img = pygame.transform.scale(self.bg_img, self.bg_size)
        self.background_x = 0

        # speed of the ship
        self.ship_speed = 7

        #bullet
        self.bullet_speed = 4
        self.bullet_allowed = 7

        #alien
        self.create_new_alien = False
        self.alien_direction = 1
        self.move_alien_x = 1
        self.move_alien_y = False
        self.move_alien_y_increase = 10
        self.alien_size = self.alien_height, self.alien_width = 60, 60
        self.available_column_space = self.screen_width - (self.alien_width * 2)
        self.number_of_aliens = int(self.available_column_space / (self.alien_width * 2))
        self.available_row_space = self.screen_height - (self.ship_height + self.alien_height * 3)
        self.number_of_row_aliens = int(self.available_row_space / (self.alien_height * 2))




