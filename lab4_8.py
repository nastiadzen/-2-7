import numpy as np
a = np.matrix('3,-5,3; 1,2,1; 2,7,-1')
b = np.matrix('1; 4; 8')
print('A=', a)
print('B=', b)
a_inv = np.linalg.inv(a)
print(a_inv)
x = a_inv.dot(b)
print('X=',x)
