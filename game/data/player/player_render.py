from game.modules.base_modules import *

#Unique modules
from game.data.preload.colors import ColorsManual
from game.data.background.background import bounds_x, bounds_y, grid_spacing, GridBackground
from game.data.display.display import screen, window, display_info, display_flags, width, height
from game.data.display.frames import clock, framerate
from game.data.player.player import Player
from game.data.objects.test import Test
player_velocity_base = 100
player_pos_init_x, player_pos_init_y = [0, 0]
player_size = 20
player_border = 5
player_scope_size = 5       #Scope for player to align their function drawings more accurately
player_rect = 0
player_hitbox = 0
player = Player(E)
test = Test(player)
class RenderPlayer:

   def render_player(entity):
      '''
      Render the rect representing the player on the screen
      '''
      #attempting to draw a player that is offscreen will not cause issues, so we don't need to check if they are onscreen, however the boundaries can be set through the attributes dx and dy respective to the player
      corner_of_screen_x, corner_of_screen_y = RenderPlayer.return_corners_xy()
      player_rect = pygame.draw.circle(window, (player.color), (entity.dx - corner_of_screen_x, entity.dy - corner_of_screen_y), player_size, player_border) #draw a solid green circle on the screen with a radius of 20 centered on the entity's location relative to the player
      player_scope_size_rect = pygame.draw.circle(window, (player.color), (entity.dx - corner_of_screen_x, entity.dy - corner_of_screen_y), player_scope_size, 0)
      player_rect.x = player_rect.x + (player_rect.width//2)        #Align the coordinates of the rect to the coordinates of the player dx/dy attributes
      player_rect.y = player_rect.y + (player_rect.height//2)       #same
      return(player_rect)
   pass

   def return_corners_xy():
      '''
      Return the corners of the screen relative to the player position
      '''
      corner_of_screen_x = player.dx - screen.get_size()[0]/2 #the coordinate value on the map of the point at the corner of the screen
      corner_of_screen_y = player.dy - screen.get_size()[1]/2 #same
      #clamp the viewable area of the screen to the boundaries of the map by restricting the corner of the screen to within 0 - one screen width from the edge
      corner_of_screen_x = Clamp.clamp(corner_of_screen_x, 0, bounds_x - screen.get_size()[0])
      corner_of_screen_y = Clamp.clamp(corner_of_screen_y, 0, bounds_y - screen.get_size()[1])
      return(corner_of_screen_x, corner_of_screen_y)
   pass
      

