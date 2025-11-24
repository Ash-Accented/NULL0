import pygame #Import pygame beforehand, to allow other modules to initialize
from game.modules.modules import * #Takes from dedicated modules file for main.py
from game.data.player.player_controls import PlayerControls as PC_GAMERUN
from game.data.methodsandvars.update_methods import UpdateMethods, WhilstMethods
from game.data.methodsandvars.init_vars import InitializeVars
from game.data.objects.staticpoint import StaticPoint
from game.data.objects.background_origin import BackgroundOrigin
from game.data.objects.randexpressions import RandExpressions
#Generate background and enemy object



class GameRunning:
#Generate background and enemy object
   
   def game_ongoing():
      UpdateMethods.create_eq_obj()
      UpdateMethods.upd_bgo()
      UpdateMethods.create_ctrl_opra()
      UpdateMethods.create_enemy_objs(1)
      UpdateMethods.create_rand_expr_objs(InitializeVars.max_rand_expr_sprites)
      
      quit = False
      while not quit:
         InitializeVars.window.blit(window, (display_info.current_w, display_info.current_h))
         GridBackground.grid_alignment(player)
         chck, expr = WhilstMethods.check_expr_player_coll()
         
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               quit = True
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                  WhilstMethods.if_key_space()
               if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9 or event.key == pygame.K_0:
                  chck, n = WhilstMethods.check_expr_player_coll()
                  if chck and n != False:
                     GameRunning.refresh_everything_in_game()
                     PC_GAMERUN.player_operations(n.expr, event)
                     window.blit(InitializeVars.equation_sprite.sprites()[0].surf, (InitializeVars.equation_sprite.sprites()[0].rend_rect))
                     WhilstMethods.if_used_rand_expr(n.index, n.num)
         GameRunning.refresh_everything_in_game()
         InitializeVars.dt_refresh_gen = pygame.time.get_ticks()/1000
         clock.tick(framerate) #Limit the game to 60 fps, also limit physics logic
          

   def refresh_everything_in_game():
      ''''''
      keystate = pygame.key.get_pressed() #get the currently held keys 
      UpdateMethods.upd_player(keystate)
      UpdateMethods.upd_bgo()
      #Use background_origin to draw the coordinates of static points along the plane
      UpdateMethods.upd_enemy_obj()
      UpdateMethods.upd_pos_eq_obj()
      UpdateMethods.upd_rand_expr_obj()
      UpdateMethods.upd_ctrl_opra()
      UpdateMethods.upd_mm()
      UpdateMethods.upd_func()
      UpdateMethods.upd_player_clr()
      if(len(InitializeVars.rand_expr_sprites) == 0):
         UpdateMethods.create_rand_expr_objs(3)
      elif(InitializeVars.dt_refresh_gen >= InitializeVars.time_counter*1) and len(InitializeVars.rand_expr_sprites) < 3:
         objs_created = (InitializeVars.max_rand_expr_sprites) - (len(InitializeVars.rand_expr_sprites))
         list_taken = np.ndarray((InitializeVars.max_rand_expr_sprites))
         list_taken_index = np.ndarray((InitializeVars.max_rand_expr_sprites))
         index_incr = 1
         i = 0
         for obj in InitializeVars.rand_expr_sprites:
            np.append(list_taken, obj.num)
            obj.index = i
            np.append(list_taken_index, obj.index)
            i += 1
         for i in range(objs_created):
            num = (int(np.max(list_taken)) + index_incr)
            index = (int(np.max(list_taken_index)) + index_incr)
            UpdateMethods.create_rand_expr_obj(num, index)
            index_incr += 1
         InitializeVars.time_counter += 1
      screen.blit(InitializeVars.window, (0,0))
      pygame.display.flip() #update the screen
