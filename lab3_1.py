import numpy as np
import math
from scipy.misc import derivative
def f(x):
    return x**4+2*x**3+2*x**2+6*x-5
a = -3/2.
b = 1
eps = 0.0001
def nuton(a,b,eps):
    df = derivative(f, b, n = 1)
    df2 = derivative(f, b, n = 2)
    if (df*df2>0):
        xi = b
    else:
        xi = a
    df = derivative(f,xi, n= 1)
    xi_1 = xi - f(xi)/df
    while (abs(xi_1 - xi)>eps):
        xi = xi_1
        xi_1 = xi - f(xi)/df
    return print ('Solving the equation by Newton*s method x = ', xi_1)
nuton (a,b,eps)
