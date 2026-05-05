import random
import pygame
from const import EVENT_SPAWN_ENEMY, SPAWN_POOL, TEMPO_SPAWN_ENEMY
import player
import entity 
import entityfactory
import entitymediator

class Level:
    
    def __init__(self, window, name, opcao):
        # pega as informações que vem do menu
        self.window = window
        self.name = name
        self.game_mode = opcao
        #lista de entidades na tela
        self.entity_list: list[entity.Entity] = []
        # chama a factory pra criar o background correspondete ao nivel
        self.entity_list.extend(entityfactory.EntityFactory.get_entity(self.name))
        # chama a factory pra criar o player 1, e se for modo cooperativo chama a factory pra criar o player 2
        self.entity_list.extend(entityfactory.EntityFactory.get_entity("player1"))
        if opcao == 1:
            self.entity_list.extend(entityfactory.EntityFactory.get_entity("player2"))
        #configura o tempo de spawn dos inimigos
        pygame.time.set_timer(EVENT_SPAWN_ENEMY, millis= TEMPO_SPAWN_ENEMY[self.name])
            
    def run(self):
        pygame.mixer_music.load(f'./Assets/{self.name}_music.mp3')
        pygame.mixer_music.play(-1)
        # Cria um relógio para controlar o frame rate do jogo
        clock = pygame.time.Clock()

        while True:
            # limita o jogo a rodar a 60 frames por segundo
            clock.tick(60)
            # importa as funçoes de movimento
            [ent.move() for ent in self.entity_list]
            # Desenha os backgrounds
            [self.window.blit(e.surf, e.rect) for e in self.entity_list if "background" in e.__class__.__module__]
            # Ordena entidades por posição vertical
            for ent in sorted([e for e in self.entity_list if "background" not in e.__class__.__module__], key=lambda e: e.rect.bottom):
                # desenhas as etidades organizadas na tela
                self.window.blit(source=ent.surf, dest=ent.rect)
                # se a entidade for player importa o tiro
                if isinstance(ent, player.Player): 
                    shot = ent.shoot()
                    if shot is not None:    
                        self.entity_list.append(shot)
            # desenha o texto do nome do nível, instruções e informações de debug
            self.level_text(text_size= 14, text= f"{self.name}", color= (255, 255, 255), pos= (100, 50))
            self.level_text(text_size= 14, text= "Pressione ESC para voltar ao menu", color= (255, 255, 255), pos= (100, 80))
            self.level_text(text_size= 14, text= f"Entidades na tela: {len(self.entity_list)}", color= (255, 255, 255), pos= (100, 110))
            self.level_text(text_size= 14, text= f"fps: {clock.get_fps():.2f}", color= (255, 255, 255), pos= (100, 170))
            # atualiza a tela depois de desenhar tudo
            pygame.display.update()
            # Verifica colisões entre as entidades importando a função de colisão do EntityMediator
            entitymediator.EntityMediator.colision(entity_list= self.entity_list)
            # verifica a vida, e elimina se ja passaram pelo loop da animação de morte
            self.entity_list = [ent for ent in self.entity_list if ent.health > -900]
            # botao de fechar a janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # coloquei voltar pro menu quando aperta esc
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                # evnto de spawn dos inimigos
                if event.type == EVENT_SPAWN_ENEMY:
                    # Escolhe um nome da lista baseada no nível atual
                    nome_inimigo = random.choice(SPAWN_POOL[self.name])
                    # Chama o factory passando o nome da entidade
                    self.entity_list.extend(entityfactory.EntityFactory.get_entity(nome_inimigo))

    # Função para desenhar texto na tela, usada para mostrar o nome do nível, instruções e informações de debug
    def level_text(self, text_size, text, color, pos):
        font = pygame.font.SysFont('Arial', text_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=pos)
        self.window.blit(text_surface, text_rect)
