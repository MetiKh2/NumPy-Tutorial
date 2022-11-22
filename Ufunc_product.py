import numpy as np

arr=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
x=np.prod([arr,arr2],axis=1)

#1*2*3*4*5*6*7*8=40320
print(np.cumprod(arr))
