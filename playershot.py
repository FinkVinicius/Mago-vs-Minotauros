
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
         # Carrega as frames de animação de morte do enemy
        self.framesmorte = []
        for i in range(1, 5):
            self.framesmorte.append(pygame.transform.scale(pygame.image.load(f'./Assets/{name}morte{i}.png').convert_alpha(), (size[0], size[1])))
        self.framesmorte_index = 0
    
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

            else:

                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.surf = self.frames[self.frame_index]

    def move(self):
        self.animation()
        if self.is_dead:
            return # Se o inimigo estiver morto, ele não se move
        self.rect.centerx += ENTITY_SPEED[self.name]
            