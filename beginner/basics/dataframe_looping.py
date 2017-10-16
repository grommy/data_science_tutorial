# Iterating over numpy array
# For loop over np_baseball
# for aa in np.nditer(np_baseball):
#     print(aa)

# Import cars data
import pandas as pd
cars = pd.read_csv('../DataSets/cars.csv', index_col=0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)
    
# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
    
# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
