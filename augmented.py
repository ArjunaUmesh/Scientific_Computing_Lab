# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

eq1='2x+3y=7'
eq2='5x+7y=5'

eq3='15x+3y+5z=2'
eq4='12x-5y-7z=1'
eq5='17x+7y+9z=3'

eq6='4x+1y+2z=4'
eq7='3x+5y+1z=7'
eq8='1x+1y+3z=3'

eq9='3x+20y-1z=-18'
eq10='2x-3y+20z=25'
eq11='20x+1y-2z=17'

eq12='1x+1y+2z=8'
eq13='−1x−2y+3z=1'
eq14='3x−7y+4z=10'

#lines = ["2x+3y=7", "1x-1y+0", "1x+0y-3", "0x+1y-0.5"]
equations=[eq12,eq13,eq14]

def augmented_Matrix(equations):
    augmentedMatrix=[]
    for i in equations:
         z = re.findall(r'[\d\.\-]+', i)
         for i in range(0,len(z)):
             z[i]=int(z[i])
         augmentedMatrix.append(z)
        
    return augmentedMatrix


#d=augmented_Matrix(equations)
#print(d)