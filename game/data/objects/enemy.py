from game.modules.base_modules import *
from game.modules.preloads import *
from game.data.objects.staticpoint import StaticPoint
from game.data.objects.background_origin import BackgroundOrigin
from game.data.objects.hitboxes import Hitbox
from game.data.methodsandvars.init_vars import InitializeVars
from game.data.objects.vessel import VesselCircle
import random
class Enemy(VesselCircle):
   def __init__(self):
      super().__init__((random.randrange(100, 1800)), (random.randrange(100, 1800)), 10, 30)
      
   pass
   def draw_record_enemy(enemy, color):  #ENEMY POSITION NOT RELIANT ON PLAYER POSITION
      enemy.drx, enemy.dry = BackgroundOrigin.rect_alignment_orig(enemy, InitializeVars.background_origin)
      enemy.rendered_rect = pygame.draw.circle(window, color, (enemy.drx, enemy.dry), enemy.r, width=4)
      enemy.rendered_rect = StaticPoint.fix_drawn_rect(enemy.rendered_rect)
      return(enemy.rendered_rect)
   pass



