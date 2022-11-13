from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

 
print(random.rayleigh(scale=2,size=(2,3)))
sns.distplot(random.rayleigh(size=1000),hist=False)
plt.show()
