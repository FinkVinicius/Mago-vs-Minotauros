
import pygame

from const import ENTITY_SPEED
from entity import Entity


class PlayerShot(Entity):
 
    def __init__(self, name: str, position: tuple, size: tuple):
        # Define o tamanho do player como 20% da altura da janela
        super().__init__(f"{name}1", position, size)
        self.name = name
        
        # Carrega as frames de animação do player
        self.frames = []
        for i in range(1, 5):
            image = pygame.image.load(f'./Assets/{name}{i}.png').convert_alpha()
            self.frames.append(pygame.transform.scale(image, (size[0], size[1])))
        # Inicializa o índice da animação e a imagem atual do player
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.animation_timer = 0
        self.animation_speed = 6

    def update(self):
        pass
    
    def animation(self):
        # atualiza a imagem do player para a próxima frame da animação, e reseta o timer da animação
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.surf = self.frames[self.frame_index]

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]
        self.animation()