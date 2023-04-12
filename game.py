import pygame
from pygame import mixer
import random
from player import Player
from enemy import Enemy
from bullet import Bullet
from setup import setup_window, update_window, game_over_screen, update_score
from collisions import check_enemy_collision, check_bullet_collision

# Initialize Pygame
pygame.init()

# Set up the window
screen = setup_window()

# Load background music
mixer.music.load('assets/background.wav')
mixer.music.play(-1)

# Set up the player
player = Player()

# Set up the enemy group
enemies = pygame.sprite.Group()

# Set up the bullet group
bullets = pygame.sprite.Group()

# Set up the clock
clock = pygame.time.Clock()

# Set up the game variables
game_over = False
score = 0
high_scores = []

# Load the high scores
with open("high_scores.txt", "r") as f:
    for line in f:
        high_scores.append(int(line))

# Start the game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                bullets.add(bullet)

    # Move the player
    keys_pressed = pygame.key.get_pressed()
    player.move(keys_pressed)

    # Spawn enemies
    if random.randint(1, 60) == 1:
        enemy = Enemy()
        enemies.add(enemy)

    # Update the enemy positions
    for enemy in enemies:
        enemy.move()

    # Check for collisions between player and enemies
    if check_enemy_collision(player, enemies):
        game_over = True

    # Check for collisions between bullets and enemies
    score += check_bullet_collision(bullets, enemies)

    # Remove enemies that have gone off the screen
    for enemy in enemies.copy():
        if enemy.rect.top > screen.get_height():
            enemies.remove(enemy)

    # Remove bullets that have gone off the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    # Draw the window
    update_window(screen, player, enemies, bullets, score)

    # Update the score
    update_score(screen, score, high_scores)

    # Update the clock
    clock.tick(60)

# Game over screen
game_over_screen(screen, score, high_scores)

# Save the high scores
with open("high_scores.txt", "w") as f:
    for high_score in high_scores:
        f.write(str(high_score) + "\n")

# Quit Pygame
pygame.quit()
