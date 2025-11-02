from game.modules.modules import *
from game.data.player.player_render import player, RenderPlayer
from game.data.operations.drawfunction import DrawFunction
player_max_speed = 100
general_velocity = 2
accelerationf = 0.7
deccelerationf = 0.2 
class PlayerMovement:
   def player_movement(keystate, player, sympy_expression, screen):
      if keystate[pygame.K_w]: #if the key is pressed, accelerate the player in that direction
         player.vy -= accelerationf
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
      if keystate[pygame.K_SPACE]:
         DrawFunction.draw_function(sympy_expression, player, screen)
   pass


