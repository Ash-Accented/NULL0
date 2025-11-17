from game.modules.base_modules import *
from game.modules.preloads import *
from game.data.function.generate_graph_plots import GeneratePlots

class PlayerFunc:
   def player_func_detect(sympy_expression, n):
      corner_x, corner_y = RenderPlayer.return_corners_xy()
      player_pos_x = (player.dx - corner_x)
      player_pos_y = (player.dy - corner_y)
      
      lwr_bound_x = -10
      uppr_bound_x = 10
      lwr_bound_y = player_pos_y + (-1*bounds_y)/2
      uppr_bound_y = player_pos_y + bounds_y/2
      disp = 500
      function_plots = GeneratePlots.generate_plots(sympy_expression, n, lwr_bound_x, uppr_bound_x, lwr_bound_y, uppr_bound_y, disp)
      return(function_plots)
   pass
