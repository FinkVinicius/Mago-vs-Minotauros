import pygame

from const import ALTURA_WIN, ENTITY_SPEED, LARGURA_WIN, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, PLAYER_KEY_UP
from entity import Entity

class Player(Entity):

    def __init__(self, name: str, position: tuple, size: int, assets: dict):
        self.player_size = size
        super().__init__(name, position, size=(size, size))
        self.name = name
        
        # Variáveis de tiro
        self.shot_cooldown_timer = 0
        self.shoot_tick = 0  
        self.is_shooting = False
        self.shot_frame_index = 0

        # Varivel de invecibilidade depois de tomar um dano
        self.last_hit_time = 0
        self.hit_cooldown = 1000
        
        #pegamos tudo do dicionário assets vindo da Factory
        self.framesshot = assets['atack']
        self.frames = assets['run']
        self.framesmorte = assets['morte']
        
        # Inicialização do estado visual
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.animation_timer = 0
        self.animation_speed = 6
        self.framesmorte_index = 0
        
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
        #animação de atirando
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
        
        #animação pra piscar enquanto estiver imune
        agora = pygame.time.get_ticks()
        if agora - self.last_hit_time < self.hit_cooldown and not self.is_dead:
            alpha = 255 if (agora // 50) % 2 == 0 else 0
            self.surf.set_alpha(alpha)
        else:
            self.surf.set_alpha(255)

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
        #ativa animação                      
        self.animation()
      
    def shoot(self):
        #Definição do tiro
        pressed_keys = pygame.key.get_pressed()
        key_tiro = PLAYER_KEY_SHOOT[self.name]
        #Confere o cooldown e da menos um se maior q 0
        if self.shot_cooldown_timer > 0:
            self.shot_cooldown_timer -= 1
        #enq tive ativa tem um cooldown de 20frames e puxa toda sua animação da factory tmb    
        if pressed_keys[key_tiro]:
            if self.shot_cooldown_timer == 0:
                self.shot_cooldown_timer = 20  
                self.is_shooting = True
                self.shoot_tick = 20           
                self.shot_frame_index = 0
                pos_tiro = (self.rect.centerx, self.rect.centery - (self.player_size[1]  * 0.17))
                from entityfactory import EntityFactory
                return EntityFactory.get_entity(f"{self.name}shot", position=pos_tiro)[0]
        # se n der o tiro retorna none     
        return None
        