from game.modules.modules import *
from game.data.preload.fonts import font_cmu_rm, font_cmu_bld
from game.data.preload.colors import ColorsManual
class MiniMap:
   def coordinates(player, player_rect, screen, enemy, enemy_rect):
      player_coords = str((round(player.dx), round(player.dy)))
      player_rect_coords = str((player_rect.x, player_rect.y))
      enemy_coords = str((round(enemy.dx), round(enemy.dy)))
      enemy_rect_coords = str((enemy_rect.x, enemy_rect.y))
      width, height = screen.get_size()
      
      text_player = font_cmu_rm.render("PLAYER: " + player_coords, True, ColorsManual.medium_purple)
      text_player_pos = text_player.get_rect(x = (width//2 + 600), y = (height - 200))
      text_player_rect = font_cmu_rm.render("PLAYER[RECT]: " + player_rect_coords, True, ColorsManual.medium_purple)
      text_player_rect_pos = text_player.get_rect(x = (width//2 - 800), y = (height - 200))
      
      text_enemy = font_cmu_rm.render("ENEMY: " + enemy_coords, True, ColorsManual.green)
      text_enemy_pos = text_enemy.get_rect(x = (width//2 + 600), y = (height - 100))
      
      text_enemy_rect = font_cmu_rm.render("ENEMY[RECT]: " + enemy_rect_coords, True, ColorsManual.green)
      text_enemy_rect_pos = text_enemy.get_rect(x = (width//2 - 800), y = (height - 100))
      screen.blit(text_player, text_player_pos)
      screen.blit(text_player_rect, text_player_rect_pos)
      screen.blit(text_enemy, text_enemy_pos)
      screen.blit(text_enemy_rect, text_enemy_rect_pos)
