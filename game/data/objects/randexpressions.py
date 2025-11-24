import pygame
from game.modules.modules import *
from game.data.objects.staticpoint import StaticPoint
from game.data.objects.background_origin import BackgroundOrigin
from game.data.methodsandvars.init_vars import InitializeVars
from game.data.objects.vessel import VesselRect
class RandExpressions(VesselRect):
   dx = random.randrange(100, 1800)
   dy = random.randrange(100, 1800)
   fill = 1
   r = 100
   w = 250
   h = 250
   x = Symbol('x')
   set_irr_constants = [E, pi, root(2, 2), GoldenRatio]
   list_x = [x, sin(x), log(x), tan(x)]
   expr_const = random.choice(set_irr_constants)
   expr_int = random.randrange(1, 100)
   #FINISHED
   def __init__(self, num, index):
      super().__init__(RandExpressions.dx, RandExpressions.dy, RandExpressions.fill, RandExpressions.w, RandExpressions.h)
      self.collide = False
      self.num = num
      self.index = index
      #UPDATE THE VALS
      self.expr, self.surf, self.drx, self.dry, self.rect = RandExpressions.rand_expression_generate(self)
      #Boolean, true or false depending on conditions, false to begin with then set to true and subsequently unblitted
   def rand_expression_generate(rand_expr_obj):
      op_one = random.randrange(1, 10)
      op_two = random.randrange(1, 10)
      RandExpressions.expr_const = random.choice(RandExpressions.set_irr_constants)
      RandExpressions.expr_int = random.randrange(1, 100)
      expr = 3
      expr_const_num = OperationsSelf.operation_expr(RandExpressions.expr_const, RandExpressions.expr_int, op_one)
      random.shuffle(RandExpressions.list_x)
      RandExpressions.set_rand_var = random.choice(RandExpressions.list_x)
      expr = OperationsSelf.operation_expr(expr_const_num, RandExpressions.set_rand_var, op_two)
      #else:
         #expr = expr_const_num
      name_of_file = 'temp' + str(rand_expr_obj.num)
      rand_expr_obj.expr = expr
      #We want to blit the rect surface image upon a static point on the plane (defined by )
      rand_expr_obj.surf, rand_expr_obj.rect = GenerateImage.generate_img_surface(name_of_file, rand_expr_obj, "game/images/randomexpressions/")
      rand_expr_obj.drx, rand_expr_obj.dry = BackgroundOrigin.rect_alignment_orig(rand_expr_obj, InitializeVars.background_origin)
      return(rand_expr_obj.expr, rand_expr_obj.surf, rand_expr_obj.drx, rand_expr_obj.dry, rand_expr_obj.rect)
    
   def rand_expression_regenerate():
      dx, dy = random.randrange(100, 2900, 5), random.randrange(100, 2900, 10)
      return(dx, dy)




