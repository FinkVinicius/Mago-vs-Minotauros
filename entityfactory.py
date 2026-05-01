
from background import background
from const import LARGURA_WIN


class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'lvl0':
                list_bg = []
                for i in range(1, 8):
                    list_bg.append(background(f"lvl1bg{i}", position=(0, 0)))
                    list_bg.append(background(f"lvl1bg{i}", position=(LARGURA_WIN, 0)))
                    

                return list_bg
            case _:
                return []