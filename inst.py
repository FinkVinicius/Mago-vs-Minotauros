

import pygame

from const import ALTURA_WIN, LARGURA_WIN


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

            pygame.display.flip()
            
            #Eventos do menu
            for event in pygame.event.get():
                #fecha o jogo se o jogador clicar no X da janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return