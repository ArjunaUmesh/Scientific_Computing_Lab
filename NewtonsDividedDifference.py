# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:50:10 2022

@author: 20pt04
"""

import numpy as np
import sympy as sp
x,y=sp.symbols('x,y')
def newtons_divided_diff(xval, yval):
    
    n = len(xval)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = yval
    
    formatter="{0:.6f}"
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (xval[i+j]-xval[i])
            coef[i][j] = formatter.format(coef[i][j])
    print("Divided difference table : ")       
    for i in coef:
        print(i)
    
    expr=0
    
    
    for i in range(n-1):
        val=1
        for j in range(i+1):
            val=val*(x-xval[j])
        expr+=val*coef[0][i+1]
        
    print("Polynomial f(x) : ",expr)
    print("f(2) : ",formatter.format(expr.replace(x,2)))

points={1:0,4:1.386294,6:1.791759,5:1.609438}
xval=[1,4,6,5]
yval=[0,1.386294,1.791759,1.609438]
newtons_divided_diff(xval,yval)