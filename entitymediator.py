

from const import DANO_ENTITY, LARGURA_WIN
import enemy
from entity import Entity
import player
import playershot


class EntityMediator:
    @staticmethod
    def __verify_colision_window(ent: Entity):
         if isinstance (ent, enemy.Enemy):
                if ent.rect.right < 0:
                    ent.health = -900
         if isinstance (ent, playershot.PlayerShot):
                if ent.rect.left > LARGURA_WIN:
                    ent.health = -900
    @staticmethod
    def colision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_colision_window(test_entity)
            
            # Pula verificações se a entidade já estiver morta
            if test_entity.health <= 0:
                continue

            for j in range(i + 1, len(entity_list)):
                ent = entity_list[j]
                
                # Pula se a segunda entidade já estiver morta
                if ent.health <= 0:
                    continue

                if test_entity.rect.colliderect(ent.rect):
                    # Colisão: PlayerShot vs Enemy
                    if (isinstance(test_entity, playershot.PlayerShot) and isinstance(ent, enemy.Enemy)) or \
                    (isinstance(test_entity, enemy.Enemy) and isinstance(ent, playershot.PlayerShot)):
                        
                        if isinstance(test_entity, playershot.PlayerShot):
                            ent.health -= DANO_ENTITY[test_entity.name]
                            test_entity.health = -900 # Tiro some direto
                            if ent.health <= 0: ent.is_dead = True # Ativa animação no inimigo
                        else:
                            test_entity.health -= DANO_ENTITY[ent.name]
                            ent.health = -900 # Tiro some direto
                            if test_entity.health <= 0: test_entity.is_dead = True
                # --- ADICIONE ESTE BLOCO ABAIXO DO SEU IF DE TIRO ---
                    elif (isinstance(test_entity, player.Player) and isinstance(ent, enemy.Enemy)) or \
                        (isinstance(test_entity, enemy.Enemy) and isinstance(ent, player.Player)):
                        
                        # Descobre quem é o player e quem é o inimigo
                        p = test_entity if isinstance(test_entity, player.Player) else ent
                        inimigo = ent if isinstance(test_entity, player.Player) else test_entity
                        
                        # Tira a vida do player
                        p.health -= DANO_ENTITY[inimigo.name]
                        
                        if p.health <= 0:
                            p.is_dead = True

    @staticmethod        

    def verify_health(entity_list: list [Entity]):
        for ent in entity_list:
            if ent.health <= 0:
               ent.is_dead = True
