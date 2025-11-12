from game.modules.base_modules import *
from game.modules.preloads import *
from game.data.objects.equation import EquationObject
class OperationsSelf:
   def operation_addition(equation_object, sympy_expression, n):
      x = Symbol('x', real=True)
      sympy_expression_new = simplify(sympy_expression + n)
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equation_object, latex_expr)
      surface_image_equation = EquationObject.render_equation_copy(equation_object)
      rect = surface_image_equation.get_rect()
      return(sympy_expression_new, surface_image_equation)
      
      pygame.display.flip() 
   pass

   def operation_subtraction(equation_object, sympy_expression, n):
      x = Symbol('x', real=True)
      sympy_expression_new = simplify(sympy_expression - n)
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equation_object, latex_expr)
      surface_image_equation = EquationObject.render_equation_copy(equation_object)
      rect = surface_image_equation.get_rect()
      return(sympy_expression_new, surface_image_equation)
      
      pygame.display.flip() 
   pass

   def operation_multiplication(equation_object, sympy_expression, n):
      x = Symbol('x', real=True)
      sympy_expression_new = simplify(sympy_expression*n)
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equation_object, latex_expr)
      surface_image_equation = EquationObject.render_equation_copy(equation_object)
      rect = surface_image_equation.get_rect()
      return(sympy_expression_new, surface_image_equation)
      
      pygame.display.flip() 
   pass

   def operation_division(equation_object, sympy_expression, n):
      x = Symbol('x', real=True)
      sympy_expression_new = simplify(sympy_expression/n)
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equation_object, latex_expr)
      surface_image_equation = EquationObject.render_equation_copy(equation_object)
      rect = surface_image_equation.get_rect()
      return(sympy_expression_new, surface_image_equation)
      pygame.display.flip() 
   pass

   def operation_to_power(equation_object, sympy_expression, n):
      x = Symbol('x', real=True)
      sympy_expression_new = simplify(sympy_expression**n)
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equation_object, latex_expr)
      surface_image_equation = EquationObject.render_equation_copy(equation_object)
      rect = surface_image_equation.get_rect()
      return(sympy_expression_new, surface_image_equation)
      pygame.display.flip() 
   pass

   def operation_derivative(equation_object, sympy_expression):
      x = Symbol('x', real=True)
      sympy_expression_new = simplify(diff(sympy_expression))
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equation_object, latex_expr)
      surface_image_equation = EquationObject.render_equation_copy(equation_object)
      rect = surface_image_equation.get_rect()
      return(sympy_expression_new, surface_image_equation) 
      pygame.display.flip() 
   pass

   def operation_integration(equation_object, sympy_expression):
      x = Symbol('x', real=True)
      sympy_expression_new = simplify(integrate(sympy_expression, (x)))
      
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equation_object, latex_expr)
      surface_image_equation = EquationObject.render_equation_copy(equation_object)
      rect = surface_image_equation.get_rect()
      return(sympy_expression_new, surface_image_equation)
        
      
      pygame.display.flip() 
   pass

   def operation_exponentiated(equation_object, sympy_expression, n):
      x = Symbol('x', real=True)
      sympy_expression_new = simplify(n**sympy_expression)
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equation_object, latex_expr)
      surface_image_equation = EquationObject.render_equation_copy(equation_object)
      rect = surface_image_equation.get_rect()
      return(sympy_expression_new, surface_image_equation)
      
      pygame.display.flip() 
   pass

   def operation_root(equation_object, sympy_expression, n):
      x = Symbol('x', real=True)
      sympy_expression_new = simplify(root(sympy_expression, n))
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equation_object, latex_expr)
      surface_image_equation = EquationObject.render_equation_copy(equation_object)
      rect = surface_image_equation.get_rect()
      return(sympy_expression_new, surface_image_equation)
      
      pygame.display.flip() 
   pass
   
   def operation_evaluate(equation_object, sympy_expression, n):
      x = Symbol('x', real=True)
      expression_new = simplify(sympy_expression.subs(x, n))
      latex_expr = EquationObject.sympy_to_latex(expression_new)
      EquationObject.latexeq_to_image(equation_object, latex_expr)
      surface_image_equation = EquationObject.render_equation_copy(equation_object)
      rect = surface_image_equation.get_rect()
      return(expression_new, surface_image_equation)
      
      pygame.display.flip() 
   pass

