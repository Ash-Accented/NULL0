from game.modules.base_modules import *
from game.modules.preloads import *
class DrawFunction:
   
   def draw_ind_line(point_list, j):
      x_1, y_1 = point_list[0, j], point_list[1, j]
      x_2, y_2 = point_list[0, j + 1], point_list[1, j + 1]
      x_3, y_3 = point_list[0, j + 2], point_list[1, j + 2]
      x_4, y_4 = point_list[0, j + 3], point_list[1, j + 3]
      x_5, y_5 = point_list[0, j + 4], point_list[1, j + 4]
      x_6, y_6 = point_list[0, j + 5], point_list[1, j + 5]
      x_7, y_7 = point_list[0, j + 6], point_list[1, j + 6]
      x_8, y_8 = point_list[0, j + 7], point_list[1, j + 7]
      x_9, y_9 = point_list[0, j + 8], point_list[1, j + 8]
      x_10, y_10 = point_list[0, j + 9], point_list[1, j + 9]
      line_list = [(x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5), (x_6, y_6), (x_7, y_7), (x_8, y_8), (x_9, y_9), (x_10, y_10)]
      line_comb_surface = pygame.draw.lines(screen, ColorsManual.dracula_purple, False, line_list, width=3)
      return(line_comb_surface)
      
   def render_graph(point_list, enemy_rect_hitbox): #Render points through the use of this method, with x and y coordinates
      check_hit = None
      #ERROR SURFACE AND TEXT INDICATOR
      font_cmu_rm = pygame.font.Font('game/resources/fonts/cmunrm.ttf', 30)
      text_indicator = font_cmu_rm.render("", True, ColorsManual.white)
      text_indicator_pos = text_indicator.get_rect(x = (width - width//2),y = (height - 100))
      warning_surface = pygame.Surface((width, height), pygame.SRCALPHA)

      function_array = []#store rects of combined line drawings for collision detection
      length_point_list = np.size(point_list[0])
      j = 0
      while j < (length_point_list - 9):
         function_array_part = DrawFunction.draw_ind_line(point_list, j)
         function_array.append(function_array_part)
         RenderPlayer.render_player(player)
         pygame.display.flip()
         j = j + 9
         clock.tick(framerate)
         check_hit = DrawFunction.collision_detect_func(enemy_rect_hitbox, function_array)
         if check_hit:
            return(check_hit)

   pass

   def collision_detect_func(enemy_rect_hitbox, function_array):
      if (pygame.Rect.collidelist(enemy_rect_hitbox, function_array) == -1):
         check_hit = False
         return(check_hit)
      else:
         check_hit = True
         return(check_hit)
