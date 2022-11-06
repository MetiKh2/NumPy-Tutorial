import numpy as np

arr=np.array([41,42,43,44])

# filter_arr=arr>42

# newarr=arr[filter_arr]

  #get elements are higher than 42
# for element in arr:
#     if element>42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
# newarr=arr[filter_arr]


#==============================

filter_arr=arr%2==0
newarr=arr[filter_arr]

#  get even elements
# for element in arr:
#     if element%2==0:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
# newarr=arr[filter_arr]

print(filter_arr)
print(newarr)

