import numpy as np
from math import factorial
import matplotlib.pyplot as plt

x=[1.340, 1.345, 1.350, 1.355, 1.360, 1.365, 1.370, 1.375, 1.380, 1.385, 1.390]
y=[4.2556, 4.3532, 4.4552, 4.4518, 4.6734, 4.7903, 4.9130, 5.0419, 5.1774, 5.3201, 5.4706]
h = x[1] - x[0]
x1=1.361
x2=1.394
q=(x1 - x[0])/h
q1 = (x2-x[-1])/h
def n(y,j):
    mas=[]
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0)
    if j == 1:
        return mas
    else:
        j-=1
        return n(mas, j)
s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3)
s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4)
s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)
s_5 = q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*n(y,6)[0]/factorial(6)
s_6 = q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*n(y,7)[0]/factorial(7)
s_7 = q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7)*n(y,8)[0]/factorial(8)
s_8 = q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7)*(q-8)*n(y,9)[0]/factorial(9)
s_9 = q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7)*(q-8)*(q-9)*n(y,10)[0]/factorial(10)
n_1 = s_1 + s_2 + s_3 + s_4 + s_5 + s_6 + s_7 + s_8 + s_9
print ('The value of a function at a point x1=', x1, 'using Newton*s First Interpolation Formula', round(n_1,5))

t1 = y[10] + q1*n(y,1)[9]+q1*(q1+1)*n(y,2)[8]/factorial(2)
t2 = q1*(q1+1)*(q1+2)*n(y,3)[7]/factorial(3)
t3 = q1*(q1+1)*(q1+2)*(q1+3)*n(y,4)[6]/factorial(4)
t4 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*n(y,5)[5]/factorial(5)
t5 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*n(y,6)[4]/factorial(6)
t6 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*(q1+6)*n(y,7)[3]/factorial(7)
t7 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*(q1+6)*(q1+7)*n(y,8)[2]/factorial(8)
t8 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*(q1+6)*(q1+7)*(q1+8)*n(y,9)[1]/factorial(9)
t9 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*(q1+6)*(q1+7)*(q1+8)*(q1+9)*n(y,10)[0]/factorial(10)
n_2 =  t1+t2+t3+t4+t5+t6+t7+t8+t9
print ('The value of a function at a point x2=', x2, 'using Newton*s Second Interpolation Formula', round(n_2,5))

x_1=np.linspace(np.min(x), np.max(x))
y_1=np.linspace(np.min(y), np.max(y))
plt.plot(x,y, 'ro', x_1, y_1)
plt.title('Graph of the interpolation function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
