from abc import ABC, abstractmethod

import pygame

from const import ALTURA_WIN, LARGURA_WIN


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.transform.scale(pygame.image.load(f'./Assets/{name}.png').convert_alpha(), (LARGURA_WIN, ALTURA_WIN))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
        