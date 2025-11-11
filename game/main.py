import pygame #Import pygame beforehand, to allow other modules to initialize
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("NULL0")
from game.modules.modules import * #Takes from dedicated modules file for main.py
from game.data.player.player_controls import PlayerControls as PC_MAIN



surface_transparent = pygame.Surface((width, height), pygame.SRCALPHA)

#Start @ skippable section of intro before playing intro animation, only skips if ESC key is pressed
if (IntroSkip.intro_skip_method(screen) != "exit intro"):
   IntroAnimation.intro_animation_method()
   PlayerControls.player_controls(event, player)
#Generate background and enemy object
background = GridBackground.gen_background(screen)
enemy = Enemy(1800, 900, 10, 10, 30)

#Generate Equation used to represent the image of the equation that follows the player
equation_object = EquationObject(400, 400)      #Initialize
init_printing(use_unicode=False)        #Set unicode printing to false [explicitly sets Latex]
x = Symbol('x', real=True)      #Sets x as a symbol with real inputs only
sympy_operation = 5*sin(x)        # The sympy function chosen (chose 5*sin(x) as a default for demo)
latex_expr = EquationObject.sympy_to_latex(sympy_operation)         #The latex equivalent of the sympy operation [simplifies the process of generating math equations graphically by ridding the necessity of writing initial expressions with latex]
EquationObject.latexeq_to_image(equation_object, latex_expr)        #Uses the size of equationobject, gives file path for storage, and generates an adequately compressed latex image
surface_image_equation = EquationObject.render_equation_copy(equation_object)       #Records the image generated in the form of a surface for manipulation of its properties
rect_surface_image_equation = surface_image_equation.get_rect()         #Gets the dimensions of the surface_image_equation in the form of a rect for future use
function_storage = []       #Stores the function pertaining to the player at any given instance

text_disc = font_cmu_rm.render("", True, ColorsManual.red)      #Serves to hold the text with the serif roman default font style, red colored, for the purposes of reporting errors in real time
text_disc_pos = text_disc.get_rect(x = (width//2 - 300), y = (height - 200))        #Position of text on screen
image_list, text_image_list, text_image_pos_list = ControlOperations.controls(equation_object)      #Gets the image list of all operations performable by the player

quit = False        #Responsible for recording if events are quit or not quit, closes if true

function_storage = [] #Stores the function pertaining to the player at any given instance
color_default = ColorsManual.green 
error = ""
error_check = None









def refresh_everything_in_game():
   keystate = pygame.key.get_pressed() #get the currently held keys
   
   PlayerMovement.player_movement(keystate, player)
   player_rect = RenderPlayer.render_player(player) #render the player
   EquationObject.move_equation(player, bounds_x, bounds_y, screen, rect_surface_image_equation, surface_image_equation, equation_object)
   ControlOperations.update_controls(image_list, text_image_list, text_image_pos_list, error, error_check)
   enemy_rect = Enemy.draw_record_enemy(enemy, screen, player, player_rect, color_default)
   MiniMap.coordinates(player, player_rect, screen, enemy, enemy_rect)
   Hitbox.hitbox_draw(enemy_rect, player_rect, screen)
   pygame.display.flip() #update the screen
   



while not quit:
   GridBackground.grid_alignment(player, screen)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         quit = True
      if event.type == pygame.KEYDOWN:
         function_storage, error, error_check, color_default, sympy_operation, surface_image_equation = PC_MAIN.player_controls(event, player, sympy_operation, enemy, color_default, equation_object, surface_image_equation) 
      
   refresh_everything_in_game()
   clock.tick(60) #Limit the game to 60 fps, also limit physics logic
    
pygame.quit()
