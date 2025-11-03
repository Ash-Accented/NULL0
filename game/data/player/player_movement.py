from game.modules.modules import *
from game.modules.clamp import Clamp
from game.data.player.player_render import player, RenderPlayer
from game.data.operations.drawfunction import DrawFunction
player_max_speed = 100
general_velocity = 5
accelerationf = 0.7
deccelerationf = 0.2 
class PlayerMovement:
   def player_movement(keystate, player, sympy_expression, screen, bounds_x, bounds_y):
      corner_of_screen_x = player.dx - screen.get_size()[0]/2
      corner_of_screen_y = player.dy - screen.get_size()[1]/2

      corner_of_screen_x = Clamp.clamp(corner_of_screen_x, 0, bounds_x - screen.get_size()[0])
      corner_of_screen_y = Clamp.clamp(corner_of_screen_y, 0, bounds_y - screen.get_size()[1])
      x1 = ((player.dx - corner_of_screen_x))
      y1 = ((player.dy - corner_of_screen_y))
      size_arrow = 25
      if keystate[pygame.K_w]: #if the key is pressed, accelerate the player in that direction
         player.vy -= accelerationf
         pygame.draw.polygon(screen, (0, 0, 0), ((x1, y1 - size_arrow), (x1 + size_arrow, y1), (x1 - size_arrow, y1)))
         
      elif keystate[pygame.K_a]:
         player.vx -= accelerationf
      elif keystate[pygame.K_s]:
         player.vy += accelerationf
      elif keystate[pygame.K_d]:
         player.vx += accelerationf
   
      player.vx -= player.vx*deccelerationf #slowly slow down the player and limit top speed
      player.vy -= player.vy*deccelerationf #same

      player.dx += (player.vx*general_velocity) #move the player by velocity units every tick
      player.dy += (player.vy*general_velocity)
   pass




