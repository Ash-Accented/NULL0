import pygame
from game.modules.modules import *
from game.data.objects.staticpoint import StaticPoint
from game.data.objects.background_origin import BackgroundOrigin
class RandExpressions:
   set_irr_constants = {E, pi, root(2, 2), GoldenRatio}
   set_rand_functions = {}
   set_rand_nums = set(range(1, 50))
   expr = random.choice(list(set_rand_nums))
   pos_range_x = set(range(100, 2900))
   pos_range_y = set(range(100, 2900))
   pos_range_x_rand = random.choice(list(pos_range_x))
   pos_range_y_rand = random.choice(list(pos_range_y))
   def __init__(self, dx, dy, length, height, dissipate):
      pygame.sprite.Sprite.__init__(self)
      self.dx = dx
      self.dy = dy
      self.length = length
      self.height = height
      self.dissipate = dissipate        #Boolean, true or false depending on conditions, false to begin with then set to true and subsequently unblitted
   def rand_expression_generate(rand_expr_object, equation_object, player_rect):
      RandExpressions.expr = random.choice(list(RandExpressions.set_rand_nums))
      #We want to blit the rect surface image upon a static point on the plane (defined by )
      latex_expr, surface_image_expr, rect_surface_image_expr = GenerateImage.generate_img_surface("temp1", RandExpressions.expr, rand_expr_object, "game/images/randomexpressions/")
      rect_coordinates = StaticPoint.draw_static_point(rand_expr_object, player_rect)
      return(surface_image_expr, rect_coordinates)
    
   def rand_expression_regenerate():
      RandExpressions.pos_range_x_rand = random.choice(list(RandExpressions.pos_range_x))
      RandExpressions.pos_range_y_rand = random.choice(list(RandExpressions.pos_range_y))
      return(RandExpressions.pos_range_x_rand, RandExpressions.pos_range_y_rand)

   def get_rand_expr():
      return(RandExpressions.expr)

   def rand_expression_coords(surface_image_expr, rand_expr_object, player_rect, background_origin):
      expr_coords = BackgroundOrigin.rect_alignment_orig(rand_expr_object, background_origin)
      window.blit(surface_image_expr, expr_coords)
      return(surface_image_expr.get_rect(), expr_coords)
      print(expr_coords)
