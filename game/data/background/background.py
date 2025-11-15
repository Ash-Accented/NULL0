from game.modules.base_modules import *
#Unique modules
from game.data.display.display import screen, window, display_flags
from game.data.preload.colors import ColorsManual

bounds_x = 3000
bounds_y = 3000
grid_spacing = 50 #height and width of each grid square
background_origin_rad = 5
class GridBackground:
   width, height = screen.get_size()
   def gen_background():
      global background #make the background global so that it can be accessed everywhere  
      width, height = GridBackground.width + grid_spacing, GridBackground.height + grid_spacing #add grid_spacing px for reasons explained below
      background = pygame.Surface((width, height)) #create a surface to use as a template background. create it grid_spacingpx larger than it needs to be, so we can shift it around slighty to give the appearance of a static grid that the player moves relative to, instead of the grid moving with the player 
      background.fill((10, 10, 10)) #set the background to very dark gray
      #draw horizontal and vertical light gray lines grid_spacing px apart 
      for x in range(0, width//grid_spacing + 1): #we need lines grid_spacing px apart, so divide the window width by grid_spacing and round down to the nearest whole number. we need to add 1 because line 0 is actually on the border and not visible. the code below could be written to put the first line on screen, but it's unecessary, and easier to just add an extra line
         pygame.draw.line(background, (50, 50, 50), (x*grid_spacing, 0), (x*grid_spacing, height + grid_spacing)) #draw the line on background, (0, 0, 0) is the colour code for black, start the line at grid_spacing pixels times the line number, and the top of the surface, end the line at the same horizontal, but bottom of the surface
      for y in range(0, height//grid_spacing + 1): #same as above
         pygame.draw.line(background, (50, 50, 50), (0, y*grid_spacing), (width + grid_spacing, y*grid_spacing)) #same as vertical lines, but swapped
         #draw a borderofblack lines
      background_origin_rect = pygame.draw.circle(background, ColorsManual.white, (bounds_x//2, bounds_y//2), background_origin_rad, width=0)	
      return(background)
   pass

   def grid_alignment(player):
      #TODO: Let the grids align with the map bounds
      background_x_origin = Clamp.clamp(player.dx, screen.get_size()[0]/2, bounds_x - screen.get_size()[0]/2)%grid_spacing
      background_y_origin = Clamp.clamp(player.dy, screen.get_size()[1]/2, bounds_y - screen.get_size()[1]/2)%grid_spacing
      window.blit(background, (0, 0), pygame.Rect(background_x_origin, background_y_origin, screen.get_size()[0], screen.get_size()[1]))
   pass

   

