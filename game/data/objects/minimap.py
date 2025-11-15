from game.modules.base_modules import *
from game.modules.preloads import *
class MiniMap:
   def coordinates(player_rect, enemy, enemy_rect):
      player_coords = str((round(player.dx), round(player.dy)))
      player_rect_coords = str((player_rect.x, player_rect.y))
      enemy_coords = str((round(enemy.dx), round(enemy.dy)))
      enemy_rect_coords = str((enemy_rect.x, enemy_rect.y))
      width, height = screen.get_size()
      
      text_player = font_cmu_rm.render(player_coords, True, ColorsManual.medium_purple)
      text_player_pos = text_player.get_rect(x = (width - width//9), y = (height - 100))
      window.blit(text_player, text_player_pos)
      
