from game.modules.modules import *
from game.data.player.player_render import player, RenderPlayer
from game.modules.reset_surface import ResetSurface
class PointObject:
   def __init__(self, radius, dx, dy):
      self.radius = radius
      self.dx = dx
      self.dy = dy
   pass


   def render_graph(point_list, screen): #Render points through the use of this method, with x and y coordinates
      font_cmu_rm = pygame.font.Font('game/resources/fonts/cmunrm.ttf', 30)
      width, height = screen.get_size()
      j = 0 
      t = 0.0
      dt = 1/60
      issue_1 = "Woah, the mag of y..."
      text_indicator = font_cmu_rm.render("", True, (255, 255, 255))
      text_indicator_pos = text_indicator.get_rect(x = (width - width//2),y = (height - 100))
      time_warning = 0
      warning_surface = pygame.Surface((width, height), pygame.SRCALPHA)
      warning_on = False
      clock = pygame.time.Clock()
      framerate = 60
      while j < (len(point_list) - 1):

         try:
            x_1, y_1 = point_list[j]
            x_2, y_2 = point_list[j + 1]
            l_x = (x_2 - x_1)
            l_y = (y_2 - y_1)
         
            if (abs(y_1) >= 30000 or abs(y_2) >= 30000):
               warning_surface = ResetSurface.reset_surface_transparent(warning_surface)
               issue_1 = "BIG Y VAL @ (" + str(round(x_1, 5)) + ", " +  str(round(y_1, 2)) + ") AND/OR (" + str(round(x_2, 5)) + ", " + str(round(y_2, 1)) + ")"
            
               text_indicator = font_cmu_rm.render(issue_1, True, (255, 0, 0))
               warning_surface.blit(text_indicator, text_indicator_pos)
               screen.blit(warning_surface, (0, 0))
               time_warning = 30
               #print("POINT " + j + ": (" + str(round(x1, 5)) + ", " + str(round(y1, 5)) + ")") 
               #print("POINT " + j + ": (" + str(round(x1, 5)) + ", " + str(round(y1, 5)) + ")")
            else:
               pointSurface = pygame.draw.line(screen, (224, 159, 255), (x_1, y_1), (x_1 + (l_x), y_1 + (l_y)), width=3)
               
            RenderPlayer.render_player(player, screen)
            pygame.display.flip()
            if (time_warning > 0):
               time_warning -= 1 
               warning_on = True
            elif(time_warning == 0):
               warning_on = False
               warning_surface = ResetSurface.reset_surface_transparent(warning_surface)
         
         except:
             continue
         
         j = j + 1
         clock.tick(100)
   pass


