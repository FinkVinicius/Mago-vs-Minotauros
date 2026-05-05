from abc import ABC, abstractmethod
from const import ENTITY_HEALTH
class Entity(ABC):
    # se eu tivesse o conhecimento que adquiri com o projeto atual antes
    # eu teria colocado a função de movimento e animação dentro da classe Entity
    #ja que usei basicamente o mesmo número de quadros para os mesmos tipos de animação
    def __init__(self, name: str, position: tuple, size=None):
        #recebe o nome da entidade
        self.name = name
        self.position = position
        self.size = size
        #recebe a info que a entidade n ta morta
        self.is_dead = False
        #por conta das animções n consigo receber a primeira imagem aqui por conta da diferença entre os bg e as outras entidades
        self.surf = None
        self.rect = None
        # se a entidade tem umaa vida definida pega das consts se n define como 1
        if self.name in ENTITY_HEALTH:
            self.health = ENTITY_HEALTH[self.name]
        else:
            self.health = 1

    # @abstractmethod
    # def move(self):
    #     pass
        