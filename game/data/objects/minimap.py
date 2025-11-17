from game.modules.base_modules import *
from game.modules.preloads import *
class MiniMap:
   def coordinates():
      player_coords = str((round(player.dx), round(player.dy)))
      #player_rect_coords = str((player_rect.x, player_rect.y))
      
      text_player = font_cmu_rm.render(player_coords, True, ColorsManual.medium_purple)
      text_player_pos = text_player.get_rect(x = (width - width//9), y = (height - 100))
      window.blit(text_player, text_player_pos)
      
