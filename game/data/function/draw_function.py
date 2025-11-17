from game.modules.base_modules import *
from game.modules.preloads import *
from game.data.objects.background_origin import BackgroundOrigin
from game.data.methodsandvars.init_vars import InitializeVars
from game.data.objects.staticpoint import StaticPoint
from game.data.objects.enemy import Enemy
from game.data.objects.hitboxes import Hitbox
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
      x_11, y_11 = point_list[0, j + 10], point_list[1, j + 10]
      x_12, y_12 = point_list[0, j + 11], point_list[1, j + 11]
      x_13, y_13 = point_list[0, j + 12], point_list[1, j + 12]
      x_14, y_14 = point_list[0, j + 13], point_list[1, j + 13]
      x_15, y_15 = point_list[0, j + 14], point_list[1, j + 14]
      x_16, y_16 = point_list[0, j + 15], point_list[1, j + 15]
      line_list = [(x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5), (x_6, y_6), (x_7, y_7), (x_8, y_8), (x_9, y_9), (x_10, y_10), (x_11, y_11), (x_12, y_12), (x_13, y_13), (x_14, y_14), (x_15, y_15), (x_16, y_16)]
      line_comb_surface = pygame.draw.lines(window, ColorsManual.red, False, line_list, width=3)
      return(line_comb_surface)


   def upd_enemy_obj():
      for obj in InitializeVars.enemy_sprites:
         obj.drx, obj.dry = BackgroundOrigin.rect_alignment_orig(obj, InitializeVars.background_origin)
         obj.rendered_rect = Enemy.draw_record_enemy(InitializeVars.background_origin, obj, InitializeVars.color_default)
         obj.rect = obj.rendered_rect
         obj.rendered_rect = StaticPoint.fix_drawn_rect(obj.rendered_rect)
         obj.hitbox = Hitbox.hitbox_draw_entity_circle(obj)

   def render_graph(point_list): #Render points through the use of this method, with x and y coordinates
      check_hit = None
      #ERROR SURFACE AND TEXT INDICATOR
      font_cmu_rm = pygame.font.Font('game/resources/fonts/cmunrm.ttf', 30)
      text_indicator = font_cmu_rm.render("", True, ColorsManual.white)
      text_indicator_pos = text_indicator.get_rect(x = (width - width//2),y = (height - 100))
      warning_surface = pygame.Surface((width, height), pygame.SRCALPHA)

      function_array = []#store rects of combined line drawings for collision detection
      length_point_list = np.size(point_list[0])
      j = 0
      while j < (length_point_list - 15):
         function_array_part = DrawFunction.draw_ind_line(point_list, j)
         function_array.append(function_array_part)
         player_rect = RenderPlayer.render_player(player)
         BackgroundOrigin.draw_background_origin(InitializeVars.background_origin)
         DrawFunction.upd_enemy_obj()
         check_hit = DrawFunction.collision_detect_func(function_array)
         if check_hit:
            return(check_hit)
         pygame.display.flip()
         j = j + 15
         clock.tick(framerate)
      return(check_hit)
   pass

   def collision_detect_func(function_array):
      for obj in InitializeVars.enemy_sprites:
         check_hit = False
         if pygame.Rect.collidelist(obj.hitbox, function_array) != -1:
            check_hit = True
            return(check_hit)
      return(check_hit) 
