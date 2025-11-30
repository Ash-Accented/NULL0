import pygame #Import pygame beforehand, to allow other modules to initialize
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("NULL0")
from game.modules.modules import * #Takes from dedicated modules file for main.py



#Start @ skippable section of intro before playing intro animation, only skips if ESC key is pressed
if (IntroSkip.intro_skip_method(screen) != "exit intro"):
   IntroAnimation.intro_animation_method()
from game.data.gamestates.mainmenu import MainMenu
#MainMenu.button_mmenu()
#MainMenu.update_menu()


from game.data.gamestates.game_running import GameRunning

GameRunning.game_ongoing()
pygame.quit()

