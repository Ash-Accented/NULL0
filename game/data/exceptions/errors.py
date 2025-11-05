from game.modules.modules import *

class CheckFunctions:
   global error_message_true
   error_message_true = "INV"
   def integrate_und(sympy_expression, a, b):
      new = integrate(sympy_expression, (x, a, b))
      if math.isnan(new) == True or math.isinf(new) == True:
         return(error_message_true)
      else:
         return("")
   pass
         
   def derive_und(sympy_expression):
      new = diff(sympy_expression, x)
      if isinstance(new, float) == True or isinstance(new, int) == True:
         if math.isnan(new) == True or math.isinf(new) == True:
            return(error_message_true)
      else:
         return("")
   pass

   def power_und(sympy_expression, a):
      new = (sympy_expression**a)
      if math.isnan(a) == True or math.isinf(a) == True:
         return(error_message_true)
      else:
         return("")
   pass

   def expon_und(sympy_expression, a):
      new = a**sympy_expression
      if math.isnan(a) == True or math.isinf(a) == True:
         return(error_message_true)
      else:
         return("")
   pass

   def root_und(sympy_expression, a):
      new = root(sympy_expression, a)
      if math.isnan(a) == True or math.isinf(a) == True or isinstance(new, complex) == True:
         return(error_message_true)
      else:
         return("")
   pass

   def eval_und(sympy_expression, a):
      new = sympy_expression.subs(x, a)
      if math.isnan(new) == True or math.isinf(new) == True or isinstance(new, complex) == True:
         return(error_message_true)
      else:
         return("")
   pass

   def division_und(sympy_expression, a):
      new = (sympy_expression/a)
      if math.isnan(a) == True or math.isinf(a) == True or a == 0:
         return(error_message_true)
      else:
         return("")
   pass

   def multiplication_und(sympy_expression, a):
      new = sympy_expression*a
      if math.isnan(a) == True or math.isinf(a) == True:
         return(error_message_true)
      else:
         return("")
   pass

   def subtraction_und(sympy_expression, a):
      new = sympy_expression - a
      if math.isnan(a) == True or math.isinf(a) == True:
         return(error_message_true)
      else:
         return("")
   pass

   def addition_und(sympy_expression, a):
      new = sympy_expression + a
      if math.isnan(a) == True or math.isinf(a) == True:
         return(error_message_true)
      else:
         return("")
   pass

   

