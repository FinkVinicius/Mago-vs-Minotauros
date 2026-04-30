import pygame
from const import ALTURA_WIN, LARGURA_WIN
class Menu:
    def __init__(self, window):
        self.window = window
        
        # pega a imagem e redimensiona ela pra caber na tela
        self.surf = pygame.transform.scale(pygame.image.load('./Assets/menu.png'), (LARGURA_WIN, ALTURA_WIN))
        self.rect = self.surf.get_rect()
               
    def run(self):
        self.window.blit(source=self.surf, dest=self.rect)
        pygame.display.flip()
        pass