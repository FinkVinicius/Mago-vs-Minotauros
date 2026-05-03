import pygame   
import entity

class background(entity.Entity):   

    def __init__(self, name: str, position: tuple):
        window_size = pygame.display.get_window_size()
        super().__init__(name, position, size=window_size)    
        #No meu projeto resolvi usar mais de um background para criar um efeito de paralaxe, por isso o nome do background tem um numero no final, e a velocidade do background é definida por esse numero
        window_size = pygame.display.get_window_size()
        # Você pode até forçar a extensão .png ou .jpg aqui
        self.surf = pygame.image.load(f'./Assets/{name}.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, window_size)
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = int(name[-1])

    def move(self):
        self.rect.centerx -= self.speed
        # Se o background sair completamente da tela, ele volta para a posição inicial, criando um loop infinito de background
        if self.rect.right <= 0:
            # Reseta a posição do background para o lado direito da tela
            self.rect.left = pygame.display.get_window_size()[0]
    