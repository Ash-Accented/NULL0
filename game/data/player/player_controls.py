import pygame
from game.modules.modules import *
from game.data.function.generate_graph_plots import GeneratePlots
class PlayerControls:
   n = 5
   error = ""
   error_check = None
   color_default = ColorsManual.green
   text_disc = font_cmu_rm.render("", True, (255, 0, 0))
   text_disc_pos = text_disc.get_rect(x = (width//2 - 300), y = (height - 200))
   function_storage = []
   def player_operations(event, sympy_operation, enemy, equation_object, surface_image_equation):
      '''Handle key presses regarding operations done by the player, '''
      func_graphable = GeneratePlots.check_errors(sympy_operation)
      if func_graphable:
         if event.key == pygame.K_1:
            SoundEffects.sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_addition(equation_object, sympy_operation, PlayerControls.n)
         elif event.key == pygame.K_2:
            SoundEffects.sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_subtraction(equation_object, sympy_operation, PlayerControls.n)
         elif event.key == pygame.K_3:
            SoundEffects.sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_multiplication(equation_object, sympy_operation, PlayerControls.n)
         elif event.key == pygame.K_4:
            SoundEffects.sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_division(equation_object, sympy_operation, PlayerControls.n)
         elif event.key == pygame.K_5:
            SoundEffects.sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_to_power(equation_object, sympy_operation, PlayerControls.n)
         elif event.key == pygame.K_6:
            SoundEffects.sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_derivative(equation_object, sympy_operation)
         elif event.key == pygame.K_7:
            SoundEffects.sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_integration(equation_object, sympy_operation)
         elif event.key == pygame.K_8:
            SoundEffects.sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_exponentiated(equation_object, sympy_operation, PlayerControls.n)
         elif event.key == pygame.K_9:
            SoundEffects.sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_root(equation_object, sympy_operation, PlayerControls.n)
         elif event.key == pygame.K_0:
            SoundEffects.sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_evaluate(equation_object, sympy_operation, PlayerControls.n)
         return(sympy_operation, surface_image_equation)
      else:
         SoundEffects.sound_effect_error.play()
         return(sympy_operation, surface_image_equation)
   
   def player_func_draw(sympy_operation, equation_object, enemy, color_default):
      try:
         x = Symbol('x', real=True)
         function_plots = PlayerFunc.player_func_detect(sympy_operation, PlayerControls.n)
         PlayerControls.function_storage = function_plots
         SoundEffects.sound_effect_function_draw.play()
         player_rect = RenderPlayer.render_player(player)
         enemy_rect = Enemy.draw_record_enemy(enemy, player_rect, color_default)
         player_rect_hitbox, enemy_rect_hitbox = Hitbox.hitbox_draw(enemy_rect, player_rect)
         check_hit = DrawFunction.render_graph(PlayerControls.function_storage, enemy_rect_hitbox) #sends the updated enemy_rect to the render_graph function to check if the rect of the enemy collides with the function
         if check_hit == True:
            PlayerControls.color_default = ColorsManual.red
            PlayerControls.error_check = False
            PlayerControls.error = ""
            SoundEffects.sound_effect_hit.play()
         elif check_hit == False:
            PlayerControls.error = ""
            PlayerControls.error_check = False


      except printing.codeprinter.PrintMethodNotImplementedError:
         try:
            defined_integral, err = integrate(sympy_operation, (x, -2, 10))
            if (math.isnan(defined_integral) == True or math.isinf(float(defined_integral)) == True):
               SoundEffects.sound_effect_blast.play()
               PlayerControls.text_disc = font_cmu_rm.render("CLOSED INTEGRAL IS UNDEFINED VAL, RESETTING TO 1", True, (255, 0, 0))
               sympy_operation = exp(1)
               GenerateFuncImage.generate_new_equation(equation_object, sympy_operation)
               error = "one"
               screen.blit(PlayerControls.text_disc, PlayerControls.text_disc_pos)
               
                  
         except TypeError as e:
            error = "two"
            PlayerControls.text_disc = font_cmu_rm.render("NO CLOSED FORM SOLUTION EXISTS, RESETTING TO 1", True, (255, 0, 0))
            screen.blit(PlayerControls.text_disc, PlayerControls.text_disc_pos)
            sympy_operation = exp(1)
            GenerateFuncImage.generate_new_equation(equation_object, sympy_operation)
            SoundEffects.sound_effect_error.play()
            print(e)
      except TypeError as e:
         PlayerControls.text_disc = font_cmu_rm.render("COMPLEX SOLUTIONS, RESETTING TO 1", True, (255, 0, 0))
         screen.blit(PlayerControls.text_disc, PlayerControls.text_disc_pos)
         sympy_operation = exp(1)
         GenerateFuncImage.generate_new_equation(equation_object, sympy_operation)
         error = "three"
         SoundEffects.sound_effect_error.play()
         print(e)
      except SyntaxError as e:
         PlayerControls.text_disc = font_cmu_rm.render("ISSUE WITH LIBRARY, RESETTING TO 1", True, (255, 0, 0))
         screen.blit(PlayerControls.text_disc, PlayerControls.text_disc_pos)
         sympy_operation = exp(1)
         GenerateFuncImage.generate_new_equation(equation_object, sympy_operation)
         error = "four"
         SoundEffects.sound_effect_error.play()
         print(e)
      except OverflowError as e:
         PlayerControls.text_disc = font_cmu_rm.render("TOO MANY DIGITS, RESETTING TO 1", True, (255, 0, 0))
         screen.blit(PlayerControls.text_disc, PlayerControls.text_disc_pos)
         sympy_operation = exp(1)
         GenerateFuncImage.generate_new_equation(equation_object, sympy_operation)
         error = "five"
         SoundEffects.sound_effect_error.play()
         print(e)
      return(PlayerControls.function_storage, PlayerControls.error, PlayerControls.error_check, PlayerControls.color_default, sympy_operation)

