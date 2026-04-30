
import pygame

from menu import Menu
class Game:
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode(size= (800, 600))

    def run(self, ):
       
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



            #daqui pra frente é pra fechar o games
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #pygame.quit()
                    #quit()