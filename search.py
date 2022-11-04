import numpy as np

arr=np.array([1,2,3,4,5,4,4])
arr2=np.array([1,2,3,4,5,6,7,8])
arr3=np.array([6,7,8,9])

# x=np.where(arr==4)
x=np.where(arr2%2==0)
x=np.where(arr2%2==1)
x=np.searchsorted(arr3,7,side='right')
print(x)
