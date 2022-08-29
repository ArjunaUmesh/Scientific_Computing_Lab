# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:19:59 2022

@author: 20pt04
"""

matrix=[[3, 20, -1, -18],
        [2, -3, 20, 25],
        [20, 1, -2, 17]]
matrix2=[[2,1,11],
         [5,7,13]]

def GAUSS_JACOBI(matrix):
    n=len(matrix)
    
    for i in range(n):
        s=sum(matrix[i])-matrix[i][n]-matrix[i][i]
        if(matrix[i][i]<=s):
            for j in range(n):
                if(i!=j and matrix[i][j]>matrix[i][i]):
                    t=matrix[i][i]
                    matrix[i][i]=matrix[i][j]
                    matrix[i][j]=t
    x=[1 for i in range(n)]

    for k in range(25):    
        for i in range(n):
            t=matrix[i][n]
            for j in range(n):
                if(i!=j):
                    t=t-matrix[i][j]*x[j]
            x[i]=t/matrix[i][i]
        print(x)
        
    print(x)
        

GAUSS_JACOBI(matrix2)
        
    
