

import pygame

from const import DANO_ENTITY, LARGURA_WIN
import enemy
from entity import Entity
import player
import playershot


class EntityMediator:
    @staticmethod
    def __verify_colision_window(ent: Entity):
         # se o tiro ou inimigo sairem da tela apaga eles automaticamente
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
            
            # Pula se estiver morta
            if test_entity.health <= 0:
                continue

            for j in range(i + 1, len(entity_list)):
                ent = entity_list[j]
                
                if ent.health <= 0:
                    continue

                if test_entity.rect.colliderect(ent.rect):
                    # Colisãoplayshot e enemy
                    if (isinstance(test_entity, playershot.PlayerShot) and isinstance(ent, enemy.Enemy)) or (isinstance(test_entity, enemy.Enemy) and isinstance(ent, playershot.PlayerShot)):
                        shot = test_entity if isinstance(test_entity, playershot.PlayerShot) else ent
                        inimigo = ent if isinstance(test_entity, playershot.PlayerShot) else test_entity
                        #impede do tiro acertar duas vezes pq ativa o is_dead logo depois
                        if not shot.is_dead:
                            #diminui vida do inimigo
                            inimigo.health -= DANO_ENTITY[shot.name] 
                            # O tiro morre ao tocar fazendo a animação ativar e o tiro n repetir o dano
                            shot.is_dead = True 
                            # mmata o inimigo se a vida baixar de 0
                            if inimigo.health <= 0: 
                                inimigo.is_dead = True
                    # colisão inimigo e player            
                    elif (isinstance(test_entity, player.Player) and isinstance(ent, enemy.Enemy)) or(isinstance(test_entity, enemy.Enemy) and isinstance(ent, player.Player)):
                        p = test_entity if isinstance(test_entity, player.Player) else ent
                        inimigo = ent if isinstance(test_entity, player.Player) else test_entity
                        # Verifica se o tempo atual permite um novo dano
                        ticks_atuais = pygame.time.get_ticks()
                        if ticks_atuais - p.last_hit_time > p.hit_cooldown:
                             # O dano so acontece se pegar a parte de cima do inimigo no player
                             if pygame.Rect(p.rect.left, p.rect.top, p.rect.width, p.rect.height // 2).colliderect(pygame.Rect(inimigo.rect.left, inimigo.rect.top, inimigo.rect.width, inimigo.rect.height // 2)):
                                #diminuio a vida do player
                                p.health -= DANO_ENTITY[inimigo.name]
                                # Registra o momento do dano
                                p.last_hit_time = ticks_atuais 
                                # ativa a animação de ataque do inimigo
                                inimigo.is_colliding = True
                                # se a vida do player for menor que 0 mata ele
                                if p.health <= 0:
                                    p.is_dead = True
