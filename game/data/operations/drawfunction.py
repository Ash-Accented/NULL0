from game.modules.modules import *
from game.data.objects.point import PointObject
from game.modules.clamp import Clamp
class DrawFunction:
   def draw_function(sympyExpression, player, screen, bounds_x, bounds_y):
      #When drawing a function, it makes sense to get the specific y values from the sympy expressionon
      point_list = []
      m = 0
      scale_x = 50
      scale_y = 50
      numpy_array_x = np.arange(-10, 10, 0.05)
      func = lambdify(x, sympyExpression, 'numpy')
      
      corner_of_screen_x = player.dx - screen.get_size()[0]/2
      corner_of_screen_y = player.dy - screen.get_size()[1]/2

      corner_of_screen_x = Clamp.clamp(corner_of_screen_x, 0, bounds_x - screen.get_size()[0])
      corner_of_screen_y = Clamp.clamp(corner_of_screen_y, 0, bounds_y - screen.get_size()[1])
      
      for i in numpy_array_x:
         
         dx = ((player.dx - corner_of_screen_x) + scale_x*i)
         dy = ((player.dy - corner_of_screen_y) - scale_y*func(i))
         point_coordinate = [dx, dy]
         point_list.append((point_coordinate))
         

      return(point_list)
   pass

