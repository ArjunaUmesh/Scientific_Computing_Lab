# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:05:03 2022

@author: 20pt04
"""

import sympy as sp
x,y=sp.symbols('x,y')


def inverse_lagrange(xval,yval):
    n=len(xval)
    expr=0
    
    for i in range(n):
        val=1
        for j in range(n):
            if(j!=i):
                val=val*(y-yval[j])
                val=val/(yval[i]-yval[j])
        val=val*xval[i]
        expr+=val
    return expr


xval=[1.2,2.1,2.8,4.1,4.9,6.2]
yval=[4.2,6.8,9.8,13.4,15.5,19.6]
f_inv=inverse_lagrange(xval,yval)
print("finv(12) : ",f_inv.replace(y,12))


xval1=[30,34,38,42]
yval1=[-30,-13,3,18]
f_inv=inverse_lagrange(xval1,yval1)
print("finv(0) : ",(float)(f_inv.replace(y,0)))