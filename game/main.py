from game.modules.modules import * #NOT RECCOMENDED MOST TIMES, BUT IN THIS SITUATION ITS JUST TO PREVENT 6 LINES FROM BEING WRITTEN EVERY TIME
pygame.init()
pygame.mixer.init()
from game.modules.clamp import Clamp
from game.data.background.background import bounds_x, bounds_y, grid_spacing, GridBackground
from game.data.display.display import screen, display_info, display_flags
from game.data.player.player_render import player, player_size, RenderPlayer
from game.data.player.player_movement import PlayerMovement
from game.data.objects.textbox import TextBox
from game.data.objects.equation import EquationObject
from game.data.player.player_func import PlayerFunc
from game.data.objects.point import PointObject
from game.data.operations.operationself import OperationsSelf
from game.modules.generateimage import GenerateImage
from game.modules.reset_surface import ResetSurface
from game.data.exceptions.errors import CheckFunctions
pygame.display.set_caption("spinNull0")

#REGARDLESS TO SAVE MEMORY
clock = pygame.time.Clock()
global framerate
framerate = 60
width, height = screen.get_size()
surface_inaccessible = pygame.Surface((width, height), pygame.SRCALPHA)

#SOUND EFFECTS
sound_effect_function_draw = pygame.mixer.Sound("game/resources/sound/function_draw/functiondrawingspeddeep.wav")
sound_effect_intro_animation = pygame.mixer.Sound("game/resources/sound/ambient_noise/intro_gridline_final.wav")
sound_effect_null_robot = pygame.mixer.Sound("game/resources/sound/voice_memos/null.wav")
sound_effect_electric = pygame.mixer.Sound("game/resources/sound/ambient_noise/elec.mp3")
sound_effect_powerup = pygame.mixer.Sound("game/resources/sound/ambient_noise/powerup.wav")
sound_effect_blast = pygame.mixer.Sound("game/resources/sound/ambient_noise/blast.wav")
sound_effect_interaction = pygame.mixer.Sound("game/resources/sound/menu_click/menuclick.wav")
#FONTS PRELOADED
font_cmu_rm = pygame.font.Font('game/resources/fonts/cmunrm.ttf', 30)
font_cmu_bld = pygame.font.Font('game/resources/fonts/cmunbx.ttf', 60)



