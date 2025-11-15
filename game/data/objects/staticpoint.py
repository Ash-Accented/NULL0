import pygame
from game.modules.modules import *


class StaticPoint:
   def __init__(self, dx, dy):
      self.dx = dx
      self.dy = dy

   def draw_static_point(entity, player_rect):  #entity POSITION NOT RELIANT ON PLAYER POSITION
      clamped_area_x, clamped_area_y = (bounds_x - width), (bounds_y - height) #Make scrolled_displacement the amount traversed as the grid scrolls
      static_area_x, static_area_y = width//2, height//2
     
      
      scrolled_displacement_x = (clamped_area_x) #1500 = 1400 + x --> (900)  1800 - 1500
      scrolled_displacement_y = (clamped_area_y) #800 + 450
      #36, 12 if 25 grid [15, 10]
      new_pos_x = entity.dx
      new_pos_y = entity.dy
      #1080, 1800, 900, | 970, 110, 530, 970, 530
      #960, 540
      if(player_rect.x == static_area_x):
         new_pos_x -= (player.dx - static_area_x)
      elif(player_rect.x > static_area_x):
         new_pos_x = entity.dx - (scrolled_displacement_x)
      elif(player_rect.x < static_area_x):
         new_pos_x = entity.dx
      if(player_rect.y == static_area_y):
         new_pos_y -= (player.dy - static_area_y)
      elif(player_rect.y > static_area_y):
         new_pos_y = entity.dy - (scrolled_displacement_y)
      elif(player_rect.y < static_area_y):
         new_pos_y = entity.dy
      
      coordinates_entity_rect = (new_pos_x, new_pos_y)
      return(coordinates_entity_rect)
   
   def fix_drawn_rect(entity_rect):
      entity_rect.x = entity_rect.x + (entity_rect.width//2)
      entity_rect.y = entity_rect.y + (entity_rect.height//2)
      return(entity_rect)
