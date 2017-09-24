# Import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

# Assign the filename: file
file = '../DataSets/titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
# print(df.head())

# -----------------------------------------------
# Assign the filename: file
file = '../DataSets/digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = data.values

# Print the datatype of data_array to the shell
# print(type(data_array))
# -----------------------------------------------

# Assign filename: file
file = '../DataSets/titanic_corrupted.csv'

# Import file: data
data = pd.read_csv(file, sep=',', comment='#', na_values=['', 'Nothing'], header=0)

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

# -----------------------------------------------

