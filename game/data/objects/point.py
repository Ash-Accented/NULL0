
from game.modules.modules import *

class PointObject:
   def __init__(self, radius, dx, dy):
      self.radius = radius
      self.dx = dx
      self.dy = dy
   pass


   def render_graph(point_list, screen): #Render points through the use of this method, with x and y coordinates
      for x, y in point_list:
         pointSurface = pygame.draw.lines(screen, (224, 159, 255), False, point_list, width=2)
   pass

    #Idea: Origin point is player's pos at the instance ==> function is solved via sympy and the subsequent y is added as an attribute, for loop of 2000 points with 

