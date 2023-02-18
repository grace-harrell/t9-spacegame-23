import pygame
from random import randrange
import os
import button

# button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

pygame.init()

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
exit_Button = button.Button(450, 200, exit_Button_img, 0.8)
# exit_Button = pygame.transform.scale(exit_Button_img, (100, 100))

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


#def make_text(hp):
#    text = FONT.render('HP: '+ str(hp), True, GREEN)
#    text_rect = text.get_rect()
#    text_rect.center = (60, 750)


def draw_window(player, space_trash1, space_trash2, space_trash3, hp):
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(exit_Button,(1100,675))
    WIN.blit(SPACE_STATION, (player.x, player.y))
    WIN.blit(ASTROID, (space_trash1.x, space_trash1.y))
    WIN.blit(ASTROID2, (space_trash2.x, space_trash2.y))
    WIN.blit(ASTROID3, (space_trash3.x, space_trash3.y))
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


def main():
    hp = 100
    #make_text(hp)
    space_trash1 = pygame.Rect(trash_x, trash_y, ASTROID_WIDTH - 100, ASTROID_HEIGHT - 100)
    space_trash2 = pygame.Rect(trash_x, trash_y, ASTROID_WIDTH - 100, ASTROID_HEIGHT - 100)
    space_trash3 = pygame.Rect(trash_x, trash_y, ASTROID_WIDTH - 100, ASTROID_HEIGHT - 100)

    player = pygame.Rect(150,300, SPACE_STATION_WIDTH - 70, SPACE_STATION_HEIGHT - 70)

    clock = pygame.time.Clock()
    run = True
    while run :
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            pygame.quit()
        
        space_trash_movement(space_trash1)
        space_trash_movement(space_trash2)
        space_trash_movement(space_trash3)

        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player)

        if player.colliderect(space_trash1) or player.colliderect(space_trash2) or player.colliderect(space_trash3):
            hp = hit_space_trash(hp)

        draw_window(player, space_trash1, space_trash2, space_trash3, hp)
    pygame.quit()

if __name__ == "__main__":
    main()