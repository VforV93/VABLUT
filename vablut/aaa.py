import numpy as np 

m = np.arange(81).reshape((9,9))
print(' --- --- --- O R I G I N A L --- --- --- ')
print(m)
print(' --- --- --- --- --- --- --- --- --- ')
print(np.flip(m,0))
print(' --- --- --- --- --- --- --- --- --- ')
print(np.flip(m,1))
print(' --- --- --- --- --- --- --- --- --- ')
print(np.rot90(m,3))