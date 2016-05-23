from sympy import *
import time

a = Symbol('a')
expr0 = Sum(a**2+a,(a,1,2))                                       
print expr0,"=",expr0.doit()
expr1 = Sum(0,(a,1,2))                                       
print expr1,"=",expr1.doit()
expr2 = expr1 / expr0                                               
expr3 = factor(expr2)                                               
expr4 = expr3-expr2
print expr2,"=",expr2.doit()
print expr3,"=",expr3.doit()
print expr4,"=",expr4.doit()
expr5 = simplify(expr4) # Crashes with TypeError: 'mpf' object is not iterable
print expr5,"=",expr5.doit()
