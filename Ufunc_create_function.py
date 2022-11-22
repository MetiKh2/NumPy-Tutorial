import numpy as np

# def myadd(x,y):
#     return x+y

# myadd=np.frompyfunc(myadd,2,1)

# print(myadd([1,2,3,4],[10,11,12,13]))
# print(type(np.blahblah))

if type(np.add) ==np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')
    
