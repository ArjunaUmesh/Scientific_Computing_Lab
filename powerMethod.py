# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 22:00:32 2022

@author: Arjun
"""

import numpy as np
import sympy as sp
import math


matrix=sp.Matrix([[1,3,0],[2,5,1],[-1,2,3]])

def powerMethod(matrix):
    
    size=sp.shape(matrix)[0]
    x=sp.ones(size,1)
    print(x)
    m=0
    while(True):
        x=matrix*x
        m1=m
        m=0
        for i in x:
           m+=i**2 
        m=math.sqrt(m)
        x=x*(1/m)
        if(abs(m-m1)<0.0001):
            break
    print("Dominant eigen vector : ",x)
    print("Dominant eigen value : ",m)
powerMethod(matrix)