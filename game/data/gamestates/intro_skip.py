from game.modules.modules import *
from game.data.preload.fonts import font_cmu_rm, font_cmu_bld
from game.modules.reset_surface import ResetSurface

class IntroSkip:
   def intro_skip_method(screen):
      width, height = screen.get_size()
      background_intro = pygame.Surface((width, height))
      background_intro.fill((0,0,0))
      running = True
      x_axis_placement = width // 2
      y_axis_placement = height // 2
      clock = pygame.time.Clock()
      framerate = 60
      
      if running == True:
         default_pos = (0, 0)
         m = 0
         factor_speed = 0.00555 
         amplifier = 3
     
         text_disc = font_cmu_rm.render("PRESS ESC KEY TO SKIP", True, (255, 255, 255))
         text_disc_pos = text_disc.get_rect(x = (x_axis_placement - 300), y = (2*y_axis_placement - 200))

         text_zero = font_cmu_bld.render("NULL0", True, (255, 255, 255)) #initialize
         text_zero_pos = text_zero.get_rect(x = (x_axis_placement), y = (y_axis_placement - 40))
   
         k = 0
         time_surface = pygame.Surface((width, height))
         while k < 1:
            text_disc = font_cmu_rm.render("PRESS ESC KEY TO SKIP", True, (k*255, k*255, k*255))
            text_disc_pos = text_disc.get_rect(x = (x_axis_placement - 175),y = (height - 100 ))
            j = str(round(3*(1 - k), 4))
         
            text_time_left = font_cmu_rm.render(j, True, (255, 255, 255))
            text_time_left_pos = text_time_left.get_rect(x = (x_axis_placement + x_axis_placement//1.2),y = y_axis_placement//7)
            time_surface.blit(text_disc, text_disc_pos)
            time_surface.blit(text_time_left, text_time_left_pos)
            k += factor_speed
            screen.blit(time_surface, default_pos) 
            pygame.display.flip()
            for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_ESCAPE:
                     pygame.event.clear()
                     return("exit intro")
            clock.tick(framerate)
            ResetSurface.reset_surface_opaque(time_surface, (0, 0, 0))
         ResetSurface.reset_surface_opaque(background_intro, (0, 0, 0))
         return("")
   pass

