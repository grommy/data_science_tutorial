# Import the pandas package
import pandas as pd
import matplotlib.pyplot as plt


file_name = '../DataSets/world_dev_ind.csv'

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv(file_name, chunksize=1000)

# Initialize empty DataFrame: data
data = pd.DataFrame()

# Iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader:

    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    # Zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # following line will cause a warning. A value is trying to be set on a copy of a slice from a DataFrame.
    # df_pop_ceb['Total_Urban_Population'] = [int(tup[0] * tup[1]) for tup in pops_list]

    # the perfect way
    df_pop_ceb = df_pop_ceb.assign(Total_Urban_Population=[int(tup[0] * tup[1]) for tup in pops_list])

    # Append DataFrame chunk to data: data
    data = data.append(df_pop_ceb)

# to reassign a single value
data.loc[data['Year'] == 1965, 'Total_Urban_Population'] = 5000

modified_years = data[data['Total_Urban_Population'] == 5000]['Year']
print(modified_years)

# Plot urban population data
data.plot(kind='scatter', x='Year', y='Total_Urban_Population')
# data.plot(kind='scatter', x='Year', y='Total Population')
plt.show()

