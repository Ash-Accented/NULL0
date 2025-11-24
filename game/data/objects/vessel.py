from game.modules.base_modules import *
from game.data.display.display import window
from game.data.preload.colors import ColorsManual
from game.data.objects.hitboxes import Hitbox
class Vessel(pygame.sprite.Sprite):
   def __init__(self, dx, dy, fill):
      pygame.sprite.Sprite.__init__(self)
      self.dx = dx
      self.dy = dy
      self.fill = fill


class VesselCircle(Vessel):
   def __init__(self, dx, dy, fill, r):
      super().__init__(dx, dy, fill)
      self.r = r
      self.w, self.h = self.r*2, self.r*2
      self.rect = pygame.draw.circle(window, ColorsManual.white, (self.dx, self.dy), self.r, self.fill)
      self.drx, self.dry = (self.rect.x + (self.rect.width//2)), (self.rect.y + (self.rect.height//2))
      self.hitbox = Hitbox.hitbox_draw_entity_circle(self)

class VesselRect(Vessel):
   def __init__(self, dx, dy, fill, w, h):
      super().__init__(dx, dy, fill)
      self.w, self.h = w, h
      self.rect = pygame.draw.rect(window, ColorsManual.white, ((self.dx, self.dy), (self.w, self.h)), self.fill)
      self.drx, self.dry = (self.rect.x + (self.rect.width//2)), (self.rect.y + (self.rect.height//2))
      self.hitbox = Hitbox.hitbox_draw_entity(self)


