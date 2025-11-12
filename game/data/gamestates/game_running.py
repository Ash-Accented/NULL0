import pygame #Import pygame beforehand, to allow other modules to initialize
from game.modules.modules import * #Takes from dedicated modules file for main.py
from game.data.player.player_controls import PlayerControls as PC_GAMERUN

#Generate background and enemy object



class GameRunning:
#Generate background and enemy object
   background = GridBackground.gen_background(screen)
   enemy = Enemy(1800, 900, 10, 10, 30)
   #Generate Equation used to represent the image of the equation that follows the player
   sympy_operation = 5*sin(x) 
   equation_object = EquationObject(400, 400)      #Initialize
   latex_expr, surface_image_equation, rect_surface_image_equation = GenerateFuncImage.generate_new_equation(equation_object, sympy_operation)
   

   text_disc = font_cmu_rm.render("", True, ColorsManual.red)      #Serves to hold the text with the serif roman default font style, red colored, for the purposes of reporting errors in real time
   text_disc_pos = text_disc.get_rect(x = (width//2 - 300), y = (height - 200))        #Position of text on screen
   image_list, text_image_list, text_image_pos_list = ControlOperations.controls(equation_object)      #Gets the image list of all operations performable by the player

   function_storage = [] #Stores the function pertaining to the player at any given instance
   color_default = ColorsManual.green 
   error = ""
   error_check = None
   surface_transparent = pygame.Surface((width, height), pygame.SRCALPHA)
   
   def game_ongoing():
      quit = False
      while not quit:
         GridBackground.grid_alignment(player)
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               quit = True
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                  GameRunning.function_storage, GameRunning.error, GameRunning.error_check, GameRunning.color_default, GameRunning.sympy_operation = PC_GAMERUN.player_func_draw(GameRunning.sympy_operation, GameRunning.equation_object, GameRunning.enemy, GameRunning.color_default)
                  GameRunning.latex_expr, GameRunning.surface_image_equation, GameRunning.rect_surface_image_equation = GenerateFuncImage.generate_new_equation(GameRunning.equation_object, GameRunning.sympy_operation)
               elif event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9 or event.key == pygame.K_0:
                  GameRunning.sympy_operation, GameRunning.surface_image_equation = PC_GAMERUN.player_operations(event, GameRunning.sympy_operation, GameRunning.enemy, GameRunning.equation_object, GameRunning.surface_image_equation)
         
         GameRunning.refresh_everything_in_game()
         clock.tick(framerate) #Limit the game to 60 fps, also limit physics logic
   

   def refresh_everything_in_game():
      ''''''
      keystate = pygame.key.get_pressed() #get the currently held keys 
      PlayerMovement.player_movement(keystate)
      player_rect = RenderPlayer.render_player(player) #render the player 
      EquationObject.move_equation(GameRunning.rect_surface_image_equation, GameRunning.surface_image_equation, GameRunning.equation_object)
      ControlOperations.update_controls(GameRunning.image_list, GameRunning.text_image_list, GameRunning.text_image_pos_list, GameRunning.error, GameRunning.error_check)
      enemy_rect = Enemy.draw_record_enemy(GameRunning.enemy, player_rect, GameRunning.color_default)
      MiniMap.coordinates(player_rect, GameRunning.enemy, enemy_rect)
      Hitbox.hitbox_draw(enemy_rect, player_rect)
      pygame.display.flip() #update the screen

