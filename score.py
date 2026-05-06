

import pygame

from const import ALTURA_WIN, LARGURA_WIN


class Score:
    def __init__(self, window):
        self.window = window
        self.frames = []
        for i in range(1, 9):
            self.frames.append(pygame.transform.scale(pygame.image.load(f'./Assets/frame{i}.png').convert_alpha(), (LARGURA_WIN, ALTURA_WIN)))
        self.index_anim = 0
       
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

            pygame.display.flip()
            
            #Eventos do menu
            for event in pygame.event.get():
                #fecha o jogo se o jogador clicar no X da janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
    def save (self, game_mode):
        pygame.mixer_music.load('./Assets/menu.mp3')
        pygame.mixer_music.play(-1) 
        opcao_selecionada = 0
        clock = pygame.time.Clock()
        player1 = ""


        while True:
            clock.tick(60)
            # Roda a animação do menu
            frame_atual = self.frames[int(self.index_anim)]
            self.window.blit(frame_atual, (0, 0))
            self.index_anim += 0.1 
            if self.index_anim >= len(self.frames):
                self.index_anim = 1

            # 2. Desenha o quadrado bege no meio
            largura_box, altura_box = 400, 600
            # Calcula o centro da tela baseado na sua janela
            centro_x = self.window.get_width() // 2
            centro_y = self.window.get_height() // 2
            
            rect_bege = pygame.Rect(0, 0, largura_box, altura_box)
            rect_bege.center = (centro_x, centro_y)
            pygame.draw.rect(self.window, (245, 245, 220), rect_bege) # Bege
            pygame.draw.rect(self.window, (0, 0, 0), rect_bege, 3)    # Borda preta

            # 3. Renderiza os textos
            self.menu_text(30, "Digite seu nome:", (50, 50, 50), (centro_x, centro_y - 200), shadow=False)
            self.menu_text(35, player1 + "|", (0, 0, 0), (centro_x, centro_y + 20), shadow=False)
            if game_mode = OPCOES_MENU [1]
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                
                if event.type == pygame.TEXTINPUT:
                    player1 += event.text

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        player1 = player1[:-1]
                    
                    if event.key == pygame.K_RETURN:
                        pygame.key.stop_text_input() # <--- PARA AQUI TAMBÉM
                        print(f"Nome final: {player1}")
                        return
    def menu_text(self, text_size: int, text: str, color: tuple, pos: tuple,  shadow=True):
        font = pygame.font.Font('./Assets/fonte.ttf', text_size)

        if shadow:
            shadow_surface = font.render(text, True, (0, 0, 0))
            shadow_rect = shadow_surface.get_rect(center=(pos[0] + 2, pos[1] + 2))
            self.window.blit(shadow_surface, shadow_rect)

        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=pos)
        self.window.blit(text_surface, text_rect)
       
