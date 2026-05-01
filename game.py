
import pygame
from const import ALTURA_WIN, LARGURA_WIN
from menu import Menu
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size= (LARGURA_WIN, ALTURA_WIN))
        self.clock = pygame.time.Clock()

    def run(self):
        menu = Menu(self.window)
        while True:
            self.clock.tick(60)
            menu.run()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()