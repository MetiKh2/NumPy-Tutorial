import numpy as np

#[1,2,3,4]=> [2-1,3-2,4-3]=[1,1,1]=>[1-1,1-1]=[0,0]

arr=np.array([1,2,3,4])
arr=np.array([10,15,20,5])
print(np.diff(arr,n=2))
