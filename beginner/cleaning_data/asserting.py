import pandas as pd

ebola = pd.read_csv('DataSets/ebola.csv')
print(ebola.info())
# .columns
# .describe()
# column.value_counts()

# Assert that there are no missing values
assert ebola.notnull().all().all() == False

# Assert that all values are >= 0
assert (ebola >= 0).all().all() == False
