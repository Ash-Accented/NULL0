from game.modules.base_modules import *
from game.modules.preloads import *
from game.data.function.generate_graph_plots import GeneratePlots

class PlayerFunc:
   def player_func_detect(sympy_expression, n):
      function_plots = GeneratePlots.generate_plots(sympy_expression, n)
      return(function_plots)
   pass
