# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def linearInterpolation(p1,p2,x):
    
    xdiff=p2[0]-p1[0]
    ydiff=p2[1]-p1[1]
    if(xdiff==0):
        if(x!=p1[0]):
            print('Not defined as line is parallel to y-axis')
        else:
            print('line : x = {}'.format(p1[0]))
    
    y=p1[1] + (x-p1[0])*ydiff/xdiff
    return y
    
    
    
   
    
p1=[-1,-8]
p2=[2,1]
p3=[3,6]
p4=[7,58]
p5=[5,12]
p6=[9,15]
x1=0
x2=5
x3=6
print(linearInterpolation(p1, p2, x1))
print(linearInterpolation(p3, p4, x2))
print(linearInterpolation(p5, p6, x3))


