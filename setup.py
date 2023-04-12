import pygame

def setup():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    window_width = 640
    window_height = 480
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Space Shooter")

    # Load the images
    #player_image = pygame.image.load("player.png").convert_alpha()

    # Load the sounds
    explosion_sound = pygame.mixer.Sound("Gun+Silencer.mp3")
    shoot_sound = pygame.mixer.Sound("Gun+Silencer.mp3")
    game_over_sound = pygame.mixer.Sound("gameover.wav")
    collison_sound = pygame.mixer.Sound("Grenade+1.mp3")

    # Set up the font
    font = pygame.font.Font(None, 36)
    fonts = pygame.font.SysFont('comicsans', 30)
    # Set up the clock
    clock = pygame.time.Clock()

    # Return the necessary variables
    return window,explosion_sound, shoot_sound, game_over_sound, font, clock, window_height,window_width,collison_sound,fonts

