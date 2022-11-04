import numpy as np

arr=np.array([
    [1,2,3,4],
    [5,6,7,8]
])

# newarr=arr.reshape(4,3)
# newarr=arr.reshape(2,3,2)
# newarr=arr.reshape(3,3)
newarr=arr.reshape(-1)
# newarr=arr.reshape(2,2,-1)
print(newarr)
# print(newarr)
# print(arr.reshape(2,4).base)
