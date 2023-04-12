import pygame
from setup import setup
from player import *


def drawAll():
    window,explosion_sound, shoot_sound, game_over_sound, font, clock, window_height,window_width,collison_sound,fonts = setup()
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), Player.player)