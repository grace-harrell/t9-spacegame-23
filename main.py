import pygame
from random import randrange
import os
pygame.init()

FPS = 60
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

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

def draw_window(player, space_trash):
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(SPACE_STATION, (player.x, player.y))
    WIN.blit(ASTROID, (space_trash.x, space_trash.y))

    pygame.display.update()

trash_x = 1300
trash_y = randrange(HEIGHT)
    
def main():
    space_trash = pygame.Rect(trash_x, trash_y, ASTROID_WIDTH, ASTROID_HEIGHT)
    player = pygame.Rect(150,300, SPACE_STATION_WIDTH, SPACE_STATION_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run :
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        space_trash.x -= SPACE_TRASH_VEL
        if space_trash.x <= 0:
            space_trash.x = trash_x
            space_trash.y = randrange(HEIGHT)

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:  # MOVE UP
            player.y -= VEL
        
        if keys_pressed[pygame.K_s]: # MOVE DOWN
            player.y += VEL

        draw_window(player, space_trash)
    pygame.quit()

if __name__ == "__main__":
    main()