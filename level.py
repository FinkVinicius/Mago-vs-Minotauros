import random
import pygame
from const import EVENT_SPAWN_ENEMY, SPAWN_POOL, TEMPO_SPAWN_ENEMY, LARGURA_WIN, ALTURA_WIN
import player
import entity 
import entityfactory
import entitymediator
from score import Score

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
        self.font = pygame.font.Font('./Assets/fonte.ttf', 20)
        self.start_ticks = pygame.time.get_ticks()
        self.scorep2 = 0
        self.scorep1 = 0
        
            
    def run(self):
        pygame.mixer_music.load(f'./Assets/{self.name}_music.mp3')
        pygame.mixer_music.play(-1)
        # Cria um relógio para controlar o frame rate do jogo
        clock = pygame.time.Clock()

        while True:
            # limita o jogo a rodar a 60 frames por segundo
            for ent in self.entity_list:
                if ent.health <= 0 and not ent.scored:
                    if ent.last_damage == 'player1shot':
                        self.scorep1 += 1
                        ent.scored = True
                    elif ent.last_damage == 'player2shot':
                        self.scorep2 += 1
                        ent.scored = True 
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

            segundos_passados = (pygame.time.get_ticks() - self.start_ticks) // 1000
            timer_text = f"TIME: {segundos_passados // 60:02d}:{segundos_passados % 60:02d}"
            self.level_text(timer_text, (255, 255, 255), (20,20))

            p1 = next((ent for ent in self.entity_list if ent.name == 'player1'), None)
            p2 = next((ent for ent in self.entity_list if ent.name == 'player2'), None)
            if p1:
                txt_p1 = f"P1 HP: {max(0, p1.health)} | SCORE: {self.scorep1}"
                self.level_text(txt_p1, (255, 255, 255), (20, 40))
            else:
                self.level_text(txt_p1, (255, 255, 255), (20, 40))
            if self.game_mode == 1 and p2:
                txt_p2 = f"P2 HP: {max(0, p2.health)} | SCORE: {self.scorep2}"
                self.level_text(txt_p2, (255, 255, 255), (20, 60))

            fps_text = f"FPS: {int(clock.get_fps())}"
            self.level_text(fps_text, (0, 255, 0), (LARGURA_WIN - 100, ALTURA_WIN - 40))


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
            if not any(isinstance(ent, player.Player) for ent in self.entity_list):
                pygame.mixer_music.stop()
                save_screen = Score(self.window) 
                save_screen.save(self.game_mode, self.scorep1, self.scorep2)
                return
    # Função para desenhar texto na tela
    def level_text(self, text, color, pos, shadow=True):
        if shadow:
            shadow_surface = self.font.render(text, True, (0, 0, 0))
            self.window.blit(shadow_surface, (pos[0] + 2, pos[1] + 2))
        text_surface = self.font.render(text, True, color)
        self.window.blit(text_surface, pos)