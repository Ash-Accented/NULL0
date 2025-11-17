from game.modules.base_modules import *
from game.modules.preloads import *
from game.data.objects.background_origin import BackgroundOrigin
from game.data.methodsandvars.init_vars import InitializeVars
from game.data.objects.staticpoint import StaticPoint
from game.data.objects.enemy import Enemy
from game.data.objects.hitboxes import Hitbox
from game.data.player.player_movement import PlayerMovement
class DrawFunction:
  
   def draw_axes(point_list):
      k = 0
      line_list = []
      for i in range(0, (len(point_list[0,]) - 20)):
         x1, y1 = point_list[0, i], point_list[1, i]
         line_comb_surface = pygame.draw.circle(window, (255, 0, 0), (x1, y1), 1)
         
      while k < 0.9:
         player.rendered_rect = RenderPlayer.render_player(player)
         BackgroundOrigin.draw_background_origin(InitializeVars.background_origin)
         DrawFunction.upd_enemy_obj()
         k += 0.05
         line_y_axis = pygame.draw.line(window, (k*player.color[0], k*player.color[1], k*player.color[2]), (player.drx, player.dry + 250), (player.drx, player.dry - 250))
         for i in range(-4, 5):
            lines_x = pygame.draw.line(window, (k*player.color[0], k*player.color[1], k*player.color[2]), (player.drx + i*grid_spacing, player.dry + grid_spacing//4), (player.drx + i*grid_spacing, player.dry))
            lines_y = pygame.draw.line(window, (k*player.color[0], k*player.color[1], k*player.color[2]), (player.drx + grid_spacing//4, player.dry + i*grid_spacing), (player.drx, player.dry + i*grid_spacing)) 
         line_x_axis = pygame.draw.line(window, (k*player.color[0], k*player.color[1], k*player.color[2]), (player.drx + 250, player.dry), (player.drx - 250, player.dry))
         clock.tick(framerate)
         pygame.display.flip()
   def draw_ind_line(point_list, j):
      line_list = []
      for i in range(0, 13):
         x_1, y_1 = point_list[0, j + i], point_list[1, j + i]
         x_2, y_2 = point_list[0, j + i + 1], point_list[1, j + i + 1]
         d_x_2 = x_2 - x_1
         d_y_2 = y_2 - y_1
         if (abs(d_y_2) < 2000):
            line_list.append((x_1, y_1))
         else:
            line_comb_surface = pygame.draw.circle(window, player.color, (x_1, y_1), 2)
      try:
         line_comb_surface = pygame.draw.lines(window, (player.color), False, line_list, width=4)
      except ValueError as e:
         print(e)
         for i in range(0, 13):
            x1, y1 = point_list[0, i], point_list[1, i]
            line_comb_surface = pygame.draw.circle(window, player.color, (x1, y1), 2)
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
      
      DrawFunction.draw_axes(point_list)
      while j < (length_point_list - 12):
         function_array_part = DrawFunction.draw_ind_line(point_list, j)
         function_array.append(function_array_part)
         player_rect = RenderPlayer.render_player(player)
         BackgroundOrigin.draw_background_origin(InitializeVars.background_origin)
         DrawFunction.upd_enemy_obj()
         check_hit = DrawFunction.collision_detect_func(function_array)
         if check_hit:
            return(check_hit)
         pygame.display.flip()
         j = j + 12
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
