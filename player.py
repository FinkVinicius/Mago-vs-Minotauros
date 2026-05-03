import pygame

from const import ALTURA_WIN, LARGURA_WIN, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_UP, PLAYERS_SPEED
from entity import Entity

class Player(Entity):

    def __init__(self, name: str, position: tuple, size: int):
        # Define o tamanho do player como 20% da altura da janela
        self.player_size = size
        super().__init__(f"{name}run1", position, size=(self.player_size, self.player_size))
        self.name = name
        
        # Carrega as frames de animação do player
        self.frames = []
        for i in range(1, 8):
            image = pygame.image.load(f'./Assets/{name}run{i}.png').convert_alpha()
            self.frames.append(pygame.transform.scale(image, (self.player_size, self.player_size)))
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
        # Move o player com as setas do teclado, e limita o movimento do player para dentro da tela
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > ALTURA_WIN//3:
                self.rect.y -= PLAYERS_SPEED
            if pressed_keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < ALTURA_WIN:
                self.rect.y += PLAYERS_SPEED
            if pressed_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
                self.rect.x -= PLAYERS_SPEED
            if pressed_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < LARGURA_WIN:
                self.rect.x += PLAYERS_SPEED
        
            self.animation()