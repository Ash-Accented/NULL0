from game.modules.base_modules import *
from game.modules.preloads import *
class Enemy:
   def __init__(self, dx, dy, vx, vy, radius):
      self.dx = dx
      self.dy = dy
      self.vx = vx
      self.vy = vy
      self.radius = radius
   pass
   def draw_record_enemy(enemy, player_rect, color):  #ENEMY POSITION NOT RELIANT ON PLAYER POSITION
      grid_spacing = 50
      width, height = screen.get_size()
      clamped_area_x, clamped_area_y = (bounds_x - width), (bounds_y - height) #Make scrolled_displacement the amount traversed as the grid scrolls
      static_area_x, static_area_y = width//2, height//2
     
      
      scrolled_displacement_x = (clamped_area_x) #1500 = 1400 + x --> (900)  1800 - 1500
      scrolled_displacement_y = (clamped_area_y) #800 + 450
      #36, 12 if 25 grid [15, 10]
      new_pos_x = enemy.dx
      new_pos_y = enemy.dy
      #1080, 1800, 900, | 970, 110, 530, 970, 530
      #960, 540
      if(player_rect.x == static_area_x):
         new_pos_x -= (player.dx - static_area_x)
      elif(player_rect.x > static_area_x):
         new_pos_x = enemy.dx - (scrolled_displacement_x)
      elif(player_rect.x < static_area_x):
         new_pos_x = enemy.dx
      if(player_rect.y == static_area_y):
         new_pos_y -= (player.dy - static_area_y)
      elif(player_rect.y > static_area_y):
         new_pos_y = enemy.dy - (scrolled_displacement_y)
      elif(player_rect.y < static_area_y):
         new_pos_y = enemy.dy
         
      enemy_rect = pygame.draw.circle(screen, color, (new_pos_x, new_pos_y), enemy.radius, width=4)
      enemy_rect.x = enemy_rect.x + (enemy_rect.width//2)
      enemy_rect.y = enemy_rect.y + (enemy_rect.height//2)
      
      return(enemy_rect)
   pass



