from game.modules.base_modules import *
from game.modules.preloads import *
from game.data.objects.vessel import VesselRect



class Button(VesselRect):
   fill = 0
   def __init__(self, dx, dy, w, h):
      super().__init__(dx, dy, Button.fill, w, h) 
      self.rect = pygame.draw.rect(screen, ColorsManual.white, ((self.dx, self.dy), (self.w, self.h)), width=0, border_radius=5)
