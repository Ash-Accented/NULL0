from game.modules.modules import *
from game.data.player.player_render import player, RenderPlayer
from game.data.operations.drawfunction import DrawFunction

class PlayerFunc:
   def player_func_detect(sympy_expression, player, screen, bounds_x, bounds_y):
      function_plots = DrawFunction.draw_function(sympy_expression, player, screen, bounds_x, bounds_y)
      return(function_plots)
   pass
