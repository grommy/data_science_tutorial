import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

swing_states = pd.read_csv("../DataSets/2008_swing_states.csv")

df_filter = swing_states['state'] == 'FL'
df = swing_states[df_filter]

print(df.head())

# mean and median
print(df.dem_share.mean())
print(df.dem_share.median())

# mode
print(df.mode(axis=0)['dem_share'][0])
print(df.dem_share.mode()[0])

# std
print(df.dem_share.std())

# Specify array of percentiles: percentiles
percentiles = np.array([2.5, 25.0, 50.0, 75.0, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(df.dem_share, percentiles)
print(ptiles_vers)

# Plot the CDF
df['dem_share'].hist(bins=100, normed=True, cumulative=True, color='red')
# _ = plt.plot(x=ptiles_vers, y=percentiles/100, marker='D', color='red', linestyle='none')

plt.show()

# If you need help
# help(sns.boxplot)
# sns.boxplot?

# Create box plot with Seaborn's default settings
_ = sns.boxplot(x='state', y='dem_share', data=swing_states)

# Label the axes
_ = plt.xlabel('region')
_ = plt.ylabel('percent of vote for Obama')

# Show the plot
plt.show()

