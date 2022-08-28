# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 18:24:34 2022

@author: Arjun
"""

import sympy as sp
x,y=sp.symbols('x,y')
def fixedPointIteration(expr,a,b):
    
    #g=expr/x
    #g=-expr.coeff(x,0)/((expr-expr.coeff(x,0))/x)
    g=-(expr-expr.coeff(x,1)*x)/expr.coeff(x)
    #g=eval(g)
    print(g)
    
    gd=g.diff()
    print(gd)
    print(gd.replace(x,a))
    
    '''
    if((gd.replace(x,a))>=1 or (gd.replace(x,b))>=1):
        print('Cant use fixed point iteration method')
        return
    '''
    
    c=float(a)
    c1=c
    #print(c)
    t=1
    while(True):
        c1=c
        c=float(g.replace(x,c))
        print(c1)
        if(abs(c-c1)<0.1):
            break
        t+=1
    
    print("Solution : {} , f(x) : {}".format(c,expr.replace(x,c)))
             
     
    
expr='x**3 - x - 1'
expr1='x**3+2*x**2+10*x-20'
expr=eval(expr) 
fixedPointIteration(expr,1,2)