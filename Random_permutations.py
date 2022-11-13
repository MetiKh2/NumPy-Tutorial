from numpy import random
import numpy as np

arr=np.array([1,2,3,4,5])

# random.shuffle(arr)
arr2=random.permutation(arr)
print(arr)
print(arr2)
