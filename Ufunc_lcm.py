import numpy as np

# 4*3=12,6*2=12
# x=np.lcm(4,6)
# x=np.lcm.reduce(np.array([3,6,9]))
x=np.lcm.reduce(np.arange(1,11))
print(x)
