from game.modules.base_modules import *
from game.modules.preloads import *
class DrawFunction:
   
   def draw_ind_line(point_list, j):
      x_1, y_1 = point_list[0, j], point_list[1, j]
      x_2, y_2 = point_list[0, j + 1], point_list[1, j + 1]
      x_3, y_3 = point_list[0, j + 2], point_list[1, j + 2]
      x_4, y_4 = point_list[0, j + 3], point_list[1, j + 3]
      x_5, y_5 = point_list[0, j + 4], point_list[1, j + 4]
      line_list = [(x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5)]
      line_comb_surface = pygame.draw.lines(screen, ColorsManual.dracula_purple, False, line_list, width=3)
      return(line_comb_surface)
      
   def render_graph(point_list, screen, enemy_rect_hitbox): #Render points through the use of this method, with x and y coordinates
      check_hit = None
     

      #ERROR SURFACE AND TEXT INDICATOR
      font_cmu_rm = pygame.font.Font('game/resources/fonts/cmunrm.ttf', 30)
      text_indicator = font_cmu_rm.render("", True, ColorsManual.white)
      text_indicator_pos = text_indicator.get_rect(x = (width - width//2),y = (height - 100))
      warning_surface = pygame.Surface((width, height), pygame.SRCALPHA)

      function_array = []#store rects of combined line drawings for collision detection
      length_point_list = np.size(point_list[0])
      j = 0
      while j < (length_point_list - 4):
         function_array_part = DrawFunction.draw_ind_line(point_list, j)
         function_array.append(function_array_part)
         RenderPlayer.render_player(player)
         pygame.display.flip()
         j = j + 4
         clock.tick(framerate)

      check_hit = DrawFunction.collision_detect_func(enemy_rect_hitbox, function_array)
      return(check_hit)
   pass

   def collision_detect_func(enemy_rect_hitbox, function_array):
      if (pygame.Rect.collidelist(enemy_rect_hitbox, function_array) == -1):
         check_hit = False
         return(check_hit)
      else:
         check_hit = True
         return(check_hit)
