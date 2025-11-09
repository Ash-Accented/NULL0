from game.modules.modules import *
from game.modules.clamp import Clamp
from game.data.background.background import bounds_x, bounds_y, grid_spacing, GridBackground

player = PlayerBrief()
player.from_data(0, 0, 100, 100)

player_size = 40


class RenderPlayer:
   def render_player(entity, screen):
      #attempting to draw a player that is offscreen will not cause issues, so we don't need to check if they are onscreen
      corner_of_screen_x = player.dx - screen.get_size()[0]/2 #the coordinate value on the map of the point at the corner of the screen
      corner_of_screen_y = player.dy - screen.get_size()[1]/2 #same
      #clamp the viewable area of the screen to the boundaries of the map by restricting the corner of the screen to within 0 - one screen width from the edge
      corner_of_screen_x = Clamp.clamp(corner_of_screen_x, 0, bounds_x - screen.get_size()[0])
      corner_of_screen_y = Clamp.clamp(corner_of_screen_y, 0, bounds_y - screen.get_size()[1])
      player_rect = pygame.draw.circle(screen, (224, 159, 255), (entity.dx - corner_of_screen_x, entity.dy - corner_of_screen_y), player_size, 1) #draw a solid green circle on the screen with a radius of 20 centered on the entity's location relative to the player
      player_rect.x = player_rect.x + (player_rect.width//2)
      player_rect.y = player_rect.y + (player_rect.height//2)
      return(player_rect)
   pass


      

