
import pygame
from inst import Instrucoes
from const import ALTURA_WIN, LARGURA_WIN
from level import Level
from menu import Menu
from score import Score
class Game:
    def __init__(self):
        pygame.init()
        #define  um display
        self.window = pygame.display.set_mode(size= (LARGURA_WIN, ALTURA_WIN))
        #define um relogio dr o frame rate do jogo
        self.clock = pygame.time.Clock()
    
    def show_transition_screen(self, text):
        pygame.mixer_music.load(f'./Assets/transicion.mp3')
        pygame.mixer_music.play(-1)
        self.window.fill((0, 0, 0))
        font = pygame.font.Font('./Assets/fonte.ttf', 50)
        text_surf = font.render(text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(LARGURA_WIN // 2, ALTURA_WIN // 2))
        self.window.blit(text_surf, text_rect)
        pygame.display.update()
        pygame.time.delay(5000)

    def run(self):
        while True:
            #mantem o jogo rodando a 60
            self.clock.tick(60)
            #roda o menu e pega a opção escolhida
            score = Score(self.window)
            instrucoes = Instrucoes (self.window)
            menu = Menu(self.window)
            opcao = menu.run()

            if opcao in [0, 1]:
                level1 = Level(self.window, 'lvl1', opcao)
                res1 = level1.run()

                if res1["status"] == "NEXT_LEVEL":
                    self.show_transition_screen("NIVEL 2")
                    level2 = Level(self.window, 'lvl2', opcao, res1["p1"], res1["p2"])
                    res2 = level2.run()

                    if res2["status"] == "NEXT_LEVEL":
                        self.show_transition_screen("VOCE VENCEU!")
                        pygame.mixer_music.stop()
                        save_screen = Score(self.window) 
                        save_screen.save(opcao, res2["p1"], res2["p2"])
                        pass
                    
                    elif res2["status"] == "VOCE MORREU":
                        self.show_transition_screen("VOCE MORREU")
                        pygame.mixer_music.stop()
                        pass
                else:
                    self.show_transition_screen("VOCE MORREU")
                    pygame.mixer_music.stop()
                    pass
                    
            elif opcao == 2:
                instrucoes = instrucoes.run()
                pass 
            elif opcao == 3: 
                score.run()
                pass 
            elif opcao == 4: 
                pygame.quit()
                quit()