from game.modules.base_modules import *
display_info = pygame.display.Info()
display_flags = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SCALED
display_flags_window = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SCALED
screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), display_flags) #create a monitor surface the size of the display, using the display flags
window = pygame.display.set_mode((1600, 900), display_flags_window) #create a surface that can be resized and blitted upon, then blitted upon monitor surface
width, height = screen.get_size()


