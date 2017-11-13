import pandas as pd

file_name = '../DataSets/austin_airport_departure_data_2015_july.csv'

df1 = pd.read_csv(file_name, skiprows=15)
# Buid a Boolean mask to filter out all the 'LAX' departure flights: mask
df1.columns = df1.columns.str.strip()
mask = df1['Destination Airport'] == 'LAX'

# Use the mask to subset the data: la
la = df1[mask]
# Combine two columns of data to create a datetime series: times_tz_none
times_tz_none = pd.to_datetime(la['Date (MM/DD/YYYY)'] + ' ' + la['Wheels-off Time'])

# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')

# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')

print(times_tz_central[1])
print(times_tz_pacific[1])
