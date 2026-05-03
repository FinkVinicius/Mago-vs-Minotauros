from abc import abstractmethod

import pygame

from const import ALTURA_WIN, ENEMY_SPEED, LARGURA_WIN, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_UP, PLAYERS_SPEED
from entity import Entity

class Enemy(Entity):

    def __init__(self, name: str, position: tuple, size: int):
        # Define o tamanho do enemy como 20% da altura da janela
        self.enemy_size = size
        super().__init__(f"{name}run1", position, size=(self.enemy_size, self.enemy_size))
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

    def update(self):
        pass
    
    def animation(self):
        # atualiza a imagem do enemy para a próxima frame da animação, e reseta o timer da animação
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.surf = self.frames[self.frame_index]

    def move(self):
        # Move o enemy para a esquerda, e reseta a posição do enemy para a borda direita da tela quando ele sair da tela
        self.rect.centerx -= ENEMY_SPEED[self.name]
        self.animation()