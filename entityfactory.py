
import random

from background import background
from const import ALTURA_WIN, LARGURA_WIN, TAMANHOS
from enemy import Enemy
from player import Player


class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        tamanho = int(ALTURA_WIN * TAMANHOS.get(entity_name, 0))
        match entity_name:
            case 'lvl1':
                
                list_bg = []
                # Carrega as frames de animação do background, e posiciona elas lado a lado
                for i in range(1, 8):
                    list_bg.append(background(f"lvl1bg{i}", position=(0, 0)))
                    list_bg.append(background(f"lvl1bg{i}", position=(LARGURA_WIN, 0)))
                return list_bg
            case 'player1':
                
                # Posiciona o player1 no canto esquerdo da tela, e no meio da altura da tela
                return [Player('player1', position=(0, ALTURA_WIN // 2), size=tamanho)]
            case 'player2':
                # Posiciona o player2 no canto esquerdo da tela, acima do player1
                return [Player('player2', position=(0, ALTURA_WIN // 3), size=tamanho)]
            case 'inimigo1':
                # Posiciona o inimigo1 dentro da tela, perto da borda direita
                return [Enemy('inimigo1', position=(LARGURA_WIN*1.1, random.randint(ALTURA_WIN // 3, ALTURA_WIN - tamanho)), size=tamanho)]

            case 'inimigo2':
                # Posiciona o inimigo2 dentro da tela, perto da borda direita
                return [Enemy('inimigo2', position=(LARGURA_WIN*1.1, random.randint(ALTURA_WIN // 3, ALTURA_WIN - tamanho)), size=tamanho)]

            case _:
                return []