# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:55:55 2022

@author: 20pt04
"""

matrix=[[1,2,0,0,0],[0,0,1,0,0],[0,0,0,1,5]]
matrix1=[[1,-7,5,5],[0,1,3,2]]
matrix2=[[1,2,3,4,5],[0,0,0,0,0],[0,0,0,1],[0,0,0,0]]
matrix3=[[1,2,0],[0,0,1],[0,0,0],[0,0,0]]

def checkRREF(matrix):
    rows=len(matrix)
    columns=len(matrix[0])
    if(1 not in matrix[0]):
        return 0
    for i in range(0,rows-1):
        
        if(1 not in matrix[i+1]):
            if(matrix[i+1].count(0)==columns):
                if((i+2)<rows and matrix[i+2].count(0)!=columns):
                    print("C")
                    return 0
                else:
                    continue
            else:
                print("D")
                return 0
                
        index=matrix[i].index(1)
        index2=matrix[i+1].index(1)
        if(index2<=index):
            print("A")
            return 0
        for j in range(0,index2):
            if matrix[i+1][j]!=0:
                print("B")
                return 0;
    for i in range(0,rows):
        if(1 in matrix[i]):
            
            index=matrix[i].index(1)
            for j in range(0,rows-1):
                if(j!=i and matrix[j][index]!=0):
                    return 1;
    return 2;

                
case={0:"NONE",1:"REF",2:"RREF"}

print(case[checkRREF(matrix2)])
    