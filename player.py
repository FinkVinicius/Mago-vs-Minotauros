import pygame

from const import ALTURA_WIN, ENTITY_SPEED, LARGURA_WIN, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, PLAYER_KEY_UP
from entity import Entity
from playershot import PlayerShot

class Player(Entity):

    def __init__(self, name: str, position: tuple, size: int):
        self.player_size = size
        super().__init__(name, position, size=(size, size))
        self.name = name
        
        # Variável para controlar o cooldown do tiro
        self.shot_cooldown_timer = 0
        self.shoot_tick = 0  
        self.is_shooting = False
        self.framesshot = []
        for i in range(1, 3):
            self.framesshot.append(pygame.transform.scale(pygame.image.load(f'./Assets/{name}atack{i}.png').convert_alpha(), (self.player_size, self.player_size)))
        self.is_shooting = False
        self.shoot_tick = 0
        self.shot_frame_index = 0
        # Carrega as frames de animação do player
        self.frames = []
        for i in range(1, 8):
            self.frames.append(pygame.transform.scale(pygame.image.load(f'./Assets/{name}run{i}.png').convert_alpha(), (self.player_size, self.player_size)))
        # Inicializa o índice da animação e a imagem atual do player
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.animation_timer = 0
        self.animation_speed = 6
        self.framesmorte = []
        for i in range(1, 5):
            self.framesmorte.append(pygame.transform.scale(pygame.image.load(f'./Assets/{name}morte{i}.png').convert_alpha(), (self.player_size, self.player_size)))
        self.framesmorte_index = 0
    def update(self):
        pass
    
    def animation(self):
        if self.is_dead:
            self.animation_timer += 1
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                # Só avança se não chegou no último frame de morte
                if self.framesmorte_index < len(self.framesmorte) - 1:
                    self.framesmorte_index += 1
                    self.surf = self.framesmorte[self.framesmorte_index]
                else:
                    self.health = -999 

        elif self.is_shooting:
            self.animation_timer += 1
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.shot_frame_index = (self.shot_frame_index + 1) % len(self.framesshot)
                self.surf = self.framesshot[self.shot_frame_index]
            
            self.shoot_tick -= 1
            if self.shoot_tick <= 0:
                self.is_shooting = False 

        else:
            self.animation_timer += 1
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.surf = self.frames[self.frame_index]
    def move(self):
            # Move o player com as setas do teclado, e limita o movimento do player para dentro da tela
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > ALTURA_WIN//3:
                    self.rect.y -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < ALTURA_WIN:
                    self.rect.y += ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
                    self.rect.x -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < LARGURA_WIN:
                    self.rect.x += ENTITY_SPEED[self.name]
            
        self.animation()
      
    def shoot(self):
        pressed_keys = pygame.key.get_pressed()
        key_tiro = PLAYER_KEY_SHOOT[self.name]
        current_time = pygame.time.get_ticks() # Pega o tempo atual do jogo
        if self.shot_cooldown_timer > 0:
            self.shot_cooldown_timer -= 1
        if pressed_keys[key_tiro]:
            # Só atira se o tempo atual for maior que (tempo do último tiro + delay)
            
            if self.shot_cooldown_timer == 0:
                self.shot_cooldown_timer = 20  # Delay de 20 quadros direto
            
                self.is_shooting = True
                self.shoot_tick = 20           # Pose dura os mesmos 20 quadros
                self.shot_frame_index = 0
                
                return PlayerShot(
                    name=f"{self.name}shot", 
                    position=(self.rect.centerx, self.rect.centery - (self.player_size * 0.17)),
                    size=(self.player_size // 2, self.player_size // 5)
                )
                
        return None
        