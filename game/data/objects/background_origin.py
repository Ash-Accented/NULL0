import pygame
from game.modules.modules import *
from game.data.objects.staticpoint import StaticPoint
from game.data.objects.vessel import VesselCircle

class BackgroundOrigin(VesselCircle):
   dx = bounds_x//2
   dy = bounds_y//2
   r = 4
   def __init__(self):
      super().__init__(BackgroundOrigin.dx, BackgroundOrigin.dy, 0, BackgroundOrigin.r)
      print(self.dx, self.dy, self.r, BackgroundOrigin.dx)
      self = BackgroundOrigin.draw_background_origin(self)

   def draw_background_origin(background_origin):
      upd_coords_object = StaticPoint.draw_static_point(background_origin, player.rect)
      print(upd_coords_object)
      background_origin_rect = pygame.draw.circle(screen, ColorsManual.white, (upd_coords_object), background_origin.r, width=0)
      background_origin.rect = StaticPoint.fix_drawn_rect(background_origin_rect)
      background_origin.drx, background_origin.dry = background_origin_rect.x, background_origin_rect.y
      background_origin.x_axis = pygame.draw.line(window, player.color, (background_origin.drx, 0), (background_origin.drx, height + grid_spacing), width=4)
      background_origin.y_axis = pygame.draw.line(window, player.color, (0, (background_origin.dry)), (width + grid_spacing, (background_origin.dry)), width=4)
      return(background_origin)

   def rect_alignment_orig(entity, background_origin):
      entity_coords = (background_origin.drx - (background_origin.dx - entity.dx)), (background_origin.dry - (background_origin.dy - entity.dy))
      return(entity_coords)
         
   
   
