from game.modules.base_modules import *
from game.modules.preloads import *

class Hitbox:
   surface_transparent = pygame.Surface((width, height), pygame.SRCALPHA)
   surface_transparent.set_alpha(0)
   def hitbox_draw(entity_rect, player_rect):
      width, height = screen.get_size()
      player_rect.x = player_rect.x - (player_rect.width // 2)
      player_rect.y = player_rect.y - (player_rect.height // 2)
      player_rect_hitbox = pygame.draw.rect(Hitbox.surface_transparent, ColorsManual.blue, ((player_rect.x, player_rect.y), (player_rect.width, player_rect.height)), 1)
      
      entity_rect.x = entity_rect.x - (entity_rect.width // 2)
      entity_rect.y = entity_rect.y - (entity_rect.height // 2)
      entity_rect_hitbox = pygame.draw.rect(Hitbox.surface_transparent, ColorsManual.blue, ((entity_rect.x, entity_rect.y), (entity_rect.width, entity_rect.height)), 1)
      
      window.blit(Hitbox.surface_transparent, (0, 0))

      return(player_rect_hitbox, entity_rect_hitbox)
   
   def hitbox_draw_entity_circle(entity):
      entity_rect_hitbox = pygame.draw.rect(window, ColorsManual.blue, ((entity.drx - entity.r, entity.dry - entity.r), (entity.w, entity.h)), 1)
      return(entity_rect_hitbox)
   def hitbox_draw_entity(entity):
      entity_rect_hitbox = pygame.draw.rect(window, ColorsManual.blue, ((entity.drx, entity.dry), (entity.w, entity.h)), 1)
      #window.blit(Hitbox.surface_transparent, (entity.drx, entity.dry))
      return(entity_rect_hitbox)
   def check_collision(obj, other_obj):
      check_collision = False
      if pygame.Rect.colliderect(obj.hitbox, other_obj.hitbox):
         check_collision = True 
      return(check_collision)
