from game.modules.base_modules import *
from game.modules.preloads import *
from game.data.gamestates.intro_skip import IntroSkip
class IntroAnimation:
   def intro_animation_method():
         running = True
         background_intro = pygame.Surface((width, height))
         background_intro.fill((0,0,0)) 
         x_axis_placement = width // 2
         y_axis_placement = height // 2
         text_zero = font_cmu_bld.render("NULL0", True, (255, 255, 255)) #initialize
         text_zero_pos = text_zero.get_rect(x = (x_axis_placement - 100), y = (y_axis_placement - 40))
         if running == True:
      
            logo = 200
            distnegx = x_axis_placement - logo
            distposx = x_axis_placement + logo
            distnegy = y_axis_placement - logo
            distposy = y_axis_placement + logo 
            default_pos = (0, 0)
            #m is the increment of lines drawn, factor_speed controls how long it takes for one line to draw
            m = 0
            factor_speed = 0.00555 #3 seconds for the k<1 events
            amplifier = 3
            k = 0
         
            SoundEffects.sound_effect_null_robot.play()
            while k < 1:
         
               text_zero = font_cmu_bld.render("NULL0", True, (k*255, k*255, k*255))
               background_intro.blit(text_zero, text_zero_pos)
         
               pygame.draw.line( background_intro, (ColorsManual.medium_purple), (distposx, y_axis_placement), (distposx - k*logo, distnegy + k*logo))
               pygame.draw.line( background_intro, (ColorsManual.medium_purple), (distnegx, y_axis_placement), (distnegx + k*logo, distnegy + k*logo))
               pygame.draw.line( background_intro, (ColorsManual.medium_purple), (distposx, y_axis_placement), (distposx - k*logo, distposy - k*logo))
               pygame.draw.line( background_intro, (ColorsManual.medium_purple), (distnegx, y_axis_placement), (distnegx + k*logo, distposy - k*logo))
               k += factor_speed
               screen.blit(background_intro, default_pos)
               pygame.display.flip()
               clock.tick(framerate)



         for x in range(1, width//x_axis_placement):
            lineposx = x*x_axis_placement
            SoundEffects.sound_effect_powerup.play()
            k = 0
            m += 1
            red_to_white = 255

         while k < 1:
            pygame.draw.line( background_intro, (red_to_white, 0, 0), (lineposx, 0), (lineposx, k*height)) 
            k += factor_speed*amplifier
            screen.blit(background_intro, (0,0))
            pygame.display.flip()
            clock.tick(framerate)
         
         m = 0




         for y in range(1, height//y_axis_placement):
            lineposy = y*y_axis_placement 
            SoundEffects.sound_effect_powerup.play()
            k = 0
            m+=1


         while k < 1:
            pygame.draw.line( background_intro, (red_to_white, 0, 0), (0, lineposy), (k*distnegx, lineposy) )
            k += factor_speed*amplifier
            screen.blit(background_intro, (0,0))
            pygame.display.flip()
            clock.tick(framerate)
        



         k = 0



         while k < 1:
            pygame.draw.line( background_intro, (red_to_white, 0, 0), (distposx, lineposy), (distposx + k*distnegx, lineposy))
            k += factor_speed*amplifier
            screen.blit(background_intro, (0,0))
            pygame.display.flip()
            clock.tick(framerate) 

         SoundEffects.sound_effect_blast.play()
         pygame.event.clear()

   pass

