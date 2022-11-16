import numpy as np
n,m=2,3
a=np.random.random((n,m))-0.5
print(a)
b=np.abs(a).sum(axis=0)
print(min(a[:, b.argmax()]))
