from game.modules.base_modules import *
from game.modules.preloads import *
from game.data.objects.staticpoint import StaticPoint
from game.data.objects.background_origin import BackgroundOrigin
class Enemy:
   def __init__(self, dx, dy, vx, vy, radius):
      pygame.sprite.Sprite.__init__(self)
      self.dx = dx
      self.dy = dy
      self.vx = vx
      self.vy = vy
      self.radius = radius
   pass
   def draw_record_enemy(background_origin, enemy, color):  #ENEMY POSITION NOT RELIANT ON PLAYER POSITION
      enemy_coords = BackgroundOrigin.rect_alignment_orig(enemy, background_origin)
      enemy_rect = pygame.draw.circle(window, color, (enemy_coords), enemy.radius, width=4)
      enemy_rect = StaticPoint.fix_drawn_rect(enemy_rect) 
      return(enemy_rect)
   pass



