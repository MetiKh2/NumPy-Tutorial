import numpy as np

# x=np.sin(np.pi/2)
#pi/180*degree_values
# x=np.rad2deg(np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5,0]))
# x=np.deg2rad(np.array([90,180,270,360]))
# x=np.arcsin(1.0)
# x=np.arcsin(np.array([1,-1,0.1]))
base=3
perp=4
x=np.hypot(base,perp)
print(x)
