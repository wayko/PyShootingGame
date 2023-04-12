import pygame
from setup import setup

class Player:
    window,explosion_sound, shoot_sound, game_over_sound, font, clock, window_height,window_width,collison_sound,fonts = setup()
   # Set up the game state
    player_width = 50
    player_height = 50
    player_x = 50
    player_y = window_height / 2 - player_height / 2
    player_speed = 5
    player_rotation = 0
    #player = pygame.Rect(player_x, player_y, player_width, player_height)
    num_of_players = 3
    player_points = [(player_x + player_width // 2, player_y), (player_x + player_width, player_y + player_height), (player_x, player_y + player_height)]
    player = pygame.draw.polygon(window, (0,0,255), player_points)
    #player = pygame.image.load("player.png")

    