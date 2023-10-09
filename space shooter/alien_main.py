import pygame
from pygame import mixer
from alien_settings import Settings
import alien_function as fun
from player import Player
from alien import Alien


def run_game():
    """"initialize the functionality of the game"""
    pygame.init()

    settings = Settings()
    #setting the screen
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    #clock
    CLOCK = pygame.time.Clock()

    # player object
    player = Player(screen, settings)
    #bullet
    bullets = []
    #aliens
    aliens = []
    # create a background music
    mixer.music.load("background_sound.mp3")
    mixer.music.play(-1)

    while True:
        fun.run_event(player, settings, bullets, screen)



        fun.update_screen(CLOCK, screen, settings, player, bullets, aliens)





if __name__ == "__main__":
    run_game()



