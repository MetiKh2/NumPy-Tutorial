from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000),hist=False)
plt.show()
# print(random.uniform(size=(2,3)))
