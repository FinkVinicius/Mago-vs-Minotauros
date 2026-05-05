
import random
import pygame
from background import Background
from const import ALTURA_WIN, LARGURA_WIN, TAMANHOS
from enemy import Enemy
from player import Player
from playershot import PlayerShot

class EntityFactory:
#fiz todas as animações na mão individualmente, entidade por entidade, pra so depois decobrir que podia ter salvo em um dicionario aqui.
    _image_cache = {}

    @staticmethod
    def _load_assets(name: str, size: int):
        if name in EntityFactory._image_cache:
            return EntityFactory._image_cache[name]
        assets = {
            'run': [],
            'morte': [],
            'atack': []
        }

        # Carrega a corrida
        for i in range(1, 8):
            img = pygame.image.load(f'./Assets/{name}run{i}.png').convert_alpha()
            assets['run'].append(pygame.transform.scale(img, size))

        # Carrega Morte 
        for i in range(1, 6):
            img = pygame.image.load(f'./Assets/{name}morte{i}.png').convert_alpha()
            assets['morte'].append(pygame.transform.scale(img, size))

        # Carrega ataque se não for um tiro
        if 'shot' not in name:
            for i in range(1, 5):
                img = pygame.image.load(f'./Assets/{name}atack{i}.png').convert_alpha()
                assets['atack'].append(pygame.transform.scale(img, size))

        EntityFactory._image_cache[name] = assets
        return assets
    
    @staticmethod
    def get_entity(entity_name: str, position = (0,0)):
                
        match entity_name:
            # cria o background
            case 'lvl1':
                # Carrega as frames de animação do background, e posiciona elas lado a lado tmb adiciona o lvl1bj no nome da entity
                list_bg = []
                for i in range(1, 8):
                    list_bg.append(Background(f"lvl1bg{i}", position=(0, 0)))
                    list_bg.append(Background(f"lvl1bg{i}", position=(LARGURA_WIN, 0)))
                return list_bg
            
            case 'player1' | 'player2':
                tamanho = LARGURA_WIN*TAMANHOS.get(entity_name)[0], ALTURA_WIN*TAMANHOS.get(entity_name)[1]
                assets = EntityFactory._load_assets(entity_name, tamanho)
                y_pos = ALTURA_WIN // 2 if entity_name == 'player1' else ALTURA_WIN // 3
                return [Player(entity_name, (0, y_pos), tamanho, assets)]
            
            case 'inimigo1' | 'inimigo2':
                tamanho = LARGURA_WIN*TAMANHOS.get(entity_name)[0], ALTURA_WIN*TAMANHOS.get(entity_name)[1]
                assets = EntityFactory._load_assets(entity_name, tamanho)
                pos_x = LARGURA_WIN * 1.1
                pos_y = random.randint(ALTURA_WIN // 3, int(ALTURA_WIN - tamanho[1]))
                return [Enemy(entity_name, (pos_x, pos_y), tamanho, assets)]
            
            case 'player1shot' | 'player2shot':
                tamanho = LARGURA_WIN*TAMANHOS.get(entity_name)[0], ALTURA_WIN*TAMANHOS.get(entity_name)[1]
                assets = EntityFactory._load_assets(entity_name, tamanho) 
                return [PlayerShot(entity_name, position, tamanho, assets)]
            
            case _:
                return []