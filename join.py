import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

arr3=np.array([
    [1,2],
    [3,4]
])
arr4=np.array([
    [5,6],
    [7,8]
])


# arr=np.concatenate((arr3,arr4),axis=1)
# arr=np.stack((arr1,arr2),axis=1)
arr=np.hstack((arr1,arr2))
arr=np.vstack((arr1,arr2))
arr=np.dstack((arr1,arr2))

print(arr)
