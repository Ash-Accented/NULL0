import pygame
from game.modules.modules import *
from game.data.player.player_controls import PlayerControls as PC_TUTORIAL
from game.data.gamestates.game_running import GameRunning as GAME_ONGOING
class Tutorial:
   sympy_operation = exp(1)
   text_prompt = font_cmu_rm.render("", True, ColorsManual.red)      #Serves to hold the text with the serif roman default font style, red colored, for the purposes of reporting errors in real time
   text_prompt_pos = text_disc.get_rect(x = (width//2 - 300), y = (height - 200))        #Position of text on screen
   
   #image_list, text_image_list, text_image_pos_list = ControlOperations.controls(equation_object)      #Gets the image list of all operations performable by the player
