from sympy import *

c0 = Integer(0) 
v0 = Symbol('a') 
expr0 = pi 
expr1 = Sum(expr0,(v0,c0,c0)) 
expr2 = expr0 % expr1 

print "TEST COMPLETED SUCCESSFULLY"
