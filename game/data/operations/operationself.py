from game.modules.base_modules import *
from game.modules.preloads import *
from game.data.objects.equation import EquationObject
class OperationsSelf:

   def operation_equation(eq_obj, n, operation_num):
      x = Symbol('x', real=True)
      match operation_num:
         case 1:
            eq_obj.expr = simplify(eq_obj.expr + n)
         case 2:
            eq_obj.expr = simplify(eq_obj.expr - n)
         case 3:
            eq_obj.expr = simplify(eq_obj.expr*n)
         case 4:
            eq_obj.expr = simplify(eq_obj.expr/n)
         case 5:
            eq_obj.expr = simplify(eq_obj.expr**n)
         case 6:
            eq_obj.expr = simplify(diff(eq_obj.expr))
         case 7:
            eq_obj.expr = integrate(eq_obj.expr)
         case 8:
            eq_obj.expr = simplify(n**eq_obj.expr)
         case 9:
            x = Symbol('x')
            eq_obj.expr = simplify(root(eq_obj.expr, n))
         case 10:
            x = Symbol('x')
            eq_obj.expr = eq_obj.expr.subs(x, n)
      
      latex_expr = EquationObject.sympy_to_latex(eq_obj)
      EquationObject.latexeq_to_image(eq_obj)
      eq_obj.surf = EquationObject.render_equation_copy(eq_obj)
      eq_obj.rend_rect = eq_obj.surf.get_rect()
      return(eq_obj.expr, eq_obj.surf)


   def operation_expr(expr, n, operation_num):
      x = Symbol('x', real=True)
      match operation_num:
         case 1:
            expr = simplify(expr + n)
         case 2:
            expr = simplify(expr - n)
         case 3:
            expr = simplify(expr*n)
         case 4:
            expr = simplify(expr/n)
         case 5:
            expr = simplify(expr**n)
         case 6:
            if n == x:
               expr = simplify(diff(expr))
         case 7:
            if n == x:
               expr = integrate(expr)
         case 8:
            expr = simplify(n**expr)
         case 9:
            x = Symbol('x')
            expr = simplify(root(expr, n))
         case 10:
            x = Symbol('x')
            expr = expr.subs(x, n)

      return(expr)


