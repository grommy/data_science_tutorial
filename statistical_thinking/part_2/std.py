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
print(df.dem_share.var())
print(np.var(df['dem_share']))
print(df.dem_share.std())
