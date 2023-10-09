import pygame


class Player:
    """"setting up the player"""
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.transform.scale(pygame.image.load("C:\\Users\\motte\\IdeaProjects\\space shooter\\player_img.png"), settings.ship_size )
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center
        self.image_rect.bottom = self.screen_rect.bottom

        self.move_left = False
        self.move_right = False

    def draw_player(self):
        # draw the player onto the screen
        self.screen.blit(self.image, self.image_rect)

    def move_player(self):
        if self.move_right and self.image_rect.x + self.image_rect.width < self.settings.screen_width:
            self.image_rect.x += self.settings.ship_speed
        elif self.move_left and self.image_rect.x > 0:
            self.image_rect.x -= self.settings.ship_speed



