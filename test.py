import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# scatter plot
mean, cov = [4, 6], [(1.5, .7), (.7, 1)]
x, y = np.random.multivariate_normal(mean, cov, 80).T
sns.regplot(x=x, y=y, color="g", scatter=True, fit_reg=False)
plt.show()

# line plot
x = np.arange(10)
y = x**2
sns.pointplot(x, y, markers=[""])
sns.regplot(x=x, y=y, color="yellow", scatter=True, fit_reg=False)
plt.show()

# histogram
mean, cov = [4, 6], [(1.5, .7), (.7, 1)]
x, y = np.random.multivariate_normal(mean, cov, 80).T
sns.distplot(x, hist=True, kde=False)
plt.show()

# density
mean, cov = [4, 6], [(1.5, .7), (.7, 1)]
x, y = np.random.multivariate_normal(mean, cov, 80).T
sns.distplot(x, hist=False, kde=True)
plt.show()

# bar
tips = sns.load_dataset('tips')
sns.barplot(x="day", y="total_bill", ci=None, data=tips)
plt.show()

# boxplot
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

# area
# ???

# faceting
sns.factorplot(x="day", y="total_bill", data=tips, col="time", kind="bar")
plt.show()

p = sns.FacetGrid(tips, col="time",  row="smoker")
p = sns.FacetGrid(tips, col=None, row=None)
p.map(plt.scatter, "total_bill", "tip", edgecolor="w")
p.map(plt.plot, "total_bill", "tip")
plt.show()
