from game.modules.modules import *
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("spinNull0")
from game.modules.clamp import Clamp 
from game.data.background.background import bounds_x, bounds_y, grid_spacing, GridBackground
from game.data.display.display import screen, display_info, display_flags
from game.data.player.player_render import player,  player_size, RenderPlayer
from game.data.player.player_movement import PlayerMovement
from game.data.objects.textbox import TextBox
from game.data.objects.equation import EquationObject
from game.data.player.player_func import PlayerFunc
from game.data.objects.point import PointObject
from game.data.operations.operationself import OperationsSelf
from game.modules.generateimage import GenerateImage
from game.modules.reset_surface import ResetSurface
from game.data.exceptions.errors import CheckFunctions
from game.data.preload.sound_effects import sound_effect_function_draw, sound_effect_intro_animation, sound_effect_null_robot, sound_effect_electric, sound_effect_powerup, sound_effect_blast, sound_effect_interaction
from game.data.preload.fonts import font_cmu_rm, font_cmu_bld
from game.data.animations.intro_animation import IntroAnimation
from game.data.gamestates.intro_skip import IntroSkip
from game.data.preload.colors import ColorsManual




#: + %s/string-in-file-to-replace/desired-string-to-insert/g + enter

#REGARDLESS TO SAVE MEMORY
clock = pygame.time.Clock()
global framerate
framerate = 60
width, height = screen.get_size()
surface_inaccessible = pygame.Surface((width, height), pygame.SRCALPHA)





def controls(equation_object, player):
   path_desired = "game/images/operations/"
   one_add = GenerateImage.render_equation_copy(equation_object, path_desired, "addition.png")
   two_subtract = GenerateImage.render_equation_copy(equation_object, path_desired, "subtraction.png")
   three_multiply = GenerateImage.render_equation_copy(equation_object, path_desired, "multiplication.png")
   four_divide = GenerateImage.render_equation_copy(equation_object, path_desired, "division.png")
   five_powered = GenerateImage.render_equation_copy(equation_object, path_desired, "powerof.png")
   six_differentiate = GenerateImage.render_equation_copy(equation_object, path_desired, "derivative.png")
   seven_integrate = GenerateImage.render_equation_copy(equation_object, path_desired, "integral.png")
   eight_exponentiate = GenerateImage.render_equation_copy(equation_object, path_desired, "exponentiated.png")
   nine_root = GenerateImage.render_equation_copy(equation_object, path_desired, "root.png")
   ten_evaluate = GenerateImage.render_equation_copy(equation_object, path_desired, "evaluated.png")
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

if (IntroSkip.intro_skip_method(screen) != "exit intro"):
   IntroAnimation.intro_animation_method(screen)

GridBackground.gen_background(screen)



#Creating New Equation Object, don't draw on screen  yet but initialize everything first 
equation_object = EquationObject(400, 400)
image_list, text_image_list, text_image_pos_list = controls(equation_object, player)

#TESTING

init_printing(use_unicode=False)
x = Symbol('x', real=True)
sympy_operation = tan(x) 
latex_expr = EquationObject.sympy_to_latex(sympy_operation)


EquationObject.latexeq_to_image(equation_object, latex_expr) #Uses the size of equationobject, gives file path
surface_image_equation = EquationObject.render_equation_copy(equation_object)
rect = surface_image_equation.get_rect()
function_storage = []
quit = False


def refresh_everything_in_game():
   keystate = pygame.key.get_pressed() #get the currently held keys
   PlayerMovement.player_movement(keystate, player, sympy_operation, screen, bounds_x, bounds_y)
   RenderPlayer.render_player(player, screen) #render the player
   EquationObject.move_equation(player, bounds_x, bounds_y, screen, rect, surface_image_equation, equation_object)
   update_controls(image_list, text_image_list, text_image_list, error, error_check)
   pygame.display.flip() #update the screen


