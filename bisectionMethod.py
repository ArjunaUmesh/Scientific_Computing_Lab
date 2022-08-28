# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 08:53:23 2022

@author: 20pt04
"""
import math
import sympy as sp
x,y=sp.symbols('x,y')
def bisectionMethod(expr,low,high):
    
    iteration=1
    
    
    while(True):
        
        mid=(high+low)/2
        
        print('Iteration : {} , mid : {} , f(mid) = {}'.format(iteration,mid,expr.replace(x,mid)))
        
        a=expr.replace(x,low)
        b=expr.replace(x,mid)
        #c=expr.replace(x,high)
        if(a*b>0):
            low=mid
        else:
            high=mid
            
        iteration+=1
        
        
        if(abs(high-low)<0.00001 or b==0):
            break
    print("\nlow : {} , high : {} , mid : {} ".format(low,high,mid))
    print("Root : {} , f(x) : {}".format(mid,b))
    
    
    
expr=x*x*x - x - 2
expr1=x**3+2*x**2+10*x-20
expr2=3*x+sp.cos(x)-x
expr3=sp.exp(-x)-sp.sin(x)
#expr2=eval(expr2)
print(expr3)

bisectionMethod(expr3,0,1)