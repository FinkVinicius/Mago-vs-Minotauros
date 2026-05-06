import pygame
from const import ALTURA_WIN, COR_MENU, COR_SELECTED, LARGURA_WIN, OPCOES_MENU
import game
from level import Level

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
        opcao_selecionada = 0
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            # Roda a animação do menu
            frame_atual = self.frames[int(self.index_anim)]
            self.window.blit(frame_atual, (0, 0))
            self.index_anim += 0.1 
            if self.index_anim >= len(self.frames):
                self.index_anim = 1

            #Puxa o logo do menu para a tela, e centraliza ele coloca a 1 quarto da tela
            self.window.blit(self.surface_menu, (LARGURA_WIN/2 - self.surface_menu.get_width()/2, ALTURA_WIN/6 - self.surface_menu.get_height()/2 ))
            
            #Chama o metodo para escrever o texto do menu e alinha ele no centro da tela, e coloca as opções do menu uma em baixo da outra
            for i in range(len(OPCOES_MENU)):    
                if i == opcao_selecionada:
                    #Se a opção estiver selecionada, chama o metodo para escrever o texto do menu com a cor selecionada e um tamanho maior
                    self.menu_text(text_size= 35, text= OPCOES_MENU[i], color= COR_SELECTED, pos= (LARGURA_WIN/2, ALTURA_WIN/2 + 120 + i * 40))
                else:
                    self.menu_text(text_size= 30, text= OPCOES_MENU[i], color= COR_MENU, pos= (LARGURA_WIN/2, ALTURA_WIN/2 + 120 + i * 40))     
            
            #atualiza a tela
            pygame.display.flip()
            
            #Eventos do menu
            for event in pygame.event.get():
                #fecha o jogo se o jogador clicar no X da janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                #navega pelas opções do menu com as setas para cima e para baixo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        opcao_selecionada -= 1
                        if opcao_selecionada < 0:
                            opcao_selecionada = len(OPCOES_MENU) - 1
                    elif event.key == pygame.K_DOWN:
                        opcao_selecionada += 1
                        if opcao_selecionada >= len(OPCOES_MENU):
                            opcao_selecionada = 0
                    # devolve a opção selecionada quando o jogador pressionar Enter, e para a musica do menu
                    elif event.key == pygame.K_RETURN:
                        pygame.mixer_music.stop()
                        return opcao_selecionada

    #metodo para escrever o texto do menu
    def menu_text(self, text_size: int, text: str, color: tuple, pos: tuple,  shadow=True):
        font = pygame.font.Font('./Assets/fonte.ttf', text_size)

        if shadow:
            shadow_surface = font.render(text, True, (0, 0, 0))
            shadow_rect = shadow_surface.get_rect(center=(pos[0] + 2, pos[1] + 2))
            self.window.blit(shadow_surface, shadow_rect)

        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=pos)
        self.window.blit(text_surface, text_rect)
       
       

