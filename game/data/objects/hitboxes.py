from game.modules.base_modules import *
from game.modules.preloads import *
class Hitbox:
   def hitbox_draw(entity_rect, player_rect):
      width, height = screen.get_size()
      player_rect.x = player_rect.x - (player_rect.width // 2)
      player_rect.y = player_rect.y - (player_rect.height // 2)
      player_rect_hitbox = pygame.draw.rect(screen, ColorsManual.blue, ((player_rect.x, player_rect.y), (player_rect.width, player_rect.height)), 1)
      
      entity_rect.x = entity_rect.x - (entity_rect.width // 2)
      entity_rect.y = entity_rect.y - (entity_rect.height // 2)
      entity_rect_hitbox = pygame.draw.rect(screen, ColorsManual.blue, ((entity_rect.x, entity_rect.y), (entity_rect.width, entity_rect.height)), 1)
      return(player_rect_hitbox, entity_rect_hitbox)

