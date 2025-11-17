import pygame #Import pygame beforehand, to allow other modules to initialize
from game.modules.modules import * #Takes from dedicated modules file for main.py
from game.data.methodsandvars.init_vars import InitializeVars
from game.data.player.player_controls import PlayerControls as PC_GAMERUN
from game.data.objects.staticpoint import StaticPoint
from game.data.objects.background_origin import BackgroundOrigin
from game.data.objects.control_operations import ControlOperations
from game.data.objects.randexpressions import RandExpressions as RE




###############################################################################################

class UpdateMethods:
   def upd_mm():
      MiniMap.coordinates()
   def upd_bgo():
      InitializeVars.background_origin = BackgroundOrigin.draw_background_origin(InitializeVars.background_origin)
   def create_eq_obj():
      eq_obj = EquationObject(400, 400)
      eq_obj.expr = player.character
      eq_obj.character = player.character
      eq_obj.latex, eq_obj.surf, eq_obj.rend_rect = EquationObject.generate_new_equation(eq_obj)
      InitializeVars.equation_sprite.add(eq_obj)
   def upd_pos_eq_obj():
      for obj in InitializeVars.equation_sprite:
         EquationObject.move_equation(obj)
   def create_ctrl_opra():
      ctrl_obj = ControlOperations(400, 400)
      InitializeVars.ctrl_opra_sprite.add(ctrl_obj)
      
   def upd_ctrl_opra():
      ctrl_obj = InitializeVars.ctrl_opra_sprite.sprites()[0]
      ControlOperations.update_controls(ctrl_obj, InitializeVars.error, InitializeVars.error_check, InitializeVars.check_collision)
      InitializeVars.ctrl_opra_sprite.sprites()[0] = ctrl_obj
   def create_enemy_objs(objs):
      for i in range(objs):
        enemy_obj = Enemy(random.randrange(100, 1800), random.randrange(100, 1800), 30)
        enemy_obj.drx, enemy_obj.dry = BackgroundOrigin.rect_alignment_orig(enemy_obj, InitializeVars.background_origin)
        enemy_obj.rendered_rect = pygame.draw.circle(window, ColorsManual.red, (enemy_obj.w, enemy_obj.h), enemy_obj.r)
        enemy_obj.rend_rect = StaticPoint.fix_drawn_rect(enemy_obj.rend_rect)
        enemy_obj.hitbox = Hitbox.hitbox_draw_entity(enemy_obj)
        InitializeVars.enemy_sprites.add(enemy_obj)
   
   def create_rand_expr_objs(objs):
      for i in range(objs):
         rand_expr_obj = RE(100, 100, i, i)
         rand_expr_obj.dx, rand_expr_obj.dy = RE.rand_expression_regenerate()
         rand_expr_obj.expr, rand_expr_obj.surf, rand_expr_obj.drx, rand_expr_obj.dry, rand_expr_obj.rect = RE.rand_expression_generate(rand_expr_obj)
         rand_expr_obj.hitbox = Hitbox.hitbox_draw_entity(rand_expr_obj)
         rand_expr_obj.surf.set_alpha(70)
         InitializeVars.window.blit(rand_expr_obj.surf, (rand_expr_obj.drx, rand_expr_obj.dry))
         InitializeVars.rand_expr_sprites.add(rand_expr_obj)

   def create_rand_expr_obj(num, index):
      rand_expr_obj = RE(100, 100, num, index)
      rand_expr_obj.dx, rand_expr_obj.dy = RE.rand_expression_regenerate()
      rand_expr_obj.expr, rand_expr_obj.surf, rand_expr_obj.drx, rand_expr_obj.dry, rand_expr_obj.rect = RE.rand_expression_generate(rand_expr_obj)
      rand_expr_obj.hitbox = Hitbox.hitbox_draw_entity(rand_expr_obj)
      rand_expr_obj.surf.set_alpha(70)
      InitializeVars.window.blit(rand_expr_obj.surf, (rand_expr_obj.drx, rand_expr_obj.dry))
      InitializeVars.rand_expr_sprites.add(rand_expr_obj)
          
   def upd_rand_expr_obj():
      for obj in InitializeVars.rand_expr_sprites:
         obj.drx, obj.dry = BackgroundOrigin.rect_alignment_orig(obj, InitializeVars.background_origin)
         print(obj.expr)
         obj.surf.set_alpha(70)
         obj.hitbox = Hitbox.hitbox_draw_entity(obj)
         InitializeVars.window.blit(obj.surf, (obj.drx, obj.dry))

   def upd_enemy_obj():
      for obj in InitializeVars.enemy_sprites:
         obj.drx, obj.dry = BackgroundOrigin.rect_alignment_orig(obj, InitializeVars.background_origin)
         obj.rendered_rect = Enemy.draw_record_enemy(InitializeVars.background_origin, obj, InitializeVars.color_default)
         obj.rect = obj.rendered_rect
         obj.rendered_rect = StaticPoint.fix_drawn_rect(obj.rendered_rect)
         obj.hitbox = Hitbox.hitbox_draw_entity_circle(obj)

   def upd_player_clr():
      if player.character == pi:
         player.color = ColorsManual.blue_pi
         player.color_eq = ColorsManual.blue_pi_eq
      elif player.character == exp(1):
         player.color = ColorsManual.sage_e
         player.color_eq = ColorsManual.sage_e_eq
      elif player.character == root(2, 2):
         player.color = ColorsManual.purp_root
         player.color_eq = ColorsManual.purp_root_eq
      elif player.character == GoldenRatio:
         player.color = ColorsManual.amber_gr
         player.color_eq = ColorsManual.amber_gr_eq
   def upd_player(keystate):
      PlayerMovement.player_movement(keystate)
      k = 0.25
      line_y_axis = pygame.draw.line(window, (k*player.color[0], k*player.color[1], k*player.color[2]), (player.drx, player.dry + 250), (player.drx, player.dry - 250))
      for i in range(-4, 5):
         lines_x = pygame.draw.line(window, (k*player.color[0], k*player.color[1], k*player.color[2]), (player.drx + i*grid_spacing, player.dry + grid_spacing//4), (player.drx + i*grid_spacing, player.dry))
         lines_y = pygame.draw.line(window, (k*player.color[0], k*player.color[1], k*player.color[2]), (player.drx + grid_spacing//4, player.dry + i*grid_spacing), (player.drx, player.dry + i*grid_spacing)) 
      line_x_axis = pygame.draw.line(window, (k*player.color[0], k*player.color[1], k*player.color[2]), (player.drx + 250, player.dry), (player.drx - 250, player.dry))

      player.rendered_rect = RenderPlayer.render_player(player)
      player.drx, player.dry = player.rendered_rect.x, player.rendered_rect.y
      player.hitbox = Hitbox.hitbox_draw_entity_circle(player)
   def upd_player_hitbox():
      player.rendered_rect = RenderPlayer.render_player(player)
      player.hitbox = Hitbox.hitbox_draw_entity_circle(player)
   def upd_func():
      k = 0.4
      eq = InitializeVars.equation_sprite.sprites()[0]
      corner_x, corner_y = RenderPlayer.return_corners_xy()
      player_pos_x = (player.dx - corner_x)
      player_pos_y = (player.dy - corner_y)
      
      lwr_bound_x = -5
      uppr_bound_x = 10
      lwr_bound_y = 1
      uppr_bound_y = -1
      disp = 50
      try:
         point_list = GeneratePlots.generate_plots(eq.expr, 1, lwr_bound_x, uppr_bound_x, lwr_bound_y, uppr_bound_y, disp) #
         for i in range(0, (len(point_list[0,]) - 20)):
            x1, y1 = point_list[0, i], point_list[1, i]
            line_comb_surface = pygame.draw.circle(window, (k*255, 0, 0), (x1, y1), 1)
      except KeyError as e:
         try:
            expr = N(eq.expr, 8)
            point_list = GeneratePlots.generate_plots(expr, 1, lwr_bound_x, uppr_bound_x, lwr_bound_y, uppr_bound_y, disp) #
            for i in range(0, (len(point_list[0,]) - 20)):
               x1, y1 = point_list[0, i], point_list[1, i]
               line_comb_surface = pygame.draw.circle(window, (k*255, 0, 0), (x1, y1), 1)
         except KeyError as e:
            eq.expr = eq.character
            EquationObject.generate_new_equation(eq)
            SoundEffects.sound_effect_error.play()
            print(e)

      except SyntaxError as e:
         eq.expr = eq.character
         EquationObject.generate_new_equation(eq)
         SoundEffects.sound_effect_error.play()
         print(e) 
      except OverflowError as e:
         window.blit(PlayerControls.text_disc, PlayerControls.text_disc_pos)
         eq_obj.expr = eq.character
         EquationObject.generate_new_equation(eq)
         SoundEffects.sound_effect_error.play()
         print(e)
      except TypeError as e:
         window.blit(PlayerControls.text_disc, PlayerControls.text_disc_pos)
         eq.expr = eq.character
         EquationObject.generate_new_equation(eq)
         SoundEffects.sound_effect_error.play()
         print(e)
##########################################################################################




class WhilstMethods:
   def check_expr_player_coll():
      UpdateMethods.upd_rand_expr_obj()
      UpdateMethods.upd_player_hitbox()
      screen.blit(InitializeVars.window, (0, 0))
      
      for expr in InitializeVars.rand_expr_sprites:
         expr.collide = Hitbox.check_collision(expr, player)
         if expr.collide:
            expr.surf.set_alpha(255)
            InitializeVars.window.blit(expr.surf, (expr.drx, expr.dry))
            return(expr.collide, expr)
         else:
            expr.surf.set_alpha(70)
            InitializeVars.window.blit(expr.surf, (expr.drx, expr.dry))
      return(expr.collide, False)
   def if_key_space():
      SoundEffects.sound_effect_function_draw.play()
      eq_obj = InitializeVars.equation_sprite.sprites()[0]
      InitializeVars.function_storage, InitializeVars.error, InitializeVars.error_check, InitializeVars.color_default, eq_obj.expr  = PC_GAMERUN.player_func_draw(eq_obj, InitializeVars.enemy_sprites, InitializeVars.color_default)
      eq_obj.latex, eq_obj.surf, eq_obj.rend_rect = EquationObject.generate_new_equation(eq_obj)
      InitializeVars.equation_sprite.sprites()[0] = eq_obj

   def if_used_rand_expr(index, num):
      rand_expr_sprite = InitializeVars.rand_expr_sprites.sprites()[index]
      os.remove("game/images/randomexpressions/temp" + str(num))
      InitializeVars.rand_expr_sprites.remove(rand_expr_sprite)
   
