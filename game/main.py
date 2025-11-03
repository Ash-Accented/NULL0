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

pygame.display.set_caption("spinNull0")

#REGARDLESS TO SAVE MEMORY
clock = pygame.time.Clock()
framerate = 60


#SOUND EFFECTS
sound_effect_function_draw = pygame.mixer.Sound("game/resources/sound/function_draw/functiondrawingspeddeep.wav")
sound_effect_intro_animation = pygame.mixer.Sound("game/resources/sound/ambient_noise/intro_gridline_final.wav")
sound_effect_null_robot = pygame.mixer.Sound("game/resources/sound/voice_memos/null.wav")
sound_effect_electric = pygame.mixer.Sound("game/resources/sound/ambient_noise/elec.mp3")
sound_effect_powerup = pygame.mixer.Sound("game/resources/sound/ambient_noise/powerup.wav")
sound_effect_blast = pygame.mixer.Sound("game/resources/sound/ambient_noise/blast.wav")
#FONTS PRELOADED
font_cmu_rm = pygame.font.Font('game/resources/fonts/cmunrm.ttf', 30)
font_cmu_bld = pygame.font.Font('game/resources/fonts/cmunbx.ttf', 60)




def intro_animation(screen):
   
   grid_spacing = 840 
   width, height = screen.get_size()
   backgroundIntro = pygame.Surface((width, height))
   backgroundIntro.fill((0,0,0))
   


   logo = 200
   grid_spacing_x = width // 2
   grid_spacing_y = height // 2
   distnegx = grid_spacing_x - logo
   distposx = grid_spacing_x + logo
   distnegy = grid_spacing_y - logo
   distposy = grid_spacing_y + logo 
   
   #m is the increment of lines drawn, factor_speed controls how long it takes for one line to draw
   m = 0
   factor_speed = 0.002

   #Logo Text
   text_zero = font_cmu_bld.render("NULL-0", True, (255, 255, 255)) #initialize
   text_zero_pos = text_zero.get_rect(centerx = (grid_spacing_x), y = (grid_spacing_y - 40))
   backgroundIntro.blit(text_zero, text_zero_pos)
   
   #Logo Border [diamond with boreders colored medium purple]
   medium_purple = [147, 112, 219]
   k = 0
   while k < 1:
      text_zero = font_cmu_bld.render("NULL-0", True, (k*255, k*255, k*255))
      backgroundIntro.blit(text_zero, text_zero_pos)
      pygame.draw.line( backgroundIntro, (medium_purple), (distposx, grid_spacing_y), (distposx - k*logo, distnegy + k*logo))
      pygame.draw.line( backgroundIntro, (medium_purple), (distnegx, grid_spacing_y), (distnegx + k*logo, distnegy + k*logo))
      pygame.draw.line( backgroundIntro, (medium_purple), (distposx, grid_spacing_y), (distposx - k*logo, distposy - k*logo))
      pygame.draw.line( backgroundIntro, (medium_purple), (distnegx, grid_spacing_y), (distnegx + k*logo, distposy - k*logo))
      k += factor_speed*0.25
      screen.blit(backgroundIntro, (0,0))
      pygame.display.flip()
      
   
   #Horizontal axis drawn first
   for x in range(1, width//grid_spacing_x):
      lineposx = x*grid_spacing_x
      sound_effect_powerup.play()
      k = 0
      m += 1
      red_to_white = 255
      while k < 1:
         pygame.draw.line( backgroundIntro, (red_to_white, 0, 0), (lineposx, 0), (lineposx, k*height)) 
         k += factor_speed
         screen.blit(backgroundIntro, (0,0))
         pygame.display.flip()
   m = 0
   
   text_one = font_cmu_bld.render("NULL", True, (255, 255, 255))
   text_one_pos = text_one.get_rect(centerx=(width / 2) - 400, y = (height / 2 - 200))




   for y in range(1, height//grid_spacing_y):
      lineposy = y*grid_spacing_y 
      sound_effect_powerup.play()
      k = 0
      m+=1
      
      while k < 1:
         pygame.draw.line( backgroundIntro, (red_to_white, 0, 0), (0, lineposy), (k*distnegx, lineposy) )
         k += factor_speed
         screen.blit(backgroundIntro, (0,0))
         pygame.display.flip()
         
      k = 0
      while k < 1:
         pygame.draw.line( backgroundIntro, (red_to_white, 0, 0), (distposx, lineposy), (distposx + k*distnegx, lineposy))
         k += factor_speed
         screen.blit(backgroundIntro, (0,0))
         pygame.display.flip()
 

   sound_effect_null_robot.play()
   sound_effect_electric.play()
pass

intro_animation(screen)
GridBackground.gen_background(screen)



#Creating New Equation Object, don't draw on screen  yet but initialize everything first 
equationObject = EquationObject(200, 200)

#TESTING
init_printing(use_unicode=False)
sympy_operation = (6*(sin(x)))
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
   pygame.display.flip() #update the screen















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
            

   refresh_everything_in_game()
   clock.tick(60) #Limit the game to 60 fps, also limit physics logic
    
pygame.quit()

