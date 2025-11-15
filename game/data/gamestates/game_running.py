import pygame #Import pygame beforehand, to allow other modules to initialize
from game.modules.modules import * #Takes from dedicated modules file for main.py
from game.data.player.player_controls import PlayerControls as PC_GAMERUN
from game.data.objects.randexpressions import RandExpressions
from game.data.objects.staticpoint import StaticPoint
from game.data.objects.background_origin import BackgroundOrigin
#Generate background and enemy object



class GameRunning:
#Generate background and enemy object
   background = GridBackground.gen_background()
   background_origin = BackgroundOrigin(bounds_x//2 + grid_spacing, bounds_y//2 + grid_spacing, 0, 0, 4)
   enemy = Enemy(1800, 900, 10, 10, 30)
   #Generate Equation used to represent the image of the equation that follows the player
   sympy_operation = 1/20*(x**3)
   equation_object = EquationObject(400, 400)      #Initialize
   latex_expr, surface_image_equation, rect_surface_image_equation = GenerateFuncImage.generate_new_equation(equation_object, sympy_operation)

   text_disc = font_cmu_rm.render("", True, ColorsManual.red)      #Serves to hold the text with the serif roman default font style, red colored, for the purposes of reporting errors in real time
   text_disc_pos = text_disc.get_rect(x = (width//2 - 300), y = (height - 200))        #Position of text on screen
   image_list, text_image_list, text_image_pos_list = ControlOperations.controls(equation_object)      #Gets the image list of all operations performable by the player
   rand_expr_object = RandExpressions(RandExpressions.pos_range_x_rand, RandExpressions.pos_range_y_rand, equation_object.length, equation_object.height, False)
   static_point = StaticPoint(rand_expr_object.dx, rand_expr_object.dy)
   function_storage = [] #Stores the function pertaining to the player at any given instance
   color_default = ColorsManual.green 
   error = ""
   error_check = None
   surface_transparent = pygame.Surface((width, height), pygame.SRCALPHA)
   window = window


   player_rect = RenderPlayer.render_player(player)
   enemy_rect = Enemy.draw_record_enemy(background_origin, enemy, color_default)
   surface_image_expr, expr_rect_coordinates = RandExpressions.rand_expression_generate(rand_expr_object, equation_object, player_rect)
   surface_image_expr.set_alpha(70)
   expr_rect = surface_image_expr.get_rect()
   scaled_window = pygame.Surface((window.get_size()), display_flags_window)
   player_rect_hitbox, enemy_rect_hitbox = Hitbox.hitbox_draw(enemy_rect, player_rect)
   expr_rect_hitbox = Hitbox.hitbox_draw_entity(expr_rect, (expr_rect.x, expr_rect.y))
   expr_coords = (0, 0)
   dt = pygame.time.get_ticks()/1000
   time_counter = 1

   check_collision = False
   def game_ongoing():
      quit = False
      while not quit:
         GameRunning.window.blit(window, (display_info.current_w, display_info.current_h))
         print(display_info.current_w, display_info.current_h)
         GridBackground.grid_alignment(player)
         GameRunning.check_collision = Hitbox.check_collision(GameRunning.expr_rect_hitbox, GameRunning.player_rect_hitbox)
         if GameRunning.check_collision == True:
            GameRunning.surface_image_expr.set_alpha(255)
            pygame.transform.smoothscale(GameRunning.surface_image_expr, (800, 800))
            
            window.blit(GameRunning.surface_image_expr, GameRunning.expr_coords)

         else:
            GameRunning.surface_image_expr.set_alpha(150)
            window.blit(GameRunning.surface_image_expr, GameRunning.expr_coords)
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               quit = True
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                  GameRunning.function_storage, GameRunning.error, GameRunning.error_check, GameRunning.color_default, GameRunning.sympy_operation = PC_GAMERUN.player_func_draw(GameRunning.background_origin, GameRunning.sympy_operation, GameRunning.equation_object, GameRunning.enemy, GameRunning.color_default)
                  GameRunning.latex_expr, GameRunning.surface_image_equation, GameRunning.rect_surface_image_equation = GenerateFuncImage.generate_new_equation(GameRunning.equation_object, GameRunning.sympy_operation)
               if GameRunning.check_collision == True:
                  GameRunning.surface_image_expr.set_alpha(255)
                  window.blit(GameRunning.surface_image_expr, GameRunning.expr_coords)
                  if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9 or event.key == pygame.K_0:
                     n = RandExpressions.get_rand_expr()
                     GameRunning.sympy_operation, GameRunning.surface_image_equation = PC_GAMERUN.player_operations(n, event, GameRunning.sympy_operation, GameRunning.enemy, GameRunning.equation_object, GameRunning.surface_image_equation)
                     
         player_rect = GameRunning.refresh_everything_in_game()
         GameRunning.dt = pygame.time.get_ticks()/1000
         if(GameRunning.dt >= GameRunning.time_counter*10):
            new_dx, new_dy = RandExpressions.rand_expression_regenerate()
            GameRunning.rand_expr_object.dx, GameRunning.rand_expr_object.dy = new_dx, new_dy
            GameRunning.surface_image_expr, GameRunning.expr_rect_coordinates = RandExpressions.rand_expression_generate(GameRunning.rand_expr_object, GameRunning.equation_object, player_rect)
            
            GameRunning.time_counter += 1
         clock.tick(framerate) #Limit the game to 60 fps, also limit physics logic
          

   def refresh_everything_in_game():
      ''''''
      keystate = pygame.key.get_pressed() #get the currently held keys 
      PlayerMovement.player_movement(keystate)
      player_rect = RenderPlayer.render_player(player) #render the player 
      #Use background_origin to draw the coordinates of static points along the plane
      coords_rela = BackgroundOrigin.draw_background_origin(GameRunning.background_origin, player_rect)
      GameRunning.background_origin.drx, GameRunning.background_origin.dry = coords_rela
      enemy_rect = Enemy.draw_record_enemy(GameRunning.background_origin, GameRunning.enemy, GameRunning.color_default)
      EquationObject.move_equation(GameRunning.rect_surface_image_equation, GameRunning.surface_image_equation, GameRunning.equation_object)
      ControlOperations.update_controls(GameRunning.image_list, GameRunning.text_image_list, GameRunning.text_image_pos_list, GameRunning.error, GameRunning.error_check, GameRunning.check_collision)
      MiniMap.coordinates(player_rect, GameRunning.enemy, enemy_rect)
      GameRunning.player_rect_hitbox, GameRunning.enemy_rect_hitbox = Hitbox.hitbox_draw(enemy_rect, player_rect)
      expr_rect, GameRunning.expr_coords = RandExpressions.rand_expression_coords(GameRunning.surface_image_expr, GameRunning.rand_expr_object, player_rect, GameRunning.background_origin)
      GameRunning.expr_rect_hitbox = Hitbox.hitbox_draw_entity(expr_rect, GameRunning.expr_coords)
      
      screen.blit(GameRunning.window, (0,0))
      pygame.display.flip() #update the screen
      return(player_rect)

