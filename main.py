import pygame
from random import randrange
from pygame import mixer
import os
import button
import time
import sys
pygame.init()
mixer.init()

mixer.music.load(os.path.join('Assets','space_tunes.mp3'))
mixer.music.set_volume(0.5)
mixer.music.play()

FPS = 100
VEL = 5
SPACE_TRASH_VEL = 7
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

WIDTH, HEIGHT = 1200, 800


SPACE_STATION_WIDTH, SPACE_STATION_HEIGHT = 300, 300
ASTROID_WIDTH, ASTROID_HEIGHT = 200, 200


FONT = pygame.font.Font('freesansbold.ttf', 32)

exit_Button_img= pygame.image.load(os.path.join('Assets', 'quit_button.png'))
exit_Button = button.Button(1050, 680, exit_Button_img, 0.03)
# exit_Button = pygame.transform.scale(exit_Button_img, (100, 100))

reset_Button_img= pygame.image.load(os.path.join('Assets', 'retry_button.png'))
reset_Button = button.Button(900, 685, reset_Button_img, 0.03)

BACKGROUND_IMG = pygame.image.load(os.path.join('Assets', 'spacegame_background.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))

SPACE_STATION_IMG = pygame.image.load(os.path.join('Assets', 'spacestation_sprite.png'))
SPACE_STATION = pygame.transform.scale(SPACE_STATION_IMG, (SPACE_STATION_WIDTH, SPACE_STATION_HEIGHT))

ASTROID_IMG = pygame.image.load(os.path.join('Assets', 'astroid_sprite.png'))
ASTROID = pygame.transform.scale(ASTROID_IMG, (ASTROID_WIDTH, ASTROID_HEIGHT))

ASTROID_IMG2 = pygame.image.load(os.path.join('Assets', 'astroid_sprite2.png'))
ASTROID2 = pygame.transform.scale(ASTROID_IMG2, (ASTROID_WIDTH, ASTROID_HEIGHT))

ASTROID_IMG3 = pygame.image.load(os.path.join('Assets', 'astroid_sprite3.png'))
ASTROID3 = pygame.transform.scale(ASTROID_IMG3, (ASTROID_WIDTH, ASTROID_HEIGHT))



WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")


def draw_window(player, space_trash1, space_trash2, space_trash3, hp, hour, mins, sec):
    WIN.blit(BACKGROUND,(0,0))
    # WIN.blit(exit_Button,(1100,675))
    WIN.blit(SPACE_STATION, (player.x, player.y))
    WIN.blit(ASTROID, (space_trash1.x, space_trash1.y))
    WIN.blit(ASTROID2, (space_trash2.x, space_trash2.y))
    WIN.blit(ASTROID3, (space_trash3.x, space_trash3.y))
    time_text = FONT.render("{}:{}:{}".format(sec, mins, hour), True, GREEN)
    time_text_rect = time_text.get_rect()
    time_text_rect.center = (60, 720)
    WIN.blit(time_text, time_text_rect)
    text = FONT.render('HP: '+ str(hp), True, GREEN)
    text_rect = text.get_rect()
    text_rect.center = (60, 750)
    WIN.blit(text, text_rect)
    pygame.display.update()

trash_x = 1300
trash_y = randrange(HEIGHT)

# class Space_trash():
 #   def__init__(self, x, y, image):


#def spawn_space_trash ():

def space_trash_movement(space_trash):
    space_trash.x -= SPACE_TRASH_VEL
    if space_trash.x <= 0:
        space_trash.x = randrange(1250, 2250)
        space_trash.y = randrange(HEIGHT)

def player_movement(keypressed, player):
        if keypressed[pygame.K_w]  and player.y > -100:  # MOVE UP
            player.y -= VEL 
        
        if keypressed[pygame.K_s] and player.y < (HEIGHT - 70): # MOVE DOWN
            player.y += VEL

def hit_space_trash(hp):
    hp -= 1
    return hp

def game_over():
    #player.kill()
    game_over_text = FONT.render("Game Over", True, (200, 0, 0))
    WIN.blit(game_over_text,((WIDTH/2 - (game_over_text.get_width()/2)), (HEIGHT/2 + (game_over_text.get_height()/2)))) 
    pygame.display.update()
    if reset_Button.draw(BACKGROUND):
        main()
    time.sleep(20)
    pygame.quit()
    sys.exit()


def main():
    sec = 0
    mins = 0
    hour = 0
    hp = 100
    space_trash1 = pygame.Rect(trash_x, trash_y, ASTROID_WIDTH - 100, ASTROID_HEIGHT - 100)
    space_trash2 = pygame.Rect(trash_x, trash_y, ASTROID_WIDTH - 100, ASTROID_HEIGHT - 100)
    space_trash3 = pygame.Rect(trash_x, trash_y, ASTROID_WIDTH - 100, ASTROID_HEIGHT - 100)

    player = pygame.Rect(150,300, SPACE_STATION_WIDTH - 70, SPACE_STATION_HEIGHT - 70)

    clock = pygame.time.Clock()
    run = True
    while run :
        clock.tick(FPS)
        sec+=1
        if sec == 60:
            sec = 0
            mins += 1
        if mins == 60:
            mins = 0
            hour += 1

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if exit_Button.draw(BACKGROUND):
           pygame.quit()
        
        if reset_Button.draw(BACKGROUND):
            main()
        
        space_trash_movement(space_trash1)
        space_trash_movement(space_trash2)
        space_trash_movement(space_trash3)

        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player)

        if player.colliderect(space_trash1) or player.colliderect(space_trash2) or player.colliderect(space_trash3):
            hp = hit_space_trash(hp)

        draw_window(player, space_trash1, space_trash2, space_trash3, hp, sec, mins, hour)
        if hp == 0:
            game_over()
    pygame.quit()

if __name__ == "__main__":
    main()