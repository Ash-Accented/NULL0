from game.modules.modules import * #NOT RECCOMENDED MOST TIMES, BUT IN THIS SITUATION ITS JUST TO PREVENT 6 LINES FROM BEING WRITTEN EVERY TIME
pygame.init()
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
GridBackground.gen_background(screen)

clock = pygame.time.Clock()
framerate = 60

#Creating New Equation Object, don't draw on screen  yet but initialize everything first 
equationObject = EquationObject(200, 200)

init_printing(use_unicode=False)
sympy_operation = ((sin(x)))

latex_expr = EquationObject.sympy_to_latex(sympy_operation)

EquationObject.latexeq_to_image(equationObject, latex_expr) #Uses the size of equationobject, gives file path
surfaceImageEquation = EquationObject.render_equation_copy(equationObject)
rect = surfaceImageEquation.get_rect()
function_storage = []
quit = False


def refresh_everything():
   keystate = pygame.key.get_pressed() #get the currently held keys
   PlayerMovement.player_movement(keystate, player, sympy_operation, screen)
   RenderPlayer.render_player(player, screen) #render the player
   EquationObject.move_equation(player, bounds_x, bounds_y, screen, rect, surfaceImageEquation, equationObject)
   pygame.display.flip() #update the screen


while not quit:
   GridBackground.grid_alignment(player, screen)


   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         quit = True
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            function_plots = PlayerFunc.player_func_detect(sympy_operation, player, screen, bounds_x, bounds_y)
            function_storage = function_plots
            PointObject.render_graph(function_storage, screen)

   refresh_everything()
   clock.tick(60) #Limit the game to 60 fps, also limit physics logic
    
pygame.quit()