error_check = False
def update_controls(image_list, text_image_list, text_image_pos_list, error, error_check):
   dist_between_imgs_x = 160
   perched_imgs_where_y = 100
   k = 0
   m = 0
   for image in image_list:
      rect = image.get_rect()
      rect.x = (200 + k*dist_between_imgs_x)
      rect.y = (perched_imgs_where_y)
      text_image = text_image_list[k]
      text_image_pos = text_image_pos_list[k]
      if(error != "" and error_check == False):
         if(error == "one" or error == "two"):
            l = 6
            image_list[l].set_alpha(100)
            error_check = True
         if(error == "three"):
            l = 8
            image_list[l].set_alpha(100) 
            error_check = True
      if(error == "" and error_check == True):
         image.set_alpha(255)
         error_check = False
      screen.blit(image, rect)
      k += 1












#RUNTIME

text_disc = font_cmu_rm.render("UNABLE TO GRAPH", True, (255, 0, 0))
text_disc_pos = text_disc.get_rect(x = (width//2 - 300), y = (height - 200))

def keepfunctionhere(func):
   func_integrate = sympy_operation.subs(x, func)
   return(func_integrate)

def test(func):
   func_limit = limit(func, x)
   return(func_integrate)

error = ""
while not quit:
   GridBackground.grid_alignment(player, screen)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         quit = True
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            x = Symbol('x', real=True)
            try:
               function_plots = PlayerFunc.player_func_detect(sympy_operation, player, screen, bounds_x, bounds_y)
               function_storage = function_plots
               sound_effect_function_draw.play()
               PointObject.render_graph(function_storage, screen)
               sound_effect_interaction.play()
               error = ""
            except printing.codeprinter.PrintMethodNotImplementedError:
            
               try:
                  defined_integral, err = quad(keepfunctionhere, 0, 5)
                  if (math.isnan(defined_integral) == True or math.isinf(float(defined_integral)) == True):
                     sound_effect_blast.play()
                     text_disc = font_cmu_rm.render("CLOSED INTEGRAL IS UNDEFINED VAL", True, (255, 0, 0))
                     error = "one"
                     screen.blit(text_disc, text_disc_pos)
               except TypeError as e:
                  error = "two"
                  text_disc = font_cmu_rm.render("NO CLOSED FORM SOLUTION EXISTS", True, (255, 0, 0))
                  screen.blit(text_disc, text_disc_pos)
            
            except TypeError as e:
               text_disc = font_cmu_rm.render("COMPLEX SOLUTIONS - NOT GRAPHING", True, (255, 0, 0))
               screen.blit(text_disc, text_disc_pos)
               error = "three"
               sound_effect_blast.play()
            except SyntaxError as e:
               text_disc = font_cmu_rm.render("???", True, (255, 0, 0))
               screen.blit(text_disc, text_disc_pos)
               error = "four"
               sound_effect_blast.play()
         if event.key == pygame.K_1:
            sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_addition(equation_object, sympy_operation, 5)
         if event.key == pygame.K_2:
            sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_subtraction(equation_object, sympy_operation, 5)
         if event.key == pygame.K_3:
            sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_multiplication(equation_object, sympy_operation, 5)
         if event.key == pygame.K_4:
            sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_division(equation_object, sympy_operation, 0)
         if event.key == pygame.K_5:
            sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_to_power(equation_object, sympy_operation, 5)
         if event.key == pygame.K_6:
            sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_derivative(equation_object, sympy_operation)
         if event.key == pygame.K_7:
            sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_integration(equation_object, sympy_operation)
         if event.key == pygame.K_8:
            sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_exponentiated(equation_object, sympy_operation, 5)
         if event.key == pygame.K_9:
            sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_root(equation_object, sympy_operation, 5)
         if event.key == pygame.K_0:
            sound_effect_interaction.play()
            sympy_operation, surface_image_equation = OperationsSelf.operation_evaluate(equation_object, sympy_operation, 10)
   refresh_everything_in_game()
   clock.tick(60) #Limit the game to 60 fps, also limit physics logic
    
pygame.quit()
