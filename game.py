
import pygame

from const import ALTURA_WIN, LARGURA_WIN
from menu import Menu
class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size= (LARGURA_WIN, ALTURA_WIN))

    def run(self, ):
       
        while True:
        # Esse for é pra fechar a janela quando clicar no X
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        
            menu = Menu(self.window)
            menu.run()
            pass



            