import pygame
from const import ENTITY_SPEED
from entity import Entity

class PlayerShot(Entity):
 
    def __init__(self, name: str, position: tuple, size: tuple, assets: dict):
        #Chama entity
        super().__init__(name, position, size)
        self.name = name
        
        #pega os assets direto da factory
        self.frames = assets['run']
        self.framesmorte = assets['morte']
        
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        self.rect = self.surf.get_rect(center=position)
        
        # Variaveis da animação
        self.animation_timer = 0
        self.animation_speed = 6
        self.framesmorte_index = 0

    def animation(self):
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            
            #se morto faz a animção de contato e marca pra excluir com 999
            if self.is_dead:
                if self.framesmorte_index < len(self.framesmorte) - 1:
                    self.framesmorte_index += 1
                    self.surf = self.framesmorte[self.framesmorte_index]
                else:
                    self.health = -999 
            else:
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.surf = self.frames[self.frame_index]

    def move(self):
        self.animation()
        #se n tive morto reinicia 
        if self.is_dead:
            return 
        #seta direção e velocidade
        self.rect.centerx += ENTITY_SPEED[self.name]