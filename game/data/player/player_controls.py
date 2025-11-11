import pygame
from game.modules.modules import *

class PlayerControls:
   def player_controls(event, player, sympy_operation, enemy, color_default, equation_object, surface_image_equation):
      error_check = False
      error = ""
      function_storage = []
      text_disc = font_cmu_rm.render("", True, ColorsManual.red)      #Serves to hold the text with the serif roman default font style, red colored, for the purposes of reporting errors in real time
      text_disc_pos = text_disc.get_rect(x = (width//2 - 300), y = (height - 200))        #Position of text on screen

      if event.key == pygame.K_SPACE:
         x = Symbol('x', real=True)
         try:
            function_plots = PlayerFunc.player_func_detect(sympy_operation, player)
            function_storage = function_plots
            SoundEffects.sound_effect_function_draw.play()
            player_rect = RenderPlayer.render_player(player)
            enemy_rect = Enemy.draw_record_enemy(enemy, screen, player, player_rect, color_default)
            player_rect_hitbox, enemy_rect_hitbox = Hitbox.hitbox_draw(enemy_rect, player_rect, screen)
            check_hit = DrawFunction.render_graph(function_storage, screen, enemy_rect_hitbox) #sends the updated enemy_rect to the render_graph function to check if the rect of the enemy collides with the function
            if check_hit == True:
               color_default = ColorsManual.red
               SoundEffects.sound_effect_blast.play()
               error_check = False
            elif check_hit == False:
               error = ""
               error_check = False
         except printing.codeprinter.PrintMethodNotImplementedError:
            try:
               defined_integral, err = quad(keepfunctionhere, 0, 5)
               if (math.isnan(defined_integral) == True or math.isinf(float(defined_integral)) == True):
                  SoundEffects.sound_effect_blast.play()
                  text_disc = font_cmu_rm.render("CLOSED INTEGRAL IS UNDEFINED VAL", True, (255, 0, 0))
                  error = "one"
                  screen.blit(text_disc, text_disc_pos)
                  
            except TypeError as e:
               error = "two"
               text_disc = font_cmu_rm.render("NO CLOSED FORM SOLUTION EXISTS", True, (255, 0, 0))
               screen.blit(text_disc, text_disc_pos)
         #except TypeError as e:
             #text_disc = font_cmu_rm.render("COMPLEX SOLUTIONS - NOT GRAPHING", True, (255, 0, 0))
             #screen.blit(text_disc, text_disc_pos)
             #error = "three"
             #SoundEffects.sound_effect_blast.play()
         except SyntaxError as e:
             text_disc = font_cmu_rm.render("???", True, (255, 0, 0))
             screen.blit(text_disc, text_disc_pos)
             error = "four"
             SoundEffects.sound_effect_blast.play()
      if event.key == pygame.K_1:
         SoundEffects.sound_effect_interaction.play()
         sympy_operation, surface_image_equation = OperationsSelf.operation_addition(equation_object, sympy_operation, 5)
      if event.key == pygame.K_2:
         SoundEffects.sound_effect_interaction.play()
         sympy_operation, surface_image_equation = OperationsSelf.operation_subtraction(equation_object, sympy_operation, 5)
      if event.key == pygame.K_3:
         SoundEffects.sound_effect_interaction.play()
         sympy_operation, surface_image_equation = OperationsSelf.operation_multiplication(equation_object, sympy_operation, 5)
      if event.key == pygame.K_4:
         SoundEffects.sound_effect_interaction.play()
         sympy_operation, surface_image_equation = OperationsSelf.operation_division(equation_object, sympy_operation, 0)
      if event.key == pygame.K_5:
         SoundEffects.sound_effect_interaction.play()
         sympy_operation, surface_image_equation = OperationsSelf.operation_to_power(equation_object, sympy_operation, 5)
      if event.key == pygame.K_6:
         SoundEffects.sound_effect_interaction.play()
         sympy_operation, surface_image_equation = OperationsSelf.operation_derivative(equation_object, sympy_operation)
      if event.key == pygame.K_7:
         SoundEffects.sound_effect_interaction.play()
         sympy_operation, surface_image_equation = OperationsSelf.operation_integration(equation_object, sympy_operation)
      if event.key == pygame.K_8:
         SoundEffects.sound_effect_interaction.play()
         sympy_operation, surface_image_equation = OperationsSelf.operation_exponentiated(equation_object, sympy_operation, 5)
      if event.key == pygame.K_9:
         SoundEffects.sound_effect_interaction.play()
         sympy_operation, surface_image_equation = OperationsSelf.operation_root(equation_object, sympy_operation, 5)
      if event.key == pygame.K_0:
         SoundEffects.sound_effect_interaction.play()
         sympy_operation, surface_image_equation = OperationsSelf.operation_evaluate(equation_object, sympy_operation, 10)
      return(function_storage, error, error_check, color_default, sympy_operation, surface_image_equation)
