import numpy as np
a=np.array([[1,2,3,4], [3,-1,2,5], [1,2,3,4], [1,3,4,5]])
print('Result: ')
rank=np.linalg.matrix_rank(a)
print(rank)
