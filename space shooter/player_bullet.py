import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """" a class of bullet"""
    def __init__(self, settings, screen, player):
        self.settings = settings
        self.screen = screen
        self.player = player
        self.image = pygame.transform.scale(pygame.image.load('C:\\Users\\motte\\IdeaProjects\\space shooter\\bullet_img.png'), (50, 50))
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = self.player.image_rect.centerx
        self.image_rect.top = self.player.image_rect.top

    def create_bullet(self):
        self.screen.blit(self.image, self.image_rect)

    def update(self):
        self.image_rect.y -= self.settings.bullet_speed
        self.create_bullet()

