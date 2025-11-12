import pygame #Import pygame beforehand, to allow other modules to initialize
from game.modules.modules import * #Takes from dedicated modules file for main.py
class GenerateFuncImage:
   def generate_new_equation(equation_object, sympy_operation_rec):
      init_printing(use_unicode=False)        #Set unicode printing to false [explicitly sets Latex]
      x = Symbol('x', real=True)      #Sets x as a symbol with real inputs only
      sympy_operation = sympy_operation_rec      # The sympy function chosen for rendering 
      latex_expr = EquationObject.sympy_to_latex(sympy_operation)         #The latex equivalent of the sympy operation [simplifies the process of generating math equations graphically by ridding the necessity of writing initial expressions with latex]
      EquationObject.latexeq_to_image(equation_object, latex_expr)        #Uses the size of equationobject, gives file path for storage, and generates an adequately compressed latex image
      surface_image_equation = EquationObject.render_equation_copy(equation_object)       #Records the image generated in the form of a surface for manipulation of its properties
      rect_surface_image_equation = surface_image_equation.get_rect() 
      return(latex_expr, surface_image_equation, rect_surface_image_equation)
