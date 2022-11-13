from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size=1000),hist=False,label='logistic')
sns.distplot(random.normal(size=1000,scale=2),hist=False,label='normal')
plt.show()
# print(random.logistic(loc=1,scale=2,size=(2,3)))
