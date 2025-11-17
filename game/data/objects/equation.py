from game.modules.base_modules import *
from game.modules.preloads import *
class EquationObject(pygame.sprite.Sprite):
   def __init__(self, w, h):
      pygame.sprite.Sprite.__init__(self)
      self.w = w
      self.h = h
      self.expr = E
      self.character = self.expr
      self.latex, self.surf, self.rend_rect = EquationObject.generate_new_equation(self)
   pass

   def generate_new_equation(eq_obj):
      init_printing(use_unicode=False)        #Set unicode printing to false [explicitly sets Latex]
      x = Symbol('x', real=True)      #Sets x as a symbol with real inputs only      # The sympy function chosen for rendering 
      eq_obj.latex = EquationObject.sympy_to_latex(eq_obj)
      latex_expr = eq_obj.latex#The latex equivalent of the sympy operation [simplifies the process of generating math equations graphically by ridding the necessity of writing initial expressions with latex]
      EquationObject.latexeq_to_image(eq_obj)        #Uses the size of equationobject, gives file path for storage, and generates an adequately compressed latex image
      surface_image_equation = EquationObject.render_equation_copy(eq_obj)       #Records the image generated in the form of a surface for manipulation of its properties
      rect_surface_image_equation = surface_image_equation.get_rect()
      return(latex_expr, surface_image_equation, rect_surface_image_equation)

   def move_equation(eq_obj):
      corner_of_screen_x, corner_of_screen_y = RenderPlayer.return_corners_xy()
      rect = eq_obj.surf.get_rect()
      rect.x = (player.dx - corner_of_screen_x) + (eq_obj.w*0.3)  #distance away from player x
      rect.y = (player.dy - corner_of_screen_y) - (eq_obj.h*0.3) #distance away from player y
      #AFTER HERE, THE DRAWING OF AN EQUATION CAN BE DONE
      screen.blit(eq_obj.surf, rect)
       
   def render_equation_copy(eq_obj):
      eq_obj.surf = pygame.Surface((eq_obj.w, eq_obj.h))
      eq_obj.surf.fill((255, 255, 255))
      eq_obj.surf = pygame.image.load(os.path.join('game/images/equationtemp/temp.png')) #Make initial surface containing the player's equation
      return(eq_obj.surf.convert_alpha())
   
   def latexeq_to_image(eq_obj):
      preview(eq_obj.latex, viewer="file", filename='game/images/equationtemp/temp.png', euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 200", "-bg", "Transparent", "-fg", player.color_eq]) #white 1/1/1; black 0/0/0;
      imageResized = Image.open("game/images/equationtemp/temp.png")
      size = (eq_obj.w, eq_obj.h)
      imageResized.thumbnail(size, Image.Resampling.LANCZOS)
      out_dim = imageResized.size
      imageResized.save('game/images/equationtemp/temp.png',"PNG")
      imageResized.close
   pass
   def sympy_to_latex(eq_obj):
      init_printing(use_unicode=False)
      eq_obj_latex = latex(eq_obj.expr, mode='inline') #INLINE MODE IS CRUCIAL SEE DOCUMENTATION https://docs.sympy.org/latest/modules/printing.html#sympy.printing.latex.latex
      return(eq_obj_latex)
   pass


