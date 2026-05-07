

import pygame

from dbproxy import DBProxy
from const import ALTURA_WIN, COR_MENU, LARGURA_WIN


class Score:
    def __init__(self, window):
        self.window = window
        self.frames = []
        for i in range(1, 9):
            self.frames.append(pygame.transform.scale(pygame.image.load(f'./Assets/frame{i}.png').convert_alpha(), (LARGURA_WIN, ALTURA_WIN)))
        self.index_anim = 0
       
    def run(self, ):
        
        pygame.mixer_music.load('./Assets/menu.mp3')
        pygame.mixer_music.play(-1) 
        
        clock = pygame.time.Clock()
        meu_banco = DBProxy('highscores.db')
        top_10 = meu_banco.consulta()
        meu_banco.close()

        while True:
            clock.tick(60)
            
            frame_atual = self.frames[int(self.index_anim)]
            self.window.blit(frame_atual, (0, 0))
            self.index_anim += 0.1 
            if self.index_anim >= len(self.frames):
                self.index_anim = 1
            self.menu_text(20, "Pressione ESC para voltar", (255, 255, 255), (220, 20))

            centro_x, centro_y = self.window.get_width() // 2, self.window.get_height() // 2
            rect_bege = pygame.Rect(0, 0, 310, 320)
            rect_bege.center = (centro_x, centro_y)
            pygame.draw.rect(self.window, (245, 245, 220), rect_bege)
            pygame.draw.rect(self.window, (0, 0, 0), rect_bege, 3)

            self.menu_text(30, "TOP 10", COR_MENU, (centro_x, centro_y - 130))
            y_offset = centro_y - 60
            for i, registro in enumerate(top_10):
                nome = registro[1]
                score = registro[2]
                texto_rank = f"{i+1}. {nome} - {score}"
                self.menu_text(20, texto_rank, COR_MENU, (centro_x, y_offset-40))
                y_offset += 25

            pygame.display.flip()
            
           
            for event in pygame.event.get():
               
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
    
    
    
    def save(self, game_mode, scorep1, scorep2):
        pygame.key.start_text_input()
        clock = pygame.time.Clock()
        self.scorep1 = scorep1
        self.scorep2 = scorep2
        meu_banco = DBProxy('highscores.db')
        player1 = ""
        player2 = ""
        focando_p1 = True
        
        while True:
            clock.tick(60)
            
            
            frame_atual = self.frames[int(self.index_anim)]
            self.window.blit(frame_atual, (0, 0))
            self.index_anim = (self.index_anim + 0.1) % len(self.frames)

            centro_x, centro_y = self.window.get_width() // 2, self.window.get_height() // 2
            rect_bege = pygame.Rect(0, 0, 430, 200)
            rect_bege.center = (centro_x, centro_y)
            pygame.draw.rect(self.window, (245, 245, 220), rect_bege)
            pygame.draw.rect(self.window, (0, 0, 0), rect_bege, 3)

            # 3. Textos na Tela
            self.menu_text(30, "Registre seu score", COR_MENU, (centro_x, centro_y - 70))

            if focando_p1:
                self.menu_text(25, "Nome do Player 1:", (COR_MENU), (centro_x, centro_y - 30))
                self.menu_text(30, player1 + "|", (COR_MENU), (centro_x, centro_y + 20))
            else:
                
                self.menu_text(25, "Nome do Player 2:", (COR_MENU), (centro_x, centro_y - 30))
                self.menu_text(30, player2 + "|", (COR_MENU), (centro_x, centro_y + 20))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.TEXTINPUT:
                    if focando_p1:
                        if len(player1) < 15: player1 += event.text
                    else:
                        if len(player2) < 15: player2 += event.text

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if focando_p1: player1 = player1[:-1]
                        else: player2 = player2[:-1]

                    if event.key == pygame.K_RETURN:
                            if game_mode != 0 and focando_p1:
                                focando_p1 = False
                            else:
                                p1_score_final = self.scorep1 
                                if player1 and p1_score_final > 0: 
                                    meu_banco.save(player1, p1_score_final)
                                if game_mode != 0 and player2:
                                    p2_score_final = self.scorep2
                                    if p2_score_final > 0:
                                        meu_banco.save(player2, p2_score_final)
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

       
