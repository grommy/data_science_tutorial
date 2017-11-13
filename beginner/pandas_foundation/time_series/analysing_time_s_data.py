import pandas as pd

file_name = '../DataSets/austin_airport_departure_data_2015_july.csv'
# READ AND PARSE
df = pd.read_csv(file_name, skiprows=15, parse_dates={'Date': ['Date (MM/DD/YYYY)']}, index_col='Date')
# print(df.head())

# Strip extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip()

# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')

# Compute the total number of Dallas departures each day: daily_departures
daily_departures = dallas.resample('D').sum()

# Generate the summary statistics for daily Dallas departures: stats
stats = daily_departures.describe()
print(stats)



