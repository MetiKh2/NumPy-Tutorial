from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
# x=random.binomial(n=10,p=0.5,size=10)
# print(x)

sns.distplot(random.binomial(n=100,p=0.5,size=1000),
label='binomial',
hist=False)
sns.distplot(random.normal(loc=50,scale=5,size=1000),hist=False,label='normal')

plt.show()
