# %%
from re import T
import numpy as np
from matplotlib import pyplot as plt
from IPython import get_ipython
from scipy import stats
import seaborn as sns

# %%
# plot distributoion of log-normal distribution

fig = plt.figure(figsize=(8, 4))
x = np.linspace(0, 5, 10000)

# pdf of log-normal distribution
pdf = stats.lognorm.pdf(x, 1, 0, 1)

test = plt.plot(x, pdf)
# draw a vertical line at peak
plt.axvline(x=x[736], color="k", linestyle="--")

# set x-axis limit
plt.xlim(0, 5)
plt.ylim(0.02, 0.7)
plt.xlabel("x")
plt.ylabel("Distribution")
plt.yticks([])
plt.show()
