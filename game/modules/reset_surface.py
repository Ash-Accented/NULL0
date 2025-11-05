from game.modules.modules import *


class ResetSurface:

   def reset_surface_transparent(surface):
      width, height = surface.get_size()
      surface_restart = pygame.Surface((width, height), pygame.SRCALPHA)
      
      return(surface_restart)
   pass
   def reset_surface_opaque(surface, color):
      width, height = surface.get_size()
      surface.fill(color)
   pass
