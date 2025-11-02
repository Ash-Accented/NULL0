from game.modules.modules import *


class PointObject:
   def __init__(self, radius, dx, dy):
      self.radius = radius
      self.dx = dx
      self.dy = dy
   pass


   def render_graph(point_list, screen): #Render points through the use of this method, with x and y coordinates

      j = 0
      
      while j < (len(point_list) - 1):
         x_1, y_1 = point_list[j]
         x_2, y_2 = point_list[j + 1]
         draw_factor = 0
         speed_draw = 0.001
         l_x = (x_2 - x_1)
         l_y = (y_2 - y_1)
         while draw_factor <= 1: 
         
            pointSurface = pygame.draw.line(screen, (224, 159, 255), (x_1, y_1), (x_1 + draw_factor*(l_x), y_1 + draw_factor*(l_y)), width=2)
            draw_factor += speed_draw
         pygame.display.flip()
         pygame.event.get()
         
         j = j + 1
   pass

    #Idea: Origin point is player's pos at the instance ==> function is solved via sympy and the subsequent y is added as an attribute, for loop of 2000 points with 

