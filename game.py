
import pygame
from const import ALTURA_WIN, LARGURA_WIN, OPCOES_MENU
from level import Level
from menu import Menu
class Game:
    def __init__(self):
        pygame.init()
        #define  um display
        self.window = pygame.display.set_mode(size= (LARGURA_WIN, ALTURA_WIN))
        #define um relógio para controlar o frame rate do jogo
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            #mantem o jogo rodando a 60 frames por segundo
            self.clock.tick(60)
            #roda o menu e pega a opção escolhida
            menu = Menu(self.window)
            opcao = menu.run()
            #roda o nível correspondente a opção escolhida
            if opcao == 0: 
                level = Level(self.window, 'lvl1', opcao)
                level_return = level.run()
            elif opcao == 1:
                level = Level(self.window, 'lvl1', opcao)
                level_return = level.run()    
            elif opcao == 2: 
                pass 
            elif opcao == 3: 
                pygame.quit()
                quit()