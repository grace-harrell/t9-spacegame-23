import pygame
from random import randrange
import os
import button
pygame.init()

FPS = 100
VEL = 5
SPACE_TRASH_VEL = 7

WIDTH, HEIGHT = 1200, 800


SPACE_STATION_WIDTH, SPACE_STATION_HEIGHT = 300, 300
ASTROID_WIDTH, ASTROID_HEIGHT = 200, 200

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

def draw_window(player, space_trash1, space_trash2, space_trash3):
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(SPACE_STATION, (player.x, player.y))
    WIN.blit(ASTROID, (space_trash1.x, space_trash1.y))
    WIN.blit(ASTROID2, (space_trash2.x, space_trash2.y))
    WIN.blit(ASTROID3, (space_trash3.x, space_trash3.y))



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



def main():
    space_trash1 = pygame.Rect(trash_x, trash_y, ASTROID_WIDTH, ASTROID_HEIGHT)
    space_trash2 = pygame.Rect(trash_x, trash_y, ASTROID_WIDTH, ASTROID_HEIGHT)
    space_trash3 = pygame.Rect(trash_x, trash_y, ASTROID_WIDTH, ASTROID_HEIGHT)

    player = pygame.Rect(150,300, SPACE_STATION_WIDTH, SPACE_STATION_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run :
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        space_trash_movement(space_trash1)
        space_trash_movement(space_trash2)
        space_trash_movement(space_trash3)

        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player)

        draw_window(player, space_trash1, space_trash2, space_trash3)
    pygame.quit()

if __name__ == "__main__":
    main()