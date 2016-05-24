import sympy
from sympy import *
from sympy.core.cache import *


clear_cache()


expr1 = E 
expr0 = expr1 * expr1 
expr1 = expr0.subs(expr1,expr0) 

print "TEST COMPLETED SUCCESSFULLY"
