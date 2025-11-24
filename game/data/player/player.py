from game.modules.base_modules import *
from game.data.preload.colors import ColorsManual
from game.data.objects.vessel import VesselCircle

class Player(VesselCircle):
   dx = 0
   dy = 0        #DEFAULT POSITION FOR PLAYER
   fill = 5
   r = 20 #Radius (or default size)
   
   vx = 100
   vy = 100     #DEFAULT VELOCITY FOR PLAYER
   accf = 0.8
   deccf = 0.2

   def __init__(self, character):
      """
      Package data about a player into a PlayerBrief
      """
      super().__init__(Player.dx, Player.dy, Player.fill, Player.r)
      self.vx = Player.vx
      self.vy = Player.vy
      self.accf = Player.accf
      self.deccf = Player.deccf
      self.character = character
      
      if self.character == E:
         self.color = ColorsManual.sage_e
         self.color_eq = ColorsManual.sage_e_eq
      elif self.character == pi:
         self.color = ColorsManual.blue_pi
         self.color_eq = ColorsManual.blue_pi_eq
      elif self.character == GoldenRatio:
         self.color = ColorsManual.amber_gr
         self.color_eq = ColorsManual.amber_gr_eq
      elif self.character == root(2, 2):
         self.color = ColorsManual.purp_root
         self.color_eq = ColorsManual.purp_root_eq
      else:
         self.color = ColorsManual.white
         self.color_eq = ColorsManual.white_eq
      
