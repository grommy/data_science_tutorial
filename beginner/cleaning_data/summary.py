import pandas as pd
import matplotlib.pyplot as plt

g1800s = pd.read_csv('DataSets/gapminder.csv')

print(g1800s.head())
print(g1800s.info())
print(g1800s.describe())
print(g1800s.shape)
print(g1800s.columns)

# Create the scatter plot
g1800s.plot(kind='scatter', x='1800', y='1899')

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()
