import pandas as pd

list_keys = [1, 2]
list_values = [['United States', 'Soviet Union', 'United Kingdom'], [1118, 473, 273]]  # list of lists

# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys, list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)

# Assign the list of labels to the columns attribute: df.columns
df.columns = ['Country', 'Total']
print(df)
