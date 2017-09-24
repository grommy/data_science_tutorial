import numpy as np
# Assign the filename: file
file = '../DataSets/titanic.csv'

# Import records from csv
d = np.recfromcsv(file, delimiter=',', names=True, dtype=None)
print(type(d))
print(d[:3])
