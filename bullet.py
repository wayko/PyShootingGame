import pygame

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def move(self):
        self.rect.move_ip(self.speed, 0)
