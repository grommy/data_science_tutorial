import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

swing_states = pd.read_csv("../DataSets/2008_swing_states.csv")
print(swing_states.head())

df_filter = swing_states['state'].isin(['PA', 'OH', 'FL'])
df = swing_states[df_filter]

print(df.head())

# Create bee swarm plot with Seaborn's default settings
sns.swarmplot(x='state', y='dem_share', data=df)

# Label the axes
plt.xlabel('state')
plt.ylabel('% of votes for democrats')

# Show the plot
plt.show()


