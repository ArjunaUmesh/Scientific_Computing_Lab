# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:49:16 2022

@author: Arjun
"""

import sympy as sp
x,y=sp.symbols('x,y')

def trapezoidal(eq, limits):
    X = []
    Y = []
    i = limits[0]
    h = 0.1

    while i <= limits[1]:
        X.append(i)
        Y.append(eq.subs(x, i))
        i += h

    ySum = 0
    for j in range(1, len(Y) - 1):
        ySum += Y[j]

    value = (h / 2) * (Y[0] + Y[-1] + 2 * ySum)

    return sp.N(value)
'''
eq = sp.log(x)
limits = [4, 5.2]
print(trapezoidal(eq, limits))
'''


def simpsons1by3(eq, limits):
    X = []
    Y = []
    i = limits[0]
    h = 0.1

    while i <= limits[1]:
        X.append(i)
        Y.append(eq.subs(x, i))
        i += h

    yOdd = 0
    yEven = 0
    for j in range(1, len(Y) - 1):
        if j % 2 == 0:
            yEven += Y[j]
        else:
            yOdd += Y[j]

    value = (h / 3) * (Y[0] + Y[-1] + 2 * yEven + 4 * yOdd)

    return sp.N(value)

'''
eq = log(x)
limits = [4, 5.2]
print(simpsons1by3(eq, limits))
'''


def simpsons3by8(eq, limits):
    X = []
    Y = []
    i = limits[0]
    h = 0.1

    while i <= limits[1]:
        X.append(i)
        Y.append(eq.subs(x, i))
        i += h

    y3 = 0
    yRest = 0
    for j in range(1, len(Y) - 1):
        if j % 3 == 0:
            y3 += Y[j]
        else:
            yRest += Y[j]

    value = (3 * h / 8) * (Y[0] + Y[-1] + 2 * y3 + 3 * yRest)

    return sp.N(value)

'''
eq = log(x)
limits = [4, 5.2]
print(simpsons3by8(eq, limits))
'''

t = [x for x in range(0, 41, 5)]
V = [30, 24, 19.5, 16, 13.6, 11.7, 10.0, 8.5, 7.0]

#SIMPSONS RULE
h = t[1] - t[0]
yOdd = 0
yEven = 0

for j in range(1, len(V) - 1):
    if j % 2 == 0:
        yEven += V[j]
    else:
        yOdd += V[j]

value = (h / 3) * (V[0] + V[-1] + 2 * yEven + 4 * yOdd)

print("The distance moved by the train in 40 seconds is ", value, " metres", sep = "")



#TRAPZOIDAL RULE

h = t[1] - t[0]
X = []
Y = []
#i = sp.limits[0]

ySum = 0
for j in range(1, len(V) - 1):
    ySum += V[j]

value = (h / 2) * (V[0] + V[-1] + 2 * ySum)

print("The distance moved by the train in 40 seconds is ", value, " metres", sep = "")