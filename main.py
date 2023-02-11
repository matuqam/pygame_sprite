import sys
from typing import List
import pygame
from pygame.locals import *

from world import World

map = World()
pygame.init()

# optional clock: makes the game run at 60 fps
clock = pygame.time.Clock()

# optional window name
pygame.display.set_caption('This is the window caption') 
WINDOW_SIZE = (400, 400)
# screen is considered a surface
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

# hub surface
hub = pygame.Surface(size=(200, 50))

# this returns a surface
player_image_idle = pygame.image.load('./sprites/player_idle.png')
player_image_right = pygame.image.load('./sprites/player_right.png')
player_image_left = pygame.transform.flip(player_image_right, True, False)

# npc
r2d2_sprites: List[pygame.Surface] = [pygame.image.load(f'./sprites/r2d2/r2d2_{orientation}.png') for orientation in ["left", "center", "right"]]
r2d2_left, r2d2_center, r2d2_right = r2d2_sprites

def configure_controls():
    up = K_e
    down = K_d
    left = K_s
    right = K_f
    return (up, down, left, right)

def manage_movement(keys, player):
    up, down, left, right = keys
    p_last_x, p_last_y = player
    player_x, player_y = p_last_x, p_last_y
    if pygame.key.get_pressed()[up]:
        player_y = p_last_y - 1
    if pygame.key.get_pressed()[down]:
        player_y = p_last_y + 1
    if pygame.key.get_pressed()[left]:
        player_x = p_last_x - 1
    if pygame.key.get_pressed()[right]:
        player_x  = p_last_x + 1
        
    
    return (player_x, player_y), (p_last_x, p_last_y)


controls = configure_controls()
player_pos = (50, 50)

while True:
    screen.fill((130,110,130))  # Clear the screen each frame.

    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()

    player_pos, p_last_pos = manage_movement(controls, player_pos)

    # select which image to display based on the player direction
    if player_pos[0] > p_last_pos[0]:
        r2_sprite = r2d2_right
        player_image = player_image_right
    elif player_pos[0] < p_last_pos[0]:
        r2_sprite = r2d2_left
        player_image = player_image_left
    else:
        r2_sprite = r2d2_center
        player_image = player_image_idle

    screen.blit(source=hub, dest=(0, 0))
    hub.blit(source=r2_sprite, dest=(160, 8))
    screen.blit(player_image, player_pos)

    pygame.display.update()
    clock.tick(60)