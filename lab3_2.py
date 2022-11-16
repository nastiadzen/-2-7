import sympy as sp
from sympy import *
from scipy.misc import derivative
def f(x):
    return x**4+2*x**3+2*x**2+6*x-5
a=-3/2
b=1
eps=0.0001
def some(a,b,eps):
    if derivative(f,a,n=1)*derivative(f,a,n=2) < 0:
        a0=b
        b0=a
    else:
        a0=a
        b0=b
    xp1=a0
    xp2=b0
    while abs(xp2-xp1) >eps:
        xn1=xp1-f(xp1)*(xp2-xp1)/(f(xp2)-f(xp1))
        xn2=xp2-f(xp2)/derivative(f,xp2,n=1)
        xp1 = xn1
        xp2 = xn2
    x = (xp1+xp2)/2
    print(x)
some(a,b,eps)
