from game.modules.base_modules import *
from game.modules.preloads import *
class GeneratePlots:
   def check_errors(sympy_expression):
      init_printing()
      x = Symbol('x', real=True)
      func_graphable = True
      try:
         func = lambdify(x, sympy_expression, modules='numexpr', cse=True, docstring_limit=1000) #creation of a function 'func', that numerically evaluates sympy functions with the 'numexpr' code printer 
         print("HI")
         return(func_graphable)
      except SyntaxError as e:
         print({e})
         func_graphable = False
         return(func_graphable)
   def generate_plots(sympy_expression):
      corner_x, corner_y = RenderPlayer.return_corners_xy()
      
      scale = grid_spacing
      lower_bound_y = (-1*bounds_y)/2
      upper_bound_y = bounds_y/2
     
      lower_bound_x = -2
      upper_bound_x = 10
      dispersion_points = 275
      
      
      init_printing()
      x = Symbol('x', real=True)
      player_pos_x = (player.dx - corner_x)
      player_pos_y = (player.dy - corner_y)
      func = lambdify(x, sympy_expression, modules='numexpr', cse=True, docstring_limit=1000) #creation of a function 'func', that numerically evaluates sympy functions with the 'numexpr' code printer 
      print(func)
      x_arr = np.linspace(lower_bound_x, upper_bound_x, dispersion_points) #initialization of array for x coordinates
      y_arr = (player_pos_y - scale*func(x_arr))
      try:
         print(y_arr)
         y_arr = np.clip(y_arr, lower_bound_y, upper_bound_y, out=y_arr) #initialization of array for y coordinates; generating baseline y mappings for all values x defined by our linspace array x_arr
      except TypeError as e:
         print({e})
         try:
            y_arr = np.full(len(x_arr), y_arr)
         except TypeError as e:
            print({e})
      #Strips NaNs, and INF+- values and renders functions that may possess errors, renderable
      y_arr[np.isnan(y_arr)] = player_pos_y
      y_arr[np.isposinf(y_arr)] = player_pos_y + upper_bound_y 
      y_arr[np.isneginf(y_arr)] = player_pos_y + lower_bound_y
      
      x_arr = player_pos_x + scale*x_arr 
      try:
         point_arr = np.vstack((x_arr, y_arr))
      except ValueError as e:
         y_arr = np.full(len(x_arr), upper_bound_y)
         point_arr = np.vstack((x_arr, y_arr))
      #x_arr = (player.dx - corner_x)  #set origin point for x values relative to player position and scale x values by a factor equivalent to grid_spacing 
      #y_arr = (player.dy - corner_y) #set origin point for y values relative to player position and scale y values by a factor equivalent to grid_spacing
               
      with ignore_warnings(RuntimeWarning):
        float(func(np.array([0])))
 
      
      return(point_arr)
   pass

