import pygame
import random
from setup import setup
from player import *
from drawAll import *

# Initialize Pygame
pygame.init()

# Set up the game
window,explosion_sound, shoot_sound, game_over_sound, font, clock, window_height,window_width,collison_sound,fonts = setup()

# Set up the bullets
bullet_speed = 10
bullets = []
bullet_sound = shoot_sound
max_bullets = 6
crash = collison_sound
gameover = game_over_sound

# Set up the enemies
enemy_width = 50
enemy_height = 50
enemy_speed = 5
enemies = []
enemy_spawn_rate = 30
enemy_spawn_counter = 0

# Set up the score and high scores
score = 0
high_scores = 0
font = pygame.font.SysFont('comicsans', 30)
# Set up the game loop

with open("high_scores.txt", "r") as file:
    scores = file.readlines()
scores = [s.strip().split(",") for s in scores]
scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)
 
high_scores = scores[0][1]

game_running = True
while game_running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        Player.player.y -= Player.player_speed
    if keys[pygame.K_DOWN]:
        Player.player.y += Player.player_speed

    # Keep player within screen bounds
    if Player.player.top <= 0:
        Player.player.top = 0
    if Player.player.bottom >= window_height:
        Player.player.bottom = window_height

    # Handle shooting
    if keys[pygame.K_SPACE] and len(bullets) < max_bullets:
        bullet_sound.play()
        bullet = pygame.Rect(Player.player.right, Player.player.centery - 2, 10, 5)
        bullet.x += bullet_speed
        bullets.append(bullet)

    # Handle bullet movement and collision
    for bullet in bullets:
        bullet.x += bullet_speed
        if bullet.x > window_width:
            if bullet in bullets:
                bullets.remove(bullet)
        for enemy in enemies:
            if bullet.colliderect(enemy):
                if bullet in bullets:
                    bullets.remove(bullet)
                if enemy in enemies:
                    enemies.remove(enemy)
                    score += 10


    # Handle enemy movement and collision
    enemy_spawn_counter += 1
    if enemy_spawn_counter == enemy_spawn_rate:
        enemy_spawn_counter = 0
        enemy_y = random.randint(0, window_height - enemy_height)
        enemy = pygame.Rect(window_width, enemy_y, enemy_width, enemy_height)
        enemies.append(enemy)
    for enemy in enemies:
        enemy.x -= enemy_speed
        if enemy.x < 0 - enemy.width:
            if enemy in enemies:
                enemies.remove(enemy)
        if enemy.colliderect(Player.player):
            Player.num_of_players -= 1
            enemies.remove(enemy)
            crash.play()
            pygame.time.delay(100)
            pygame.draw.rect(window, (255, 0, 0), Player.player)
            
    if Player.num_of_players <= 0:
        gameover.play()
        game_over_text = font.render("GAME OVER!", True, (255,0,0))
        window.blit(game_over_text, (window_width/3, window_height/2.5))
        pygame.display.update()
        pygame.time.delay(3500)
        game_running = False



    # Draw everything
    drawAll()
    

    for bullet in bullets:
        pygame.draw.rect(window, (255, 0, 0), bullet)
    for enemy in enemies:
        pygame.draw.rect(window, (0, 0, 255), enemy)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))
    
    high_score_text = font.render("High Score: " + str(high_scores), True, (255, 255, 255))
    window.blit(high_score_text, (250, 10))
    
    lives_text = font.render("Lives: " + str(Player.num_of_players), True, (255,255,255))
    window.blit(lives_text, (0, 440))
    
    #update high score and display it on the screen
    if int(score) > int(high_scores) :
        high_scores = score 
        window.blit(high_score_text, (250, 10))
    if score%50 == 0 and score > 0:
         enemy_speed += .01


    pygame.display.update()
    # Tick the clock
    clock.tick(60)

# Game loop has ended, prompt for high score and save
#name = input("Enter your name: ")
score_entry = "Player1" + "," + str(score) + "\n"
with open("high_scores.txt", "a") as file:
    file.write(score_entry)

# Read high scores from file and print top 5
with open("high_scores.txt", "r") as file:
    scores = file.readlines()
scores = [s.strip().split(",") for s in scores]
scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)
print("High scores:")
for i in range(min(len(scores), 5)):
    print(f"{i+1}. {scores[i][0]} - {scores[i][1]}")
 
# Quit Pygame
pygame.quit()
