from abc import ABC, abstractmethod

import pygame

from const import ALTURA_WIN, ENTITY_HEALTH, LARGURA_WIN


class Entity(ABC):

    def __init__(self, name: str, position: tuple, size=None):
        self.name = name
        self.is_dead = False
        self.surf = None
        self.rect = None
        self.speed = 0
        if self.name in ENTITY_HEALTH:
            self.health = ENTITY_HEALTH[self.name]
        else:
            self.health = 999

    @abstractmethod
    def move(self):
        pass
        