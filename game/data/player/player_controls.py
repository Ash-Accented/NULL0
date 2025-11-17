import pygame
from game.modules.modules import *
from game.data.function.generate_graph_plots import GeneratePlots
from game.data.function.draw_function import DrawFunction
from game.data.methodsandvars.init_vars import InitializeVars
class PlayerControls:
   n = 5
   error = ""
   error_check = None
   color_default = ColorsManual.green
   text_disc = font_cmu_rm.render("", True, (255, 0, 0))
   text_disc_pos = text_disc.get_rect(x = (width//2 - 300), y = (height - 200))
   function_storage = []
   eq_obj_temp = 0
   def player_operations(n, event):
      PlayerControls.n = n
      '''Handle key presses regarding operations done by the player, '''
      for obj in InitializeVars.equation_sprite:
         PlayerControls.eq_obj_temp = obj
      print(PlayerControls.eq_obj_temp.expr, PlayerControls.eq_obj_temp.latex)
      func_graphable = GeneratePlots.check_errors(PlayerControls.eq_obj_temp.expr)
      if func_graphable:
         if event.key == pygame.K_1:
            operation_num = 1
         elif event.key == pygame.K_2:
            operation_num = 2
         elif event.key == pygame.K_3:
            operation_num = 3
         elif event.key == pygame.K_4:
            operation_num = 4
         elif event.key == pygame.K_5:
            operation_num = 5
         elif event.key == pygame.K_6:
            operation_num = 6
         elif event.key == pygame.K_7:
            operation_num = 7
         elif event.key == pygame.K_8:
            operation_num = 8
         elif event.key == pygame.K_9:
            operation_num = 9
         elif event.key == pygame.K_0:
            operation_num = 10
         SoundEffects.sound_effect_edit_func.play()
         PlayerControls.eq_obj_temp.expr, PlayerControls.eq_obj_temp.surf = OperationsSelf.operation_equation(PlayerControls.eq_obj_temp, PlayerControls.n, operation_num)
         PlayerControls.eq_obj_temp.latex, PlayerControls.eq_obj_temp.surf, PlayerControls.eq_obj_temp.rend_rect = EquationObject.generate_new_equation(PlayerControls.eq_obj_temp)
         InitializeVars.equation_sprite.sprites()[0] = PlayerControls.eq_obj_temp

         print(PlayerControls.eq_obj_temp.expr, PlayerControls.eq_obj_temp.latex)
      else:
         SoundEffects.sound_effect_error.play()
         return(PlayerControls.eq_obj_temp.expr, PlayerControls.eq_obj_temp.surf)
   
   def player_func_draw(eq_obj, enemy, color_default):
      try:
         PlayerControls.function_storage, PlayerControls.error, PlayerControls.error_check, PlayerControls.color_default, eq_obj.expr = PlayerControls.draw_func(eq_obj.expr, eq_obj.expr, enemy, color_default)
      except printing.codeprinter.PrintMethodNotImplementedError:
         try:
            defined_integral, err = integrate(eq_obj.expr, (x, -2, 10))
            if (math.isnan(defined_integral) == True or math.isinf(float(defined_integral)) == True):
               SoundEffects.sound_effect_blast.play()
               PlayerControls.text_disc = font_cmu_rm.render("CLOSED INTEGRAL IS UNDEFINED VAL, RESETTING TO 1", True, (255, 0, 0))
               eq_obj.expr = exp(1)
               GenerateFuncImage.generate_new_equation(equation_object, eq_obj.expr)
               error = "one"
               window.blit(PlayerControls.text_disc, PlayerControls.text_disc_pos)
               
                  
         except TypeError as e:
            error = "two"
            PlayerControls.text_disc = font_cmu_rm.render("NO CLOSED FORM SOLUTION EXISTS, RESETTING TO 1", True, (255, 0, 0))
            window.blit(PlayerControls.text_disc, PlayerControls.text_disc_pos)
            eq_obj.expr = exp(1)
            GenerateFuncImage.generate_new_equation(equation_object, eq_obj.expr)
            SoundEffects.sound_effect_error.play()
            print(e)
      except TypeError as e:
         PlayerControls.text_disc = font_cmu_rm.render("COMPLEX SOLUTIONS, RESETTING TO 1", True, (255, 0, 0))
         window.blit(PlayerControls.text_disc, PlayerControls.text_disc_pos)
         eq_obj.expr = exp(1)
         EquationObject.generate_new_equation(eq_obj)
         error = "three"
         SoundEffects.sound_effect_error.play()
         print(e)
      except SyntaxError as e:
         PlayerControls.text_disc = font_cmu_rm.render("ISSUE WITH LIBRARY, RESETTING TO 1", True, (255, 0, 0))
         window.blit(PlayerControls.text_disc, PlayerControls.text_disc_pos)
         eq_obj.expr = exp(1)
         EquationObject.generate_new_equation(eq_obj)
         error = "four"
         SoundEffects.sound_effect_error.play()
         print(e)
      except OverflowError as e:
         PlayerControls.text_disc = font_cmu_rm.render("TOO MANY DIGITS, RESETTING TO 1", True, (255, 0, 0))
         window.blit(PlayerControls.text_disc, PlayerControls.text_disc_pos)
         eq_obj.expr = exp(1)
         EquationObject.generate_new_equation(eq_obj)
         error = "five"
         SoundEffects.sound_effect_error.play()
         print(e)
      except KeyError as e:
         print(e)
         expr = N(eq_obj.expr, 8)
         PlayerControls.function_storage, PlayerControls.error, PlayerControls.error_check, PlayerControls.color_default, eq_obj.expr = PlayerControls.draw_func(expr, eq_obj.expr, enemy, color_default)
         print(e) 
            


      return(PlayerControls.function_storage, PlayerControls.error, PlayerControls.error_check, PlayerControls.color_default, eq_obj.expr)

   def draw_func(expr, eq_expr, enemy_list, color_default):
      x = Symbol('x', real=True)
      function_plots = PlayerFunc.player_func_detect(expr, PlayerControls.n)
      PlayerControls.function_storage = function_plots
      SoundEffects.sound_effect_function_draw.play()
      player.rendered_rect = RenderPlayer.render_player(player)
      player.hitbox = Hitbox.hitbox_draw_entity_circle(player)
      check_hit = DrawFunction.render_graph(PlayerControls.function_storage) #sends the updated enemy_rect to the render_graph function to check if the rect of the enemy collides with the function
      if check_hit:
         PlayerControls.color_default = ColorsManual.red
         PlayerControls.error_check = False
         PlayerControls.error = ""
         SoundEffects.sound_effect_hit.play()
      elif check_hit == False:
         PlayerControls.error = ""
         PlayerControls.error_check = False
      return(PlayerControls.function_storage, PlayerControls.error, PlayerControls.error_check, PlayerControls.color_default, eq_expr)
