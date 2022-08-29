# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:38:40 2022

@author: 20pt04
"""

import augmented
import GaussJordan

eq1='1x+1y+2z=8'
eq2='-1x-2y+3z=1'
eq3='3x-7y+4z=10'



equations=[eq1,eq2,eq3]


matrix=augmented.augmented_Matrix(equations)

gjmatrix=GaussJordan.GAUSSJORDAN(matrix)

n=len(gjmatrix[0])-1
x=[round(gjmatrix[i][n],2) for i in range(len(gjmatrix))]
print(x)

