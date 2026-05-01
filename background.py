import pygame   
from const import LARGURA_WIN
import entity

class background(entity.Entity):   

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)    
        #No meu projeto resolvi usar mais de um background para criar um efeito de paralaxe, por isso o nome do background tem um numero no final, e a velocidade do background é definida por esse numero
        self.speed = int(name[-1])
        pass

    def move(self,):
        self.rect.centerx -= self.speed

        if self.rect.right <= 0:
            self.rect.left = LARGURA_WIN
        pass