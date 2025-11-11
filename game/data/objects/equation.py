from game.modules.base_modules import *
from game.modules.preloads import *
class EquationObject:
   def __init__(self, length, height):
      self.length = length
      self.height = height
   pass

   def move_equation(player, bounds_x, bounds_y, screen, rect, surfaceImageEquation, equationObject):
      
      corner_of_screen_x = player.dx - screen.get_size()[0]/2
      corner_of_screen_y = player.dy - screen.get_size()[1]/2

      corner_of_screen_x = Clamp.clamp(corner_of_screen_x, 0, bounds_x - screen.get_size()[0])
      corner_of_screen_y = Clamp.clamp(corner_of_screen_y, 0, bounds_y - screen.get_size()[1])
      
      rect.x = (player.dx - corner_of_screen_x) + (equationObject.length*0.3)  #distance away from player x
      rect.y = (player.dy - corner_of_screen_y) - (equationObject.height*0.3) #distance away from player y
      #AFTER HERE, THE DRAWING OF AN EQUATION CAN BE DONE
      screen.blit(surfaceImageEquation, rect)
       
   def render_equation_copy(equationObject):
      surfaceImageEquation = pygame.Surface((equationObject.length, equationObject.height))
      surfaceImageEquation.fill((255, 255, 255))
      surfaceImageEquation = pygame.image.load(os.path.join('game/images/equationtemp/temp.png')) #Make initial surface containing the player's equation
      return(surfaceImageEquation.convert_alpha())
   def latexeq_to_image(equationObject, latex_expr):
      preview(latex_expr, viewer="file", filename='game/images/equationtemp/temp.png', euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 200", "-bg", "Transparent", "-fg", "rgb 0.8 0.7 1.0"]) #white 1/1/1; black 0/0/0;
      

      
      imageResized = Image.open("game/images/equationtemp/temp.png")
      size = (equationObject.length, equationObject.height)
      imageResized.thumbnail(size, Image.Resampling.LANCZOS)
      out_dim = imageResized.size
      imageResized.save('game/images/equationtemp/temp.png',"PNG")
      imageResized.close
      
   pass
   def sympy_to_latex(sympy_operation):
      init_printing(use_unicode=False)
      latex_expr = latex(sympy_operation, mode='inline') #INLINE MODE IS CRUCIAL SEE DOCUMENTATION https://docs.sympy.org/latest/modules/printing.html#sympy.printing.latex.latex
       
      return(latex_expr)
   pass


