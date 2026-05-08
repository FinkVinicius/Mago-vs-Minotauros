import pygame

#cores
COR_MENU = (218, 165, 32)
COR_SELECTED = (94, 33, 22)

#tamanho da janela
LARGURA_WIN = 1268
ALTURA_WIN = 720

# opções do menu
OPCOES_MENU = ('Single Player', 'Multiplayer', 'Instrucoes','Score', 'Sair')


#CONFIGURAÇÕES ENTIDADES
DANO_ENTITY = {'player1shot': 1,
               'player2shot': 1,
               'inimigo1': 1,
               'inimigo2': 1}
ENTITY_SPEED = {'player1':  5,
                'player2':  5,
                'inimigo1':  10, 
                'inimigo2':  5,
                'player1shot':  10,
                'player2shot':  10}
ENTITY_HEALTH = {'player1':  4, 
                 'player2':  4,
                 'inimigo1':  3,
                 'inimigo2':  4}
TAMANHOS =  {'player1':  (0.1, 0.2), 
               'player2':  (0.1, 0.2),
               'inimigo1':  (0.20, 0.3), 
               'inimigo2':  (0.15, 0.3),
               'player1shot':  (0.10, 0.04),
               'player2shot':  (0.10, 0.04),
                }

                    
# configurações dos players
PLAYERS_SPEED = 5
PLAYER_KEY_UP = {'player1': pygame.K_UP, 
                 'player2': pygame.K_w}
PLAYER_KEY_DOWN = {'player1': pygame.K_DOWN, 
                   'player2': pygame.K_s}
PLAYER_KEY_LEFT = {'player1': pygame.K_LEFT, 
                   'player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'player1': pygame.K_RIGHT, 
                    'player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'player1': pygame.K_RCTRL, 
                    'player2': pygame.K_LCTRL}


#configurações dos inimigos
EVENT_SPAWN_ENEMY = pygame.USEREVENT + 1
TEMPO_SPAWN_ENEMY = {'lvl1':  2000, 
                     'lvl2':  500}
SPAWN_POOL = {'lvl1': ['inimigo1'],
              'lvl2': ['inimigo1', 'inimigo2']}

