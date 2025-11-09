from game.modules.modules import *
from game.modules.clamp import Clamp
from game.data.background.background import bounds_x, bounds_y, grid_spacing, GridBackground
from game.data.preload.colors import ColorsManual
class Enemy:
   def __init__(self, dx, dy, vx, vy, radius):
      self.dx = dx
      self.dy = dy
      self.vx = vx
      self.vy = vy
      self.radius = radius
   pass
   def draw_record_enemy(enemy, screen, background, player, player_rect, color):  #ENEMY POSITION NOT RELIANT ON PLAYER POSITION
     
      width, height = screen.get_size()
      
      corner_screen_x = bounds_x - width
      corner_screen_y = bounds_y - height 
      
      new_pos_x = enemy.dx
      new_pos_y = enemy.dy
      clamped_y = math.ceil(height/grid_spacing)*(grid_spacing//2) - 10 #Find value at which scrolling of the screen occurs for rect of player horizontally
      clamped_x_left = (width//grid_spacing)*(grid_spacing//2) + 10 #Find value at which scrolling of screen occurs for rect of player vertically
      clamped_x_right = bounds_x - (clamped_x_left + width)
      adjustment_x = clamped_x_left
      adjustment_y = clamped_y
      clamped_y_down = bounds_y - (clamped_y + height)
      print(player_rect.width//2, corner_screen_x, new_pos_x, new_pos_y, clamped_x_left, clamped_x_right, clamped_y,  adjustment_x, adjustment_y )
      #1080, 1800, 900, | 970, 110, 530, 970, 530
      #960, 540
      if(player_rect.x == clamped_x_left):
         new_pos_x -= (player.dx - adjustment_x)
      elif(player_rect.x > clamped_x_left):
         new_pos_x = enemy.dx - (adjustment_x + clamped_x_right)
      elif(player_rect.x < clamped_x_left):
         new_pos_x = enemy.dx
      if(player_rect.y == clamped_y):
         new_pos_y -= (player.dy - adjustment_y)
      elif(player_rect.y > clamped_y):
         new_pos_y = enemy.dy - (adjustment_y + clamped_y_down)
      elif(player_rect.y < clamped_y):
         new_pos_y = enemy.dy
         
      enemy_rect = pygame.draw.circle(screen, color, (new_pos_x, new_pos_y), enemy.radius, width=4)
      enemy_rect.x = enemy_rect.x + (enemy_rect.width//2)
      enemy_rect.y = enemy_rect.y + (enemy_rect.height//2)
      
      return(enemy_rect)
   pass



