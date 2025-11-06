from game.modules.modules import *
from game.data.objects.equation import EquationObject
class OperationsSelf:
   def operation_addition(equationObject, sympy_expression, n):
      sympy_expression_new = simplify(sympy_expression + n)
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equationObject, latex_expr)
      surfaceImageEquation = EquationObject.render_equation_copy(equationObject)
      rect = surfaceImageEquation.get_rect()
      return(sympy_expression_new, surfaceImageEquation)
      
      pygame.display.flip() 
   pass

   def operation_subtraction(equationObject, sympy_expression, n):
      sympy_expression_new = simplify(sympy_expression - n)
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equationObject, latex_expr)
      surfaceImageEquation = EquationObject.render_equation_copy(equationObject)
      rect = surfaceImageEquation.get_rect()
      return(sympy_expression_new, surfaceImageEquation)
      
      pygame.display.flip() 
   pass

   def operation_multiplication(equationObject, sympy_expression, n):
      sympy_expression_new = simplify(sympy_expression*n)
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equationObject, latex_expr)
      surfaceImageEquation = EquationObject.render_equation_copy(equationObject)
      rect = surfaceImageEquation.get_rect()
      return(sympy_expression_new, surfaceImageEquation)
      
      pygame.display.flip() 
   pass

   def operation_division(equationObject, sympy_expression, n):
      sympy_expression_new = simplify(sympy_expression/n)
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equationObject, latex_expr)
      surfaceImageEquation = EquationObject.render_equation_copy(equationObject)
      rect = surfaceImageEquation.get_rect()
      return(sympy_expression_new, surfaceImageEquation)
      
      pygame.display.flip() 
   pass

   def operation_to_power(equationObject, sympy_expression, n):
      sympy_expression_new = simplify(sympy_expression**n)
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equationObject, latex_expr)
      surfaceImageEquation = EquationObject.render_equation_copy(equationObject)
      rect = surfaceImageEquation.get_rect()
      return(sympy_expression_new, surfaceImageEquation)
   
   pygame.display.flip() 
   pass

   def operation_derivative(equationObject, sympy_expression):
      sympy_expression_new = simplify(diff(sympy_expression, x))
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equationObject, latex_expr)
      surfaceImageEquation = EquationObject.render_equation_copy(equationObject)
      rect = surfaceImageEquation.get_rect()
      return(sympy_expression_new, surfaceImageEquation)
      
      pygame.display.flip() 
   pass

   def operation_integration(equationObject, sympy_expression):
      sympy_expression_new = simplify(integrate(sympy_expression, (x)))
      
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equationObject, latex_expr)
      surfaceImageEquation = EquationObject.render_equation_copy(equationObject)
      rect = surfaceImageEquation.get_rect()
      return(sympy_expression_new, surfaceImageEquation)
        
      
      pygame.display.flip() 
   pass

   def operation_exponentiated(equationObject, sympy_expression, n):
      sympy_expression_new = simplify(n**sympy_expression)
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equationObject, latex_expr)
      surfaceImageEquation = EquationObject.render_equation_copy(equationObject)
      rect = surfaceImageEquation.get_rect()
      return(sympy_expression_new, surfaceImageEquation)
      
      pygame.display.flip() 
   pass

   def operation_root(equationObject, sympy_expression, n):
      sympy_expression_new = simplify(root(sympy_expression, n))
      latex_expr = EquationObject.sympy_to_latex(sympy_expression_new)
      EquationObject.latexeq_to_image(equationObject, latex_expr)
      surfaceImageEquation = EquationObject.render_equation_copy(equationObject)
      rect = surfaceImageEquation.get_rect()
      return(sympy_expression_new, surfaceImageEquation)
      
      pygame.display.flip() 
   pass
   
   def operation_evaluate(equationObject, sympy_expression, n):
      expression_new = simplify(sympy_expression.subs(x, n))
      latex_expr = EquationObject.sympy_to_latex(expression_new)
      EquationObject.latexeq_to_image(equationObject, latex_expr)
      surfaceImageEquation = EquationObject.render_equation_copy(equationObject)
      rect = surfaceImageEquation.get_rect()
      return(expression_new, surfaceImageEquation)
      
      pygame.display.flip() 
   pass

