import pandas as pd

# Create a list of the new column labels: new_labels
new_labels = ['year', 'population']

# Read in the file, specifying the header and names parameters: df2
df2 = pd.read_csv('DataSets/world_population.csv', header=0, names=new_labels)

# Print both the DataFrames
print(df2)
