import pygame
import random


class Alien:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        for alien_number in range(1, 4):
            self.image = pygame.transform.scale(
                pygame.image.load("C:\\Users\\motte\\IdeaProjects\\space shooter\\aliens\\alien" +
                                  str(random.randint(1, 3)) + ".png"),
                self.settings.alien_size
            )
        self.image_rect = self.image.get_rect()

        self.image_rect.y = self.image_rect.height

    def create_alien(self):
        self.screen.blit(self.image, self.image_rect)



