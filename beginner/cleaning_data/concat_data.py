import pandas as pd

# Horizontal concatenation
uber_all = pd.read_csv('DataSets/nyc_uber_2014.csv')
print(uber_all.head())
print(type(uber_all['Date/Time'][0]))

uber_all['Month'] = uber_all['Date/Time'].str[0].apply(int)

uber1 = uber_all[uber_all.Month == 4]
uber2 = uber_all[uber_all.Month == 5]
uber3 = uber_all[uber_all.Month == 6]

print(uber3.head())

# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1, uber2, uber3])

# Print the shape of row_concat
print(row_concat.shape)

# Print the head of row_concat
print(row_concat.head())

# Vertical concatenation
ebola = pd.read_csv("DataSets/ebola.csv")
print(ebola.head())

# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')
print(ebola_melt.head())
status_country = ebola[['Cases_Guinea']]
print(status_country.head())

# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())
