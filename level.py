import random

import pygame

from const import EVENT_SPAWN_ENEMY, SPAWN_POOL, TEMPO_SPAWN_ENEMY
import entity
import entityfactory
import entitymediator



class Level:

    def __init__(self, window, name, opcao):
        self.window = window
        self.name = name
        self.game_mode = opcao
        self.entity_list: list[entity.Entity] = []
        self.entity_list.extend(entityfactory.EntityFactory.get_entity(self.name))
        self.timeout = 20000
        self.entity_list.extend(entityfactory.EntityFactory.get_entity("player1"))
        if opcao == 1:
            self.entity_list.extend(entityfactory.EntityFactory.get_entity("player2"))

        pygame.time.set_timer(EVENT_SPAWN_ENEMY, millis= TEMPO_SPAWN_ENEMY[self.name])
            
    def run(self):
        pygame.mixer_music.load(f'./Assets/{self.name}_music.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            self.level_text(text_size= 14, text= f"{self.name}", color= (255, 255, 255), pos= (100, 50))
            self.level_text(text_size= 14, text= "Pressione ESC para voltar ao menu", color= (255, 255, 255), pos= (100, 80))
            self.level_text(text_size= 14, text= f"Entidades na tela: {len(self.entity_list)}", color= (255, 255, 255), pos= (100, 110))
            self.level_text(text_size= 14, text= f"fps: {clock.get_fps():.2f}", color= (255, 255, 255), pos= (100, 170))

            pygame.display.update()
            # Verifica colisões entre as entidades importando a função de colisão do EntityMediator
            entitymediator.EntityMediator.colision(entity_list= self.entity_list)
            entitymediator.EntityMediator.verify_health(entity_list= self.entity_list)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # coloquei voltar pro menu quando aperta esc
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
               # No evento de spawn
                if event.type == EVENT_SPAWN_ENEMY:
                    # Escolhe um nome da lista baseada no nível atual (ex: 'lvl1')
                    nome_inimigo = random.choice(SPAWN_POOL[self.name])
                    # Chama o factory passando o nome escolhido
                    self.entity_list.extend(entityfactory.EntityFactory.get_entity(nome_inimigo))


    def level_text(self, text_size, text, color, pos):
        font = pygame.font.SysFont('Arial', text_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=pos)
        self.window.blit(text_surface, text_rect)
