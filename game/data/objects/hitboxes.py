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

   def hitbox_draw_entity(entity_rect, entity_coords):
      width, height = screen.get_size()
      x, y = entity_coords
      entity_rect_hitbox = pygame.draw.rect(Hitbox.surface_transparent, ColorsManual.blue, ((x, y), (entity_rect.width, entity_rect.height)), 1)
      window.blit(Hitbox.surface_transparent, (x, y))
      return(entity_rect_hitbox)
   def check_collision(entity_rect, entity_other_rect):
      check_collision = False
      if pygame.Rect.colliderect(entity_rect, entity_other_rect):
         check_collision = True 
      return(check_collision)
