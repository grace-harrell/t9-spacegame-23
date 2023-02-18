import pygame
import os
pygame.init()

FPS = 60
VEL = 5

WIDTH, HEIGHT = 1200, 800
SPACE_STATION_WIDTH, SPACE_STATION_HEIGHT = 300, 300

BACKGROUND_IMG = pygame.image.load(os.path.join('Assets', 'spacegame_background.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))

SPACE_STATION_IMG = pygame.image.load(os.path.join('Assets', 'spacestation_sprite.png'))
SPACE_STATION = pygame.transform.scale(SPACE_STATION_IMG, (SPACE_STATION_WIDTH, SPACE_STATION_HEIGHT))


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

def draw_window(player):
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(SPACE_STATION, (player.x, player.y))

    pygame.display.update()

def main():
    player = pygame.Rect(150,300, SPACE_STATION_WIDTH, SPACE_STATION_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run :
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:  # MOVE UP
            player.y -= VEL
        
        if keys_pressed[pygame.K_s]: # MOVE DOWN
            player.y += VEL

        draw_window(player)
    pygame.quit()

if __name__ == "__main__":
    main()