import pygame
from const import ALTURA_WIN, COR_MENU, LARGURA_WIN, OPCOES_MENU
class Menu:
    def __init__(self, window):
        self.window = window
        #laço para carregar as imagens da animação do menu
        self.frames = []
        for i in range(1, 9):
            self.frames.append(pygame.transform.scale(pygame.image.load(f'./Assets/frame{i}.png').convert_alpha(), (LARGURA_WIN, ALTURA_WIN)))
        self.index_anim = 0
        #Imagem do logo do menu e deixa ela com metade da largura e altura da tela
        self.surface_menu = pygame.transform.scale(pygame.image.load('./Assets/logo.png').convert_alpha(), (LARGURA_WIN/2, ALTURA_WIN/2))
       
    def run(self):
        #Chama a musica e toca ela em loop
        pygame.mixer_music.load('./Assets/menu.mp3')
        pygame.mixer_music.play(-1) 
        
        while True:
            # Roda a animação do menu
            frame_atual = self.frames[int(self.index_anim)]
            self.window.blit(frame_atual, (0, 0))
            self.index_anim += 0.005 
            if self.index_anim >= len(self.frames):
                self.index_anim = 0
            #Puxa o logo do menu para a tela, e centraliza ele coloca a 1 quarto da tela
            self.window.blit(self.surface_menu, (LARGURA_WIN/2 - self.surface_menu.get_width()/2, ALTURA_WIN/6 - self.surface_menu.get_height()/2 ))
            #Chama o metodo para escrever o texto do menu e alinha ele no centro da tela, e coloca as opções do menu uma em baixo da outra
            for i in range(len(OPCOES_MENU)):    
                self.menu_text(text_size= 35, text= OPCOES_MENU[i], color= COR_MENU, pos= (LARGURA_WIN/2, ALTURA_WIN/2 + 120 + i * 40))
            #atualiza a tela
            pygame.display.flip()

            #Fecha o jogo quando clicar no X
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    #metodo para escrever o texto do menu
    def menu_text(self, text_size: int, text: str, color: tuple, pos: tuple):
        font = pygame.font.Font('./Assets/fonte.ttf', text_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=pos)
        self.window.blit(text_surface, text_rect)
    #metodo para escrever o vs do menu
   
