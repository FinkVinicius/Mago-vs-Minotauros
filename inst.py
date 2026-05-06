

import pygame

from const import ALTURA_WIN, COR_MENU, LARGURA_WIN


class Instrucoes:
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
            self.menu_text(20, "Pressione ESC para voltar", (255, 255, 255), (220, 20))

            centro_x, centro_y = self.window.get_width() // 2, self.window.get_height() // 2
            rect_bege = pygame.Rect(0, 0, 400, 350)
            rect_bege.center = (centro_x, centro_y)
            pygame.draw.rect(self.window, (245, 245, 220), rect_bege)
            pygame.draw.rect(self.window, (0, 0, 0), rect_bege, 3)

            # Reorganize as alturas (Y) para não ficarem grudadas
            self.menu_text(40, "CONTROLES", COR_MENU, (centro_x, centro_y - 120))

            # Player 1
            self.menu_text(32, "Player 1", COR_MENU, (centro_x, centro_y - 45))
            self.menu_text(26, "Setas: Mover", COR_MENU, (centro_x, centro_y - 10))
            self.menu_text(26, "Ctrl Dir: Atacar", COR_MENU, (centro_x, centro_y+20))

            # Player 2
            self.menu_text(32, "Player 2", COR_MENU, (centro_x, centro_y + 60))
            self.menu_text(26, "WASD: Mover", COR_MENU, (centro_x, centro_y + 95))
            self.menu_text(26, "Ctrl Esq: Atacar", COR_MENU, (centro_x, centro_y + 125))
            pygame.display.flip()
            
            #Eventos do menu
            for event in pygame.event.get():
                #fecha o jogo se o jogador clicar no X da janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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