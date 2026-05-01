import pygame

import entity
import entityfactory


class Level:

    def __init__(self, window, name, opcao):
        self.window = window
        self.name = name
        self.game_mode = opcao
        self.entity_list: list[entity.Entity] = []
        self.entity_list.extend(entityfactory.EntityFactory.get_entity(f"lvl{opcao}"))
        

        
            
    def run(self):
        pygame.mixer_music.load(f'./Assets/{self.name}_music.mp3')
        pygame.mixer_music.play(-1)
        
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()