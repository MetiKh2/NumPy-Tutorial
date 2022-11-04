import numpy as np

arr=np.array([1,2,3])
arr2=np.array([
    [
    [1,2,3],
    [4,5,6]
],
[
    [7,8,9],
    [10,11,12]
]
])
# arr3=np.array(
#     [
#         [
#             [1,2]
#             ,[3,4]
#             ],
#         [
#         [5,6]
#         ,[7,8]
#         ]
#         ])
# print(arr3)
# for x in np.nditer(arr3,flags=['buffered'],op_dtypes=['S']):
#     print(x)

# for x in arr2:
#     for y in x:
#         for z in y:
#             print(z)

arr4=np.array([
    [1,2,3,4]
    ,[5,6,7,8]
])

# for x in np.nditer(arr4[:,::2]):
#     print(x)

for idx,x in np.ndenumerate(arr4):
    print(idx,x)
