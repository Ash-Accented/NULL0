
import pygame #Import pygame beforehand, to allow other modules to initialize
from game.modules.modules import * #Takes from dedicated modules file for main.py
from game.data.objects.staticpoint import StaticPoint
from game.data.objects.background_origin import BackgroundOrigin

class InitializeVars:
   enemy_sprites = pygame.sprite.Group()
   rand_expr_sprites = pygame.sprite.Group()
   equation_sprite = pygame.sprite.GroupSingle()
   ctrl_opra_sprite = pygame.sprite.GroupSingle()

   dt_refresh_gen = 0
   dt_refresh_rand_expr = 0
   time_counter = 1
   max_rand_expr_sprites = 3
   background = GridBackground.gen_background()
   background_origin = BackgroundOrigin((bounds_x//2 + grid_spacing), (bounds_y//2 + grid_spacing), 4) 
   
   color_default = ColorsManual.green
   
   equation_object = EquationObject(400, 400)      #Initialize

   text_disc = font_cmu_rm.render("", True, ColorsManual.red)      #Serves to hold the text with the serif roman default font style, red colored, for the purposes of reporting errors in real time
   text_disc_pos = text_disc.get_rect(x = (width//2 - 300), y = (height - 200))        #Position of text on screen
   
   function_storage = [] #Stores the function pertaining to the player at any given instance
   color_default = ColorsManual.green 
   error = ""
   error_check = None
   surface_transparent = pygame.Surface((width, height), pygame.SRCALPHA)
   window = window
   check_collision = False
