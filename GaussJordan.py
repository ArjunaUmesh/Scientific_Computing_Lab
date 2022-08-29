# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:01:03 2022

@author: 20pt04
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 09:29:54 2022

@author: 20pt04
"""

import sympy as simp

matrix2=[[1,3,4,7],[2,4,6,8],[3,6,9,12]]
matrix3=[[0,1,-2,-3],
         [1,-3,4,-6]]
matrix4=[[1,1,2,8],
         [-1,-2,3,1],
         [3,-7,4,10]]
def GAUSSJORDAN(matrix):
    
    i=0
    j=0
    t=0
    rows=len(matrix)
    columns=len(matrix[0])


        
    while(True):
        t=i
        if(i>=rows or j>=columns):
            break
         
       
        if(matrix[i][j]==0):
            t=i
            while(t<rows and matrix[t][j]==0):
                t+=1
        #print(t)
        if(t==rows):
            j+=1
            continue
                
       
        temp=matrix[i]
        matrix[i]=matrix[t]
        matrix[t]=temp
        
        
        
        pivot=matrix[i][j]
        matrix[i]=[x/pivot for x in matrix[i]]
        pivot=matrix[i][j]
        #print(pivot)
        
        
        for k in range(0,rows):
            
            if(k==i):
                continue
            
            if(matrix[k][j]!=0):
                
                ratio=matrix[k][j]
                for e in range(0,columns):
                    
                    matrix[k][e]=matrix[k][e]-matrix[i][e]*ratio    
                
        i+=1
        j+=1
        
    return matrix

'''
matrix=GAUSSJORDAN(matrix4)
for i in matrix:
    print(i)


m=simp.Matrix(matrix2).rref()
print(m)
'''






