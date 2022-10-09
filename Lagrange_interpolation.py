# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:47:57 2022

@author: 20pt04
"""

import sympy as sp
x,y=sp.symbols('x,y')

def lagranges_interpolation(xval,yval):
    
    n=len(xval)
    expr=0
    
    for i in range(n):
        val=1
        for j in range(n):
            if(j!=i):
                val=val*(x-xval[j])
                val=val/(xval[i]-xval[j])
        val=val*yval[i]
        expr+=val
    return expr



xval0=[1,4,6]
yval0=[0,1.386294,1.791760]

f=lagranges_interpolation(xval0, yval0)
print(f)
print("f(9) : ",f.replace(x,9))

xval1=[5,7,11,13,17]
yval1=[150,392,1452,2366,5202]

f=lagranges_interpolation(xval1, yval1)
print(f)
print("f(9) : ",f.replace(x,9))

#a
xval2=[5,6,9,11]
yval2=[12,13,14,16] 

f=lagranges_interpolation(xval2, yval2)
print(f)
print("f(10) : ",f.replace(x,10))

#b
xval3=[0,1,3,4]
yval3=[-12,0,6,12]

f=lagranges_interpolation(xval3, yval3)
print(f)
print("f(2) : ",f.replace(x,2))

#c
xval4=[0,1,4,5]
yval4=[4,3,24,39] 

f=lagranges_interpolation(xval4, yval4)
print(f)
print("f(2.175) : ",f.replace(x,2.175))




