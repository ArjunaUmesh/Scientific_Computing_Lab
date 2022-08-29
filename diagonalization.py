# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:50:46 2022

@author: 20pt04
"""
import numpy as np
import sympy as sp


a,x,y,z=sp.symbols('a,x,y,z')
matrix=np.matrix([[4,0,1],[-2,1,0],[-2,0,1]])
matrix2=[[5,-3],[6,-4]]

def eigenValues(matrix):
  a=sp.Symbol('a')
  size=len(matrix)
  mat=sp.Matrix(matrix-a*np.identity(size,dtype='int'))
  #print(mat)
  #print(sp.det(mat))
  eigenvalues=sp.solve(sp.det(mat),a)
  return eigenvalues
  

def diagonalMatrix(matrix):
    eigen=eigenValues(matrix)
    mat=np.diag(eigen)
    return mat
    

print(diagonalMatrix(matrix2))