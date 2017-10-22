import pandas as pd
import numpy as np

airquality = pd.read_csv("DataSets/airquality.csv")

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=["Month", "Day"], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt)

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=["Month", "Day"],
                                               columns="measurement", values="reading",
                                               aggfunc=np.mean)

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the new index of airquality_pivot
print(airquality_pivot.index)

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the head of airquality
print(airquality.head())
