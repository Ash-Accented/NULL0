from game.modules.modules import *
from game.data.preload.colors import ColorsManual

class Hitbox:
   def hitbox_draw(entity, player_rect, screen):
      width, height = screen.get_size()
      player_rect.x = player_rect.x - (player_rect.width // 2)
      player_rect.y = player_rect.y - (player_rect.height // 2)
      player_rect_hitbox = pygame.draw.rect(screen, ColorsManual.blue, ((player_rect.x, player_rect.y), (player_rect.width, player_rect.height)), 1)
      
      entity.x = entity.x - (entity.width // 2)
      entity.y = entity.y - (entity.height // 2)
      entity_hitbox = pygame.draw.rect(screen, ColorsManual.blue, ((entity.x, entity.y), (entity.width, entity.height)), 1)
      return(player_rect_hitbox, entity_hitbox)

