from game.modules.base_modules import *
from game.modules.preloads import *
from game.data.objects.button import Button

class MainMenu:
   font_cmu_rm = pygame.font.Font('game/resources/fonts/cmunrm.ttf', 30)
   text_surface = pygame.Surface((width, height))
   button_surface = pygame.Surface((width, height))
   button_group = pygame.sprite.Group()
   button_amount = 3
   button_seperation = 500
   menu_running = True
   surface_all = pygame.Surface((width, height))
   def button_mmenu():
      for i in range(0, (MainMenu.button_amount - 1)):
         string_render = ""
         match i:
            case 0:
               string_render = "START"
            case 1:
               string_render =  "HOW TO PLAY"
            case 2:
               string_render = "SOME OTHER THING"
         pos_y = (i*MainMenu.button_seperation) + 100
         pos_x = width//2
         rect_x, rect_y = 500, 300
         button = Button(pos_x, pos_y, rect_x, rect_y)
         MainMenu.button_group.add(button)
         text = MainMenu.font_cmu_rm.render(string_render, True, ColorsManual.white)
         text_pos = text.get_rect(x = (pos_x - 50),y = (pos_y))
         MainMenu.text_surface.blit(text, text_pos)
      screen.blit(MainMenu.text_surface, (0, 0))
   def update_menu():
      MainMenu.surface_all.blit(MainMenu.text_surface, (0, 0))
      while MainMenu.menu_running:
         for button in MainMenu.button_group:
            button.rect = pygame.draw.rect(MainMenu.surface_all, ColorsManual.dark_gray, ((button.dx, button.dy), (button.w, button.h)), width=0, border_radius=5)
         
         screen.blit(MainMenu.surface_all, (0, 0))
         pygame.display.flip()
         clock.tick(framerate)

