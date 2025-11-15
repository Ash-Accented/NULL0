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

   def odd_powers(n, y_arr, y_arr_regular, x_arr, func, player_pos_y, scale):
      y_arr = np.real(y_arr)
      y_arr[np.isnan(y_arr_regular)] = player_pos_y + scale*y_arr[np.isnan(y_arr_regular)]
      y_arr[np.isfinite(y_arr_regular)] = player_pos_y - scale*y_arr[np.isfinite(y_arr_regular)]
      return(y_arr)


         #for i in y_arr:
            #r = np.roots(y_arr)
            #cross_nans = r[np.isreal(r)]
            #y_arr[np.isnan[y_arr]] = cross_nans
            #return(y_arr)
            #if np.isnan(i) and nan_splice_bool == True:
               #print(gen_counter, "nan")
               #real_index = (gen_counter - 1)
               #y_indsreals_arr.append(real_index)
               #y_indsnans_arr.append(gen_counter)
               #nan_splice_bool = False
               #real_splice_bool = True
               
            #if np.isfinite(i) and real_splice_bool == True:
               #print(gen_counter, "real") 
               #real_index = gen_counter
               #y_indsreals_arr.append(real_index)
               #y_indsnans_arr.append(gen_counter - 1)               
               #nan_splice_bool = True
               #real_splice_bool = False
            #gen_counter += 1


   def generate_plots(sympy_expression, n):
      corner_x, corner_y = RenderPlayer.return_corners_xy()
      
      scale = grid_spacing
      lower_bound_y = (-1*bounds_y)/2
      upper_bound_y = bounds_y/2
     
      lower_bound_x = -10
      upper_bound_x = 10
      dispersion_points = 500
      
      #x = Symbol('x', real=True)
      
      init_printing()
      player_pos_x = (player.dx - corner_x)
      player_pos_y = (player.dy - corner_y)
      func = lambdify(x, sympy_expression, modules='numexpr', cse=True, docstring_limit=1000) #creation of a function 'func', that numerically evaluates sympy functions with the 'numexpr' code printer 
      print(func)
      x_arr = np.linspace(lower_bound_x, upper_bound_x, dispersion_points, dtype=np.complex128) #initialization of array for x coordinates
      #x_arr = np.real(x_arr)
      y_arr = np.array(func(x_arr), dtype=np.complex128)
      x_arr = np.linspace(lower_bound_x, upper_bound_x, dispersion_points, dtype=np.float64)
      y_arr_regular = np.array(func(x_arr), dtype=np.float64)
      y_arr = GeneratePlots.odd_powers(n, y_arr, y_arr_regular, x_arr, func, player_pos_y, scale)
      print(y_arr)
      try:
         print(y_arr, "hiiii")
      except TypeError as e:
         print({e})
         print("hi")
      #Strips NaNs, and INF+- values and renders functions that may possess errors, renderable
      
              
      
      #bool_y_arr = np.where(np.isnan(y_arr)) Set up an array that holds the indeces for NaN values
      y_arr[np.isnan(y_arr)] = player_pos_y
      y_arr[np.isposinf(y_arr)] = player_pos_y + upper_bound_y 
      y_arr[np.isneginf(y_arr)] = player_pos_y + lower_bound_y
      x_arr = np.real(x_arr)
      x_arr = player_pos_x + scale*x_arr
      print(x_arr)
      try:
         point_arr = np.vstack((x_arr, y_arr))
      except ValueError as e:
         print("hi")
         y_arr = np.full(len(x_arr), y_arr)
         point_arr = np.vstack((x_arr, y_arr))
      with ignore_warnings(RuntimeWarning):
        float(func(np.array([0])))
 
      return(point_arr)
   pass

