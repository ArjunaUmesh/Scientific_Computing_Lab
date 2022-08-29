# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 09:39:05 2022

@author: 20pt04
"""

import numpy as np
import sympy as sp
import math
import FQ1
a,x,y,z=sp.symbols('a,x,y,z')

matrix = np.array([[-10, 11, -6], [-15, 16, -10], [-3, 3, -2]])
order = len(matrix)
eValues = set(FQ1.eigen(matrix))
if len(eValues) == order:
    print("Diagonizable")
else:
    print("Not Diagonizable")