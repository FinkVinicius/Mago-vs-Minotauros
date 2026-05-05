from abc import abstractmethod

import pygame

from const import ENTITY_SPEED
from entity import Entity

class Enemy(Entity):

    def __init__(self, name: str, position: tuple, size: int):
        self.enemy_size = size
        super().__init__(name, position, size=(size, size))
        self.name = name
        
        
        # Carrega as frames de animação do enemy
        self.frames = []
        for i in range(1, 8):
            image = pygame.image.load(f'./Assets/{name}run{i}.png').convert_alpha()
            self.frames.append(pygame.transform.scale(image, (self.enemy_size, self.enemy_size)))
        # Inicializa o índice da animação e a imagem atual do enemy 
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.animation_timer = 0
        self.animation_speed = 6
        # Carrega as frames de animação de morte do enemy
        self.framesmorte = []
        for i in range(1, 6):
            self.framesmorte.append(pygame.transform.scale(pygame.image.load(f'./Assets/{name}morte{i}.png').convert_alpha(), (self.enemy_size, self.enemy_size)))
        self.framesmorte_index = 0
        # Carrega as frames de animação de ataque do enemy
        self.frames_colisao = []
        for i in range(1, 5): # 2 frames: Assets/NameColisao1.png e Colisao2.png
            img = pygame.image.load(f'./Assets/{name}atack{i}.png').convert_alpha()
            self.frames_colisao.append(pygame.transform.scale(img, (self.enemy_size, self.enemy_size)))
        self.is_colliding = False
        self.frames_colisao_index = 0
    
    def animation(self):
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            
            if self.is_dead:
                if self.framesmorte_index < len(self.framesmorte) - 1:
                    self.framesmorte_index += 1
                    self.surf = self.framesmorte[self.framesmorte_index]
                else:
                    self.health = -999 

            elif self.is_colliding:
                self.frames_colisao_index = (self.frames_colisao_index + 1) % len(self.frames_colisao)
                self.surf = self.frames_colisao[self.frames_colisao_index]
                self.is_colliding = False 

            else:
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.surf = self.frames[self.frame_index]
    def move(self):
        self.animation()
        if self.is_dead:
            return
        
        self.rect.centerx -= ENTITY_SPEED[self.name]
        