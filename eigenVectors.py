# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 13:38:26 2022

@author: Arjun
"""

import numpy as np
import sympy as sp

#from sklearn.preprocessing import normalize

matrix=sp.Matrix([[4,0,1],[-2,1,0],[-2,0,1]])
matrix2=sp.Matrix([[4,-3,-3],[3,-2,-3],[-1,1,2]])
matrix3=sp.Matrix([[5,-3],[6,-4]])

a,x,y,z=sp.symbols('a,x,y,z')

def eigen(matrix):
    expr=sp.Matrix(matrix-a*np.identity(matrix.shape[0],dtype='int'))
    expr=sp.det(expr)
    eigenValues=sp.solve(expr)
    return(eigenValues)  



def eigenVectors(matrix):
    
    #print(matrix.shape[0])
    #expr=sp.Matrix(matrix-a*np.identity(matrix.shape[0],dtype='int'))
    #expr=sp.det(expr)
    #eigenValues=sp.solve(expr)
    #print(eigenValues)
    #print(eigenValues)
    eigenValues=eigen(matrix)
    
    eigenVectors=[]
    for e in eigenValues:
        matrix2=matrix-e*np.identity(matrix.shape[0],dtype='int')
        matrix2=sp.Matrix(matrix2)
        #print(matrix2)
        matrix2=matrix2.rref()[0]
        sol, params = matrix2.gauss_jordan_solve(sp.Matrix(np.zeros([matrix.shape[0],1],dtype='int')))
        #print(sol)
        tau_val={i:1 for i in params}
        sol=sol.xreplace(tau_val)
        #print(sol)
        eigenVectors.append(list(sol))
    
    return eigenVectors
    '''
    for i in range(len(eigenValues)):
        print("Eigen Value:\n", eigenValues[i], "\n", "Eigen Vector:\n",
        eigenVectors[i], "\n", sep = "")
    '''  
        
        
print(eigenVectors(matrix))