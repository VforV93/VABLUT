import numpy as np 

a = np.asarray([1,2,3,4,5], dtype=int)

a[a==3] = 15
print(a)
