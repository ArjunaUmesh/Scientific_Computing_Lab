# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:38:44 2022

@author: 20pt04
"""


import sympy as sp
x,y=sp.symbols('x,y')

def regulaFalse(expr,x0,x1):
    
    iteration=1
    while(True):
        
        fx0=expr.replace(x,x0)
        fx1=expr.replace(x,x1)
        
        x2=(float)(x0*fx1-x1*fx0)/(fx1-fx0)
        print(x2)
        fx2=expr.replace(x,x2)
        
        if(abs(fx2)<0.0001):
            break        
        if(fx1*fx2<0):
            x0=x2
        else:
            x1=x2
        print("Iteration : {} , x2 : {}".format(iteration,x2))
        iteration+=1
 
    print("Root of the equation : {}, f(x) : {}".format(x2,fx2))
     
    
    
    

expr=x**3 - x - 1 
expr1=x**3 - 5*x - 9

regulaFalse(expr,1,2)
