# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:12:02 2022

@author: 20pt04
"""

import sympy as sp
x,y=sp.symbols('x,y')
def newtonRaphson(expr,low,high):
    
    
    iteration=1
    x0=(low+high)/2

    while(True):
        
        
        fx0=expr.replace(x,x0)
        fdx0=expr.diff()
        fdx0=fdx0.replace(x,x0)
        x1=x0 - fx0/fdx0
        a=expr.replace(x,x1)
        if(abs(a)<0.00001):
            break
        else:
            x0=x1
            print("Iteration : {} , x0 : {}".format(iteration,x0))
            iteration+=1
    print("Root of the equation : {}, f(x) : {}".format(x0,a))
            
            
            

expr=x**3 - x - 1 
expr1=x**3 - 5*x - 9

newtonRaphson(expr1,2,3)
            
        
    