def intro_animation(screen):
   grid_spacing = 840 
   width, height = screen.get_size()
   backgroundIntro = pygame.Surface((width, height))
   backgroundIntro.fill((50,50,50))
   running = True
   grid_spacing_x = width // 2
   grid_spacing_y = height // 2
   
   if running == True:
      logo = 200
      distnegx = grid_spacing_x - logo
      distposx = grid_spacing_x + logo
      distnegy = grid_spacing_y - logo
      distposy = grid_spacing_y + logo 
      default_pos = (0, 0)
      #m is the increment of lines drawn, factor_speed controls how long it takes for one line to draw
      m = 0
      factor_speed = 0.00555 #3 seconds for the k<1 events
      amplifier = 3
   #Logo Text
     
      text_disc = font_cmu_rm.render("PRESS ESC KEY TO SKIP", True, (255, 255, 255))
      text_disc_pos = text_disc.get_rect(x = (grid_spacing_x - 300), y = (2*grid_spacing_y - 200))

      text_zero = font_cmu_bld.render("NULL0", True, (255, 255, 255)) #initialize
      text_zero_pos = text_zero.get_rect(centerx = (grid_spacing_x), y = (grid_spacing_y - 40))
      #backgroundIntro.blit(text_zero, text_zero_pos)
   
   #Logo Border [diamond with boreders colored medium purple]
      medium_purple = [147, 112, 219]
      k = 0
      time_surface = pygame.Surface((width, height))
      while k < 1:
         text_disc = font_cmu_rm.render("PRESS ESC KEY TO SKIP", True, (k*255, k*255, k*255))
         text_disc_pos = text_disc.get_rect(x = (grid_spacing_x - 175),y = (height//1 - 100 ))
         j = str(round(3*(1 - k), 4))
         
         text_time_left = font_cmu_rm.render(j, True, (255, 255, 255))
         text_time_left_pos = text_time_left.get_rect(x = (grid_spacing_x + grid_spacing_x//1.2),y = grid_spacing_y//7)
         time_surface.blit(text_disc, text_disc_pos)
         time_surface.blit(text_time_left, text_time_left_pos)
         k += factor_speed
         screen.blit(time_surface, default_pos) 
         pygame.display.flip()
         for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                  pygame.event.clear()
                  return("exit intro")
         clock.tick(framerate)
         ResetSurface.reset_surface_opaque(time_surface, (0, 0, 0))








      ResetSurface.reset_surface_opaque(backgroundIntro, (0, 0, 0))
      k = 0
      
      sound_effect_null_robot.play()
      while k < 1:
         
         text_zero = font_cmu_bld.render("NULL0", True, (k*255, k*255, k*255))
         backgroundIntro.blit(text_zero, text_zero_pos)
         
         pygame.draw.line( backgroundIntro, (medium_purple), (distposx, grid_spacing_y), (distposx - k*logo, distnegy + k*logo))
         pygame.draw.line( backgroundIntro, (medium_purple), (distnegx, grid_spacing_y), (distnegx + k*logo, distnegy + k*logo))
         pygame.draw.line( backgroundIntro, (medium_purple), (distposx, grid_spacing_y), (distposx - k*logo, distposy - k*logo))
         pygame.draw.line( backgroundIntro, (medium_purple), (distnegx, grid_spacing_y), (distnegx + k*logo, distposy - k*logo))
         k += factor_speed
         screen.blit(backgroundIntro, (0,0))
         pygame.display.flip()
         clock.tick(framerate)
   #Horizontal axis drawn first
      for x in range(1, width//grid_spacing_x):
         lineposx = x*grid_spacing_x
         sound_effect_powerup.play()
         k = 0
         m += 1
         red_to_white = 255
         while k < 1:
            pygame.draw.line( backgroundIntro, (red_to_white, 0, 0), (lineposx, 0), (lineposx, k*height)) 
            k += factor_speed*amplifier
            screen.blit(backgroundIntro, (0,0))
            pygame.display.flip()
            clock.tick(framerate)
      m = 0

      for y in range(1, height//grid_spacing_y):
         lineposy = y*grid_spacing_y 
         sound_effect_powerup.play()
         k = 0
         m+=1
      
      while k < 1:
         pygame.draw.line( backgroundIntro, (red_to_white, 0, 0), (0, lineposy), (k*distnegx, lineposy) )
         k += factor_speed*amplifier
         screen.blit(backgroundIntro, (0,0))
         pygame.display.flip()
         clock.tick(framerate)
         
      k = 0
      while k < 1:
         pygame.draw.line( backgroundIntro, (red_to_white, 0, 0), (distposx, lineposy), (distposx + k*distnegx, lineposy))
         k += factor_speed*amplifier
         screen.blit(backgroundIntro, (0,0))
         pygame.display.flip()
         clock.tick(framerate) 

      sound_effect_blast.play()
      intro_animation
      pygame.event.clear()

pass


def controls(equationObject, player):
   path_desired = "game/images/operations/"
   one_add = GenerateImage.render_equation_copy(equationObject, path_desired, "addition.png")
   two_subtract = GenerateImage.render_equation_copy(equationObject, path_desired, "subtraction.png")
   three_multiply = GenerateImage.render_equation_copy(equationObject, path_desired, "multiplication.png")
   four_divide = GenerateImage.render_equation_copy(equationObject, path_desired, "division.png")
   five_powered = GenerateImage.render_equation_copy(equationObject, path_desired, "powerof.png")
   six_differentiate = GenerateImage.render_equation_copy(equationObject, path_desired, "derivative.png")
   seven_integrate = GenerateImage.render_equation_copy(equationObject, path_desired, "integral.png")
   eight_exponentiate = GenerateImage.render_equation_copy(equationObject, path_desired, "exponentiated.png")
   nine_root = GenerateImage.render_equation_copy(equationObject, path_desired, "root.png")
   ten_evaluate = GenerateImage.render_equation_copy(equationObject, path_desired, "evaluated.png")
   image_list = [one_add, two_subtract, three_multiply, four_divide, five_powered, six_differentiate, seven_integrate, eight_exponentiate, nine_root, ten_evaluate]
   rect = one_add.get_rect()
   i = 1
   text_image_list = []
   text_image_pos_list = []
   for image in image_list:
      
      j = str(i)
      i += 1
      text_image = font_cmu_bld.render(j, True, (255, 255, 255))
      text_image_pos = text_image.get_rect(x = (rect.x - 100), y = rect.y)
      text_image_list.append(text_image)
      text_image_pos_list.append(text_image_pos)
   return(image_list, text_image_list, text_image_pos_list)

intro_animation(screen)
GridBackground.gen_background(screen)



#Creating New Equation Object, don't draw on screen  yet but initialize everything first 
equationObject = EquationObject(200, 200)
image_list, text_image_list, text_image_pos_list = controls(equationObject, player)

#TESTING
init_printing(use_unicode=False)
sympy_operation = 6*sin(x)
latex_expr = EquationObject.sympy_to_latex(sympy_operation)


EquationObject.latexeq_to_image(equationObject, latex_expr) #Uses the size of equationobject, gives file path
surfaceImageEquation = EquationObject.render_equation_copy(equationObject)
rect = surfaceImageEquation.get_rect()
function_storage = []
quit = False


def refresh_everything_in_game():
   keystate = pygame.key.get_pressed() #get the currently held keys
   PlayerMovement.player_movement(keystate, player, sympy_operation, screen, bounds_x, bounds_y)
   RenderPlayer.render_player(player, screen) #render the player
   EquationObject.move_equation(player, bounds_x, bounds_y, screen, rect, surfaceImageEquation, equationObject)
   update_controls(image_list, text_image_list, text_image_list)
   pygame.display.flip() #update the screen


def update_controls(image_list, text_image_list, text_image_pos_list):
   dist_between_imgs_x = 160
   perched_imgs_where_y = 100
   k = 0
   for image in image_list:
      rect = image.get_rect()
      rect.x = (200 + k*dist_between_imgs_x)
      rect.y = (perched_imgs_where_y)
      text_image = text_image_list[k]
      text_image_pos = text_image_pos_list[k]
      screen.blit(image, rect)
      k += 1












#RUNTIME


while not quit:
   GridBackground.grid_alignment(player, screen)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         quit = True
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            function_plots = PlayerFunc.player_func_detect(sympy_operation, player, screen, bounds_x, bounds_y)
            function_storage = function_plots
            sound_effect_function_draw.play()
            PointObject.render_graph(function_storage, screen)
            sound_effect_interaction.play()

         if event.key == pygame.K_1:
            sound_effect_interaction.play()
            sympy_operation, surfaceImageEquation = OperationsSelf.operation_addition(equationObject, sympy_operation, 5)
         if event.key == pygame.K_2:
            sound_effect_interaction.play()
            sympy_operation, surfaceImageEquation = OperationsSelf.operation_subtraction(equationObject, sympy_operation, 5)
         if event.key == pygame.K_3:
            sound_effect_interaction.play()
            sympy_operation, surfaceImageEquation = OperationsSelf.operation_multiplication(equationObject, sympy_operation, 5)
         if event.key == pygame.K_4:
            sound_effect_interaction.play()
            sympy_operation, surfaceImageEquation = OperationsSelf.operation_division(equationObject, sympy_operation, 5)
         if event.key == pygame.K_5:
            sound_effect_interaction.play()
            sympy_operation, surfaceImageEquation = OperationsSelf.operation_to_power(equationObject, sympy_operation, 5)
         if event.key == pygame.K_6:
            sound_effect_interaction.play()
            sympy_operation, surfaceImageEquation = OperationsSelf.operation_derivative(equationObject, sympy_operation)
         if event.key == pygame.K_7:
            sound_effect_interaction.play()
            sympy_operation, surfaceImageEquation = OperationsSelf.operation_integration(equationObject, sympy_operation)
         if event.key == pygame.K_8:
            sound_effect_interaction.play()
            sympy_operation, surfaceImageEquation = OperationsSelf.operation_exponentiated(equationObject, sympy_operation, 5)
         if event.key == pygame.K_9:
            sound_effect_interaction.play()
            sympy_operation, surfaceImageEquation = OperationsSelf.operation_root(equationObject, sympy_operation, 5)
         if event.key == pygame.K_0:
            sound_effect_interaction.play()
            sympy_operation, surfaceImageEquation = OperationsSelf.operation_evaluate(equationObject, sympy_operation, 10)
   refresh_everything_in_game()
   clock.tick(60) #Limit the game to 60 fps, also limit physics logic
    
pygame.quit()
