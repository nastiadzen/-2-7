from scipy.misc import derivative
a=-3/2
b=1
eps=0.0001
def f(x):
    return x**4+2*x**3+2*x**2+6*x-5
def hord (a, b, eps):
    if (f(a)*derivative(f, a, n = 2)>0):
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
    xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))
    while (abs(xi_1 - xi) > eps):
        xi = xi_1
        xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))
    print(f'Метод хорд.Корінь знаходиться в точці x =', round(xi_1,5))
hord(a,b,eps)
