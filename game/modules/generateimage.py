from game.modules.modules import *

class GenerateImage:
   def generate_img_latex(name_of_file, sympy_operation, equationObject):
      path_desired = "game/images/operations/"
      latex_expr = GenerateImage.sympy_to_latex(sympy_operation)
      GenerateImage.latexeq_to_image(equationObject, latex_expr, name_of_file, path_desired) #Saves equation to image png
      






   def sympy_to_latex(sympy_operation):
      init_printing(use_unicode=False)
      latex_expr = latex(sympy_operation, mode='inline') #INLINE MODE IS CRUCIAL SEE DOCUMENTATION https://docs.sympy.org/latest/modules/printing.html#sympy.printing.latex.latex
       
      return(latex_expr)
   pass

   def latexeq_to_image(equationObject, latex_expr, name_of_file, path_desired):
      preview(latex_expr, viewer="file", filename=path_desired + name_of_file, euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 200", "-bg", "Transparent", "-fg", "rgb 0.8 0.7 1.0"]) #white 1/1/1; black 0/0/0;

      imageResized = Image.open(path_desired + name_of_file)
      size = (equationObject.length, equationObject.height)
      imageResized.thumbnail(size, Image.Resampling.LANCZOS)
      out_dim = imageResized.size
      imageResized.save(path_desired + name_of_file,"PNG")
      imageResized.close
      
   pass

   def render_equation_copy(equationObject):
      surfaceImageEquation = pygame.Surface((equationObject.length, equationObject.height))
      surfaceImageEquation.fill((255, 255, 255))
      surfaceImageEquation = pygame.image.load(os.path.join(path_desired + name_of_file)) #Make initial surface containing the player's equation
      return(surfaceImageEquation.convert_alpha())
   pass

   
