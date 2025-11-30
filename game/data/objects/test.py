import pygame
from game.modules.modules import *
from game.data.objects.vessel import VesselCircle

class Test(VesselCircle):
      def __init__(self, init_pl):
         dx, dy = (pygame.mouse.get_pos()[0] - init_pl.drx), (pygame.mouse.get_pos()[1] - init_pl.dry)
         super().__init__(dx, dy, 0, 5)
         self.rect = pygame.draw.line(window, (255, 255, 255), (init_pl.dx, init_pl.dy), (self.dx, self.dy))
      
   
   
