from game.modules.base_modules import *
from game.modules.preloads import *
player_max_speed = 100
general_velocity = 3.5 #3.5 was original 
accelerationf = 0.8 #0.8 is standard [favourite]
deccelerationf = 0.2 #0.2 is standard [favourite]

class PlayerMovement:
   def player_movement(keystate):
      '''Move the player general_velocity*player.vx units in given direction [W, A, S, D] and draw an arrow in the direction of movement, speed them up by accelerationf every tick and slow them down by deccelerationf*player.vx every tick for fluid movement'''
      corner_of_screen_x, corner_of_screen_y = RenderPlayer.return_corners_xy()
      x1 = ((player.dx - corner_of_screen_x))
      y1 = ((player.dy - corner_of_screen_y))
      magnitude_arrow = 10
      distance_up = -50
      distance_down = 50
      distance_right = 50
      distance_left = -50
      width = 2*magnitude_arrow
      height = magnitude_arrow
      
      if keystate[pygame.K_w] and player.dy > (grid_spacing + player_size): #if the key is pressed, accelerate the player in that direction
         player.vy -= accelerationf #Increases the velocity attribute of the player by accelerationf amount in upward direction
         pygame.draw.polygon(screen, (0, 255, 0), ((x1, (y1 - magnitude_arrow) + distance_up ), (x1 + magnitude_arrow, y1 + distance_up), (x1 - magnitude_arrow, y1 + distance_up))) #Draw an arrow that dictates the direction of movement
      elif keystate[pygame.K_a] and player.dx > (grid_spacing + player_size):
         player.vx -= accelerationf #same but leftward
         pygame.draw.polygon(screen, (0, 255, 0), ((x1 + distance_left, y1 + magnitude_arrow), (x1 + distance_left, y1 - magnitude_arrow), (x1 + distance_left - magnitude_arrow, y1)))
      elif keystate[pygame.K_s] and player.dy < (bounds_y - (grid_spacing + player_size)):
         player.vy += accelerationf #same but downward
         pygame.draw.polygon(screen, (0, 255, 0), ((x1, (y1 + magnitude_arrow) + distance_down ), (x1 + magnitude_arrow, y1 + distance_down), (x1 - magnitude_arrow, y1 + distance_down)))
      elif keystate[pygame.K_d] and player.dx < (bounds_x - grid_spacing):
         player.vx += accelerationf #same but rightward
         pygame.draw.polygon(screen, (0, 255, 0), ((x1 + distance_right, y1 + magnitude_arrow), (x1 + distance_right, y1 - magnitude_arrow), (x1 + distance_right + magnitude_arrow, y1)))
   
      player.vx -= player.vx*deccelerationf #slowly slow down the player and limit top speed
      player.vy -= player.vy*deccelerationf #same

      player.dx += (player.vx*general_velocity) #move the player by velocity units every tick
      player.dy += (player.vy*general_velocity)
   pass




