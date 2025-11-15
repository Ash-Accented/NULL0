import pygame
from game.modules.modules import *
from game.data.objects.staticpoint import StaticPoint

class BackgroundOrigin:
   def __init__(self, dx, dy, drx, dry, radius):
      pygame.sprite.Sprite.__init__(self)
      self.dx = dx
      self.dy = dy
      self.drx = drx
      self.dry = dry
      self.radius = radius

   def draw_background_origin(background_origin_copy, player_rect):
      
      upd_coords_object = StaticPoint.draw_static_point(background_origin_copy, player_rect)
      background_origin_rect = pygame.draw.circle(screen, ColorsManual.white, (upd_coords_object), background_origin_copy.radius, width=0)
      background_origin_rect = StaticPoint.fix_drawn_rect(background_origin_rect)
      coords = background_origin_rect.x, background_origin_rect.y
      pygame.draw.line(window, ColorsManual.blue, ((coords[0]), 0), (coords[0], height + grid_spacing), width=4)
      pygame.draw.line(window, ColorsManual.blue, (0, (coords[1])), (width + grid_spacing, (coords[1])), width=4)
      return(coords)

   def rect_alignment_orig(entity, background_origin):
      entity_coords = (background_origin.drx - (background_origin.dx - entity.dx)), (background_origin.dry - (background_origin.dy - entity.dy))
      return(entity_coords)
   
