from abc import ABC, abstractmethod

import pygame

from const import ENTITY_HEALTH


class Entity(ABC):

    def __init__(self, name: str, position: tuple, size=None):
        self.name = name
        image = pygame.image.load(f'./Assets/{name}.png').convert_alpha()
        self.surf = pygame.transform.scale(image, size) if size else image
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        if self.name in ENTITY_HEALTH:
            self.health = ENTITY_HEALTH[self.name]
        else:
            self.health = 999

    @abstractmethod
    def move(self):
        pass
        