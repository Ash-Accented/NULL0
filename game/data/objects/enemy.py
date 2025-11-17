from game.modules.base_modules import *
from game.modules.preloads import *
from game.data.objects.staticpoint import StaticPoint
from game.data.objects.background_origin import BackgroundOrigin
from game.data.objects.hitboxes import Hitbox
class Enemy(pygame.sprite.Sprite):
   def __init__(self, dx, dy, radius):
      pygame.sprite.Sprite.__init__(self)
      self.dx = dx
      self.dy = dy
      self.r = radius
      self.drx = self.dx
      self.dry = self.dy
      self.w = self.r*2
      self.h = self.r*2
      self.rend_rect = pygame.draw.circle(window, ColorsManual.red, (self.drx, self.dry), self.r, 10)
      self.rect = self.rend_rect
      self.hitbox = Hitbox.hitbox_draw_entity(self)
   pass
   def draw_record_enemy(background_origin, enemy, color):  #ENEMY POSITION NOT RELIANT ON PLAYER POSITION
      enemy.drx, enemy.dry = BackgroundOrigin.rect_alignment_orig(enemy, background_origin)
      enemy.rendered_rect = pygame.draw.circle(window, color, (enemy.drx, enemy.dry), enemy.r, width=4)
      enemy.rendered_rect = StaticPoint.fix_drawn_rect(enemy.rendered_rect)
      return(enemy.rendered_rect)
   pass



