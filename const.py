import pygame

#cores
COR_MENU = (218, 165, 32)
COR_SELECTED = (255, 255, 255)

#tamanho da janela
LARGURA_WIN = 1268
ALTURA_WIN = 720

# opções do menu
OPCOES_MENU = ('Single Player', 'Multiplayer', 'Instrucoes', 'Sair')

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
ENEMY_SPEED = {'inimigo1':  3, 
               'inimigo2':  5}
EVENT_SPAWN_ENEMY = pygame.USEREVENT + 1
TEMPO_SPAWN_ENEMY = {'lvl1':  5000, 
                     'lvl2':  1000}
SPAWN_POOL = {'lvl1': ['inimigo1'],
              'lvl2': ['inimigo1', 'inimigo2']}

#tamanhos dos sprites
TAMANHOS =  {'player1':  0.2, 
               'player2':  0.2,
               'inimigo1':  0.25, 
               'inimigo2':  0.3}


