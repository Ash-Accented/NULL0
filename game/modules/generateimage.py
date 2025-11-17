from game.modules.base_modules import *
from game.modules.preloads import *
class GenerateImage:

   def generate_img_surface(name_of_file, obj, path_desired):
      latex_expr = GenerateImage.sympy_to_latex(obj.expr)
      GenerateImage.latexeq_to_image(obj, latex_expr, name_of_file, path_desired) #Saves equation to image png
      surface_image_equation = GenerateImage.render_equation_copy(obj, path_desired, name_of_file)
      rect_surface_image_equation = surface_image_equation.get_rect()
      return(surface_image_equation, rect_surface_image_equation)
      



   def sympy_to_latex(sympy_operation):
      x = Symbol('x', real=True)      #Sets x as a symbol with real inputs only
      init_printing(use_unicode=False)
      latex_expr = latex(sympy_operation, mode='inline') #INLINE MODE IS CRUCIAL SEE DOCUMENTATION https://docs.sympy.org/latest/modules/printing.html#sympy.printing.latex.latex
       
      return(latex_expr)
   pass

   def latexeq_to_image(equationObject, latex_expr, name_of_file, path_desired):
      preview(latex_expr, viewer="file", filename=path_desired + name_of_file, euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 200", "-bg", "Transparent", "-fg", "rgb 0.0 1.0 0.0"]) #white 1/1/1; black 0/0/0;

      imageResized = Image.open(path_desired + name_of_file)
      size = (equationObject.w, equationObject.h)
      imageResized.thumbnail(size, Image.Resampling.LANCZOS)
      out_dim = imageResized.size
      imageResized.save(path_desired + name_of_file,"PNG")
      imageResized.close
      
   pass

   def render_equation_copy(obj, path_desired, name_of_file):
      surfaceImageEquation = pygame.Surface((obj.w, obj.h))
      surfaceImageEquation.fill((255, 255, 255))
      surfaceImageEquation = pygame.image.load(os.path.join(path_desired + name_of_file)) #Make initial surface containing the player's equation
      return(surfaceImageEquation.convert_alpha())
   pass

   
