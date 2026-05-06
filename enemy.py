from abc import abstractmethod
from const import ENTITY_SPEED
from entity import Entity

class Enemy(Entity):

    def __init__(self, name: str, position: tuple, size: int, assets: dict):
        self.enemy_size = size
        super().__init__(name, position, size=(size, size))
        self.name = name
        
        # variavel pra saber se ta encostando no player pra pegar a animação de ataque
        self.is_colliding = False

        #pegamos tudo do dicionário assets vindo da Factory
        self.frames = assets['run']
        self.framesmorte = assets['morte']
        self.frames_colisao = assets['atack']

        # Inicialização do estado visual
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.animation_timer = 0
        self.animation_speed = 15
        self.frames_colisao_index = 0
        self.framesmorte_index = 0
    
    def animation(self):
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            # Só avança se não chegou no último frame de morte
            if self.is_dead:
                if self.framesmorte_index < len(self.framesmorte) - 1:
                    self.framesmorte_index += 1
                    self.surf = self.framesmorte[self.framesmorte_index]
                else:
                    self.health = -900
            #animação de batendo
            elif self.is_colliding:
                if self.frames_colisao_index < len(self.frames_colisao) - 1:
                    self.frames_colisao_index += 1
                    self.surf = self.frames_colisao[self.frames_colisao_index]
                else:
                    self.is_colliding = False
            else:
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.surf = self.frames[self.frame_index]
    
    def move(self):
        #ativa animação
        self.animation()
        #congela a animação do inimigo enq a animação de morte acontece
        if self.is_dead:
            return
        #define direção e velocidade
        self.rect.centerx -= ENTITY_SPEED[self.name]
        