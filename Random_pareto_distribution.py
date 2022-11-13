from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

print(random.pareto(a=2,size=(2,3))) 

sns.distplot(random.pareto(a=2,size=1000),kde=False)
plt.show()
