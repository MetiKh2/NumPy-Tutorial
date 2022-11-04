#i integer
#b boolean
#u unsigned integer
#f float
#c complex float
#m timedelta
#M datetime
#O object
#S string
#U unicode string
import numpy as np

arr=np.array([1.1,2.1,3.5,4.7])
arr3=np.array([1,0,3])
arr2=np.array(['a','b','c'])
# arr3=np.array(['a','1','3'],dtype='i')
# newarr=arr.astype('i')
newarr=arr3.astype(bool)
print(newarr)
print(newarr.dtype)
# print(arr)
# print(arr.dtype)
# print(arr2.dtype)
