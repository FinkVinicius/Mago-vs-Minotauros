from abc import ABC, abstractmethod
from const import ENTITY_HEALTH
class Entity(ABC):
    def __init__(self, name: str, position: tuple, size=None):
        #recebe o nome da entidade
        self.name = name
        self.position = position
        self.size = size
        #informa que a entidade n ta morta
        self.is_dead = False
        #por conta das animções n consigo receber a primeira imagem aqui por conta da diferença entre os bg e as outras entidades
        self.surf = None
        self.rect = None
        # se a entidade tem umaa vida definida pega das consts se n define como 1
        if self.name in ENTITY_HEALTH:
            self.health = ENTITY_HEALTH[self.name]
        else:
            self.health = 1
        
        #variavel ultimo dano
        self.last_damage = None
        self.scored = False
