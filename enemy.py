import random
import pygame
from bullet import Bullet

class Enemy:
    def __init__(self):
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.right = 800
        self.rect.top = random.randint(0, 550)
        self.speed = random.randint(2, 6)

    def move(self):
        self.rect.move_ip(-self.speed, 0)

    def shoot(self):
        return Bullet(self.rect.left, self.rect.centery)
