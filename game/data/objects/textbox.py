from game.modules.modules import * #NOT RECCOMENDED MOST TIMES, BUT IN THIS SITUATION ITS JUST TO PREVENT 6 LINES FROM BEING WRITTEN EVERY TIME
from game.modules.clamp import Clamp
from game.data.background.background import bounds_x, bounds_y, grid_spacing, GridBackground
from game.data.display.display import screen, display_info, display_flags
from game.data.player.player_render import player, player_size, RenderPlayer
from game.data.player.player_movement import player_max_speed, PlayerMovement


class TextBox(pygame.sprite.Sprite):
   
   def __init__ (self, length, height):
      self.length = length
      self.height = height

   pass

   def render_text_box(player, screen, textbox): #This integrates tracking of the player sprite which has acceleration values that are tweakable to provide more user friendly interaction
      corner_of_screen_x = player.dx - screen.get_size()[0]/2
      corner_of_screen_y = player.dy - screen.get_size()[1]/2

      corner_of_screen_x = Clamp.clamp(corner_of_screen_x, 0, bounds_x - screen.get_size()[0])
      corner_of_screen_y = Clamp.clamp(corner_of_screen_y, 0, bounds_y - screen.get_size()[1])
      
      dx = (player.dx - corner_of_screen_x) + textbox.length*0.5 #makes the distance away = 0.5 the length
      dy = (player.dy - corner_of_screen_y) - textbox.height
      pygame.draw.rect(screen, (224, 159, 255), (dx, dy, textbox.length, textbox.height), 3)
   pass

  
      

