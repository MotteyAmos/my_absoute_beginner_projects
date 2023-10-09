import pygame
import sys
from pygame import mixer
from player_bullet import Bullet
from alien import Alien



def key_pressed(event, player, settings, bullets, screen):
    """" what to do when a key is pressed on the keyboard"""
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_LEFT:
        player.move_left = True
    elif event.key == pygame.K_RIGHT:
        player.move_right = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) <= settings.bullet_allowed:
            bullet = Bullet(settings, screen, player)
            bullets.append(bullet)
            bullet_sound = mixer.Sound("laser.wav")
            bullet_sound.play()


def key_released(event, player):
    """" what to do when a key on the keyboard has been released"""
    if event.key == pygame.K_LEFT:
        player.move_left = False
    elif event.key == pygame.K_RIGHT:
        player.move_right = False


def run_event(player, settings, bullets, screen):
    """"run the keyboard event and mouse event on screen"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_pressed(event, player, settings, bullets, screen)
        elif event.type == pygame.KEYUP:
            key_released(event, player)


def background_loop(settings, screen):
    """"animating the background image"""
    screen.blit(settings.bg_img, (settings.background_x, 0))
    screen.blit(settings.bg_img, (settings.background_x + settings.screen_width, 0))

    if int(settings.background_x) == -settings.screen_width:
        screen.blit(settings.bg_img, (settings.background_x + settings.screen_width, 0))
        settings.background_x = 0

    settings.background_x -= 0.1


def create_alien_row(settings, screen, aliens):
    """" create a row of aliens"""
    width = settings.alien_width
    height = settings.alien_height
    # when the float decimal of settings.number_of_aliens is greater than 1

    for alien_row_number in range(settings.number_of_row_aliens):
        for alien_number in range(settings.number_of_aliens + 1):
            alien = Alien(settings, screen)
            alien.image_rect.x = width + (width * 2 * alien_number)
            alien.image_rect.y = height + (height * 2 * alien_row_number)
            aliens.append(alien)


def update_aliens(aliens, settings):
    """" update the aliens to move side and up and down on the screen"""
    for alien in aliens:
        alien.image_rect.x += settings.move_alien_x * settings.alien_direction

        if alien.image_rect.x + alien.image_rect.width >= settings.screen_width or alien.image_rect.x == 0:
            settings.alien_direction *= -1
            settings.move_alien_y = True

    if settings.move_alien_y:
        for alien1 in aliens:
            alien1.image_rect.y += settings.move_alien_y_increase

    settings.move_alien_y = False


def draw_aliens(aliens, settings, screen, bullets):
    # create aliens
    if len(aliens) == 0:
        create_alien_row(settings, screen, aliens)
    for alien in aliens:
        alien.create_alien()
    update_aliens(aliens, settings)

def collision(object1, object2):
    """object1 will be object below (ex: player ship) object2 will be object above (ex: alien ship)"""
    object1 = object1.image_rect
    object2 = object2.image_rect
    object2_x = [i for i in range(object2.x + 1,  ((object2.x + object2.width)-1))]
    object1_x = [i for i in range(object1.x + 1, ((object1.x + object1.width) -1))]
    object1_y = [i for i in range(object1.y + 1, ((object1.y + object1.height) -1))]
    object2_y = [i for i in range(object2.y - 1, ((object2.y + object2.height) - 1))]
    for y in object1_y:
        if y in object2_y:
            for i in object2_x:
                if i in object1_x:
                    return True
        break



def check_alien_player_collision(player, aliens, settings, screen):
    for alien in aliens[:]:
        if collision(player, alien) or alien.image_rect.bottom >= settings.screen_height:
            aliens = []
            create_alien_row(settings, screen, aliens)
            break


def check_alien_bullet_collision(aliens, bullets):
    """"killing the aliens when bullet have been fired"""
    for bullet in bullets:
        aliens_copy = aliens[:]
        for alien in aliens_copy:
            if collision(bullet, alien):
                collision_sound = mixer.Sound("C:\\Users\\motte\\IdeaProjects\\space shooter\\explosion.wav")
                collision_sound.play()
                bullets.remove(bullet)
                aliens.remove(alien)


def update_screen(CLOCK, screen, settings, player, bullets, aliens):
    #speed that which the game to update
    CLOCK.tick(settings.FLP)
    #animating the backround image
    background_loop(settings, screen)


    #move the bullet
    for bullet in bullets:
        if bullet.image_rect.bottom < 0:
            bullets.remove(bullet)
        bullet.update()



    #move the player left or right
    player.move_player()

    draw_aliens(aliens, settings, screen, bullets)



    check_alien_player_collision(player, aliens, settings, screen)
    check_alien_bullet_collision(aliens, bullets)


# draw the player onto the screen
    player.draw_player()


    if len(aliens) == 0:
        for bullet in bullets[:]:
            bullets.remove(bullet)
        CLOCK.tick(0.3)

    #updating the screen
    pygame.display.flip()



