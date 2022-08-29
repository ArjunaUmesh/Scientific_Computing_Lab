# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 08:41:06 2022

@author: 20pt04
"""

matrix=[[4, 1, 2, 4],
        [3, 5, 1, 7],
        [1, 1, 3, 3]]
matrix2=[[2,1,11],
         [5,7,13]]


def GAUSS_SEIDAL(matrix):
    
    n=len(matrix[0])-1
    e=len(matrix)
    x=[0 for i in range(0,n)]

    for t in range(25):
        for i in range(0,n):
            t=matrix[i][n]
            for j in range(0,n):
                if(j!=i):
                    t=t-matrix[i][j]*x[j]
            x[i]=t/matrix[i][i]
           
        print(x)

GAUSS_SEIDAL(matrix2);