import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return x**4+2*x**3+2*x**2+6*x-5
a = -3/2.
b = 1.
eps = 0.0001
def rec_dyhotomy(a, b, eps):
    if abs(f(b) - f(a)) < eps:
        print('Обчислюємо корінь')
        return
    mid = (a+b) / 2
    if f(mid) == 0 or abs(f(mid)) < eps:
        print(f'Корінь знаходиться в точці x = {mid}')
    elif f(a)*f(mid) < 0:
        rec_dyhotomy(a, mid, eps)
    else:
        rec_dyhotomy(mid, b, eps)
#rec_dyhotomy(a, b, eps)

x = np.arange(a, b, 0.001)

plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Метод ділення навпіл')
plt.grid()
plt.show()
