from game.modules.base_modules import *
from game.data.preload.colors import ColorsManual
from game.data.background.background import bounds_x, bounds_y, grid_spacing, GridBackground
from game.data.display.display import screen, window, display_info, display_flags, width, height
from game.data.display.frames import clock, framerate
class Hitbox:
   surface_transparent = pygame.Surface((width, height), pygame.SRCALPHA)
   surface_transparent.set_alpha(0)
 
   def hitbox_draw_entity_circle(entity):
      entity_rect_hitbox = pygame.draw.rect(Hitbox.surface_transparent, ColorsManual.blue, ((entity.drx - entity.r, entity.dry - entity.r), (entity.w, entity.h)), 1)
      window.blit(Hitbox.surface_transparent, (entity.drx, entity.dry))
      return(entity_rect_hitbox)
   def hitbox_draw_entity(entity):
      entity_rect_hitbox = pygame.draw.rect(Hitbox.surface_transparent, ColorsManual.blue, ((entity.drx, entity.dry), (entity.w, entity.h)), 1)
      window.blit(Hitbox.surface_transparent, (entity.drx, entity.dry))
      return(entity_rect_hitbox)
   def check_collision(obj, other_obj):
      check_collision = False
      if pygame.Rect.colliderect(obj.hitbox, other_obj.hitbox):
         check_collision = True 
      return(check_collision)
