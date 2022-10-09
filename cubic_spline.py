# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:46:53 2022

@author: Arjun
"""
import sympy as sp


x = [0, 1, 2, 3]
y = [1, 2, 9, 28]
X = 2.5

x = [1, 2, 3, 4]
y = [1, 5, 11, 8]
X0 = 1.5

h = x[1] - x[0]
n = len(x) - 1

X = sp.symbols('X')
m = sp.symbols('m0:%d' % (n + 1))
M = {0: 0, n: 0}
expr = []

for i in range(1, n):
     expr.append(m[i - 1] + 4 * m[i] + m[i + 1] - (6 / h ** 2) * (y[i - 1] - 2 * y[i] + y[i + 1]))
     for j in M:
         expr[i - 1] = expr[i - 1].subs(m[j], M[j])

sol = sp.solve(tuple(expr), tuple(m))

for i in range(len(sol)):
    M[i + 1] = sol[m[i + 1]]

ind = 0
for i in range(n):
    if X0 >= x[i]:
        ind = i + 1

Y = (x[ind] - X0) ** 3 * M[ind - 1] / (6 * h) + (X0 - x[ind - 1]) ** 3 * M[ind] / (6 * h) + (x[ind] - X0) * (y[ind - 1] - (h ** 2 / 6) * M[ind - 1]) / h + (X0 - x[ind - 1]) * (y[ind] - h ** 2 * M[ind] / 6) / h
print("(", X0, ", ", Y, ")", sep = "")




#______________________________________________________________________________


import numpy as np
from math import sqrt

def cubic_interp1d(x0, x, y):
    """
    Interpolate a 1-D function using cubic splines.
      x0 : a float or an 1d-array
      x : (N,) array_like
          A 1-D array of real/complex values.
      y : (N,) array_like
          A 1-D array of real values. The length of y along the
          interpolation axis must be equal to the length of x.

    Implement a trick to generate at first step the cholesky matrice L of
    the tridiagonal matrice A (thus L is a bidiagonal matrice that
    can be solved in two distinct loops).

    additional ref: www.math.uh.edu/~jingqiu/math4364/spline.pdf 
    """
    x = np.asfarray(x)
    y = np.asfarray(y)

    # remove non finite values
    # indexes = np.isfinite(x)
    # x = x[indexes]
    # y = y[indexes]

    # check if sorted
    if np.any(np.diff(x) < 0):
        indexes = np.argsort(x)
        x = x[indexes]
        y = y[indexes]

    size = len(x)

    xdiff = np.diff(x)
    ydiff = np.diff(y)

    # allocate buffer matrices
    Li = np.empty(size)
    Li_1 = np.empty(size-1)
    z = np.empty(size)

    # fill diagonals Li and Li-1 and solve [L][y] = [B]
    Li[0] = sqrt(2*xdiff[0])
    Li_1[0] = 0.0
    B0 = 0.0 # natural boundary
    z[0] = B0 / Li[0]

    for i in range(1, size-1, 1):
        Li_1[i] = xdiff[i-1] / Li[i-1]
        Li[i] = sqrt(2*(xdiff[i-1]+xdiff[i]) - Li_1[i-1] * Li_1[i-1])
        Bi = 6*(ydiff[i]/xdiff[i] - ydiff[i-1]/xdiff[i-1])
        z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]

    i = size - 1
    Li_1[i-1] = xdiff[-1] / Li[i-1]
    Li[i] = sqrt(2*xdiff[-1] - Li_1[i-1] * Li_1[i-1])
    Bi = 0.0 # natural boundary
    z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]

    # solve [L.T][x] = [y]
    i = size-1
    z[i] = z[i] / Li[i]
    for i in range(size-2, -1, -1):
        z[i] = (z[i] - Li_1[i-1]*z[i+1])/Li[i]

    # find index
    index = x.searchsorted(x0)
    np.clip(index, 1, size-1, index)

    xi1, xi0 = x[index], x[index-1]
    yi1, yi0 = y[index], y[index-1]
    zi1, zi0 = z[index], z[index-1]
    hi1 = xi1 - xi0

    # calculate cubic
    f0 = zi0/(6*hi1)*(xi1-x0)**3 + \
         zi1/(6*hi1)*(x0-xi0)**3 + \
         (yi1/hi1 - zi1*hi1/6)*(x0-xi0) + \
         (yi0/hi1 - zi0*hi1/6)*(xi1-x0)
    return f0

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    x = np.linspace(0, 10, 11)
    y = np.sin(x)
    plt.scatter(x, y)

    x_new = np.linspace(0, 10, 201)
    plt.plot(x_new, cubic_interp1d(x_new, x, y))

    plt.show()