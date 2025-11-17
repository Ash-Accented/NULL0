import pygame
from game.modules.modules import *
from game.data.objects.staticpoint import StaticPoint

class BackgroundOrigin:
   def __init__(self, dx, dy, radius):
      pygame.sprite.Sprite.__init__(self)
      self.dx = dx
      self.dy = dy
      self.drx, self.dry = dx, dy
      self.radius = radius
      self.x_axis = pygame.draw.line(window, player.color, (self.drx, 0), (self.drx, height + grid_spacing), width=4)
      self.y_axis = pygame.draw.line(window, player.color, (0, (self.dry)), (width + grid_spacing, (self.dry)), width=4)

   def draw_background_origin(background_origin):
      
      upd_coords_object = StaticPoint.draw_static_point(background_origin, player.rendered_rect)
      background_origin_rect = pygame.draw.circle(screen, ColorsManual.white, (upd_coords_object), background_origin.radius, width=0)
      background_origin_rect = StaticPoint.fix_drawn_rect(background_origin_rect)
      background_origin.drx, background_origin.dry = background_origin_rect.x, background_origin_rect.y
      background_origin.x_axis = pygame.draw.line(window, player.color, (background_origin.drx, 0), (background_origin.drx, height + grid_spacing), width=4)
      background_origin.y_axis = pygame.draw.line(window, player.color, (0, (background_origin.dry)), (width + grid_spacing, (background_origin.dry)), width=4)
      return(background_origin)

   def rect_alignment_orig(entity, background_origin):
      entity_coords = (background_origin.drx - (background_origin.dx - entity.dx)), (background_origin.dry - (background_origin.dy - entity.dy))
      return(entity_coords)
         
   
   
