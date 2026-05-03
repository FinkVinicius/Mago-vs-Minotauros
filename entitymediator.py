

from const import LARGURA_WIN
import enemy
from entity import Entity
import playershot


class EntityMediator:
    @staticmethod
    def __verify_colision_window(ent: Entity):
         if isinstance (ent, enemy.Enemy):
                if ent.rect.right < 0:
                    ent.health = 0
         if isinstance (ent, playershot.PlayerShot):
                if ent.rect.left > LARGURA_WIN:
                    ent.health = 0 3
    @staticmethod
    def colision(entity_list: list [Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_colision_window(test_entity)
        
        pass
    @staticmethod
    def verify_health(entity_list: list [Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
