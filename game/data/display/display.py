from game.modules.base_modules import *
display_info = pygame.display.Info()
display_flags = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SCALED 
screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), display_flags) #create a monitor surface the size of the display, using the display flags
width, height = screen.get_size()


