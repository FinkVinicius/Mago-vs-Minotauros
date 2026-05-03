import pygame
from entitymediator import EntityMediator
class PlayerShot:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 5
        self.height = 10
        self.color = (255, 0, 0)  # Red color

    def update(self):
        self.y -= self.speed  # Move the shot upwards

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))