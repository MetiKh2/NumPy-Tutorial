import numpy as np

arr=np.array([1,2,3,4,5])
# x=arr.copy()
x=arr.view()
y=arr.copy()
arr[0]=42

print(y.base)
print(x.base)
