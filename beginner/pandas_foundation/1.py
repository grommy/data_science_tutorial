# Import numpy
import numpy as np
import pandas as pd

df = pd.read_csv("DataSets/world_population.csv")

# Create array of DataFrame values: np_vals
np_vals = df.values

# Create new array of base 10 logarithm values: np_vals_log10
np_vals_log10 = np.log10(np_vals)

# Create array of new DataFrame by passing df to np.log10(): df_log10
df_log10 = np.log10(df)

# Print original and new data containers
print(type(np_vals), type(np_vals_log10))
print(type(df), type(df_log10))
