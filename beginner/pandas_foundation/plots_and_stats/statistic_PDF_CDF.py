import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../DataSets/tips.csv')

# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF
df.fraction.plot(ax=axes[0], bins=30, kind='hist', normed=True, range=(0, .3))

# Plot the CDF
df.fraction.plot(ax=axes[1], kind='hist', bins=30, normed=True, cumulative=True, range=(0, .3))

plt.show()
