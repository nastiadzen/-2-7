import numpy as np
from scipy import optimize
from scipy.misc import derivative
import math
x0 = 1.8
y0 = 0.6
delta = 0.1
def f1(y):
    return math.sin(y+1)+0.8
def f2 (x):
    return -1*math.sin(x-1)+1.3
def iter (x,y,e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print ('Simple iteration:')
    print ('x=', yn, '\ny=',xn,'\nThe amount of iteration = ',n)
iter(x0,y0,0.001)
