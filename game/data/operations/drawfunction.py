from game.modules.modules import *
from game.data.objects.point import PointObject

class DrawFunction:
   def draw_function(sympyExpression, player, screen):
      #When drawing a function, it makes sense to get the specific y values from the sympy expressionon
      point_list = []
      m = 0
      scale = 100
      numpy_array_x = np.arange(-10, 10, 0.05)
      func = lambdify(x, sympyExpression, 'numpy')      
      for i in numpy_array_x:
         dx = (player.dx + scale*i)
         dy = (player.dy - func(i))
         point_coordinate = [dx, dy]
         point_list.append((point_coordinate))
         

      PointObject.render_graph(point_list, screen)
   pass

