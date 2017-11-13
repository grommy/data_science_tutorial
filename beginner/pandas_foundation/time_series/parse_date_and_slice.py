import datetime
import pandas as pd

file_name = '../DataSets/weather_data_austin_2010.csv'
df = pd.read_csv(file_name)
temperature_list = list(df.Temperature)
date_list = list(df.Date)

# Prepare a format string: time_format
time_format = '%Y%m%d %H:%M'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(date_list, format=time_format)

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temperature_list, index=my_datetimes)

# READ AND PARSE
ts0 = pd.read_csv(file_name, parse_dates=['Date'], index_col='Date',
                  date_parser=lambda x: datetime.datetime.strptime(x, time_format))
print(ts0.head())
print(ts0.info())


# Extract the hour from 9pm to 10pm on '2010-10-11': ts1
ts1 = ts0.loc['2010-10-11 21:00:00']

# Extract '2010-07-04' from ts0: ts2
ts2 = ts0.loc['2010-07-04']

# Extract data from '2010-12-15' to '2010-12-31': ts3
ts3 = ts0.loc['2010-12-15':'2010-12-31']

ts4 = ts3.reindex(my_datetimes, method='bfill')
print(ts4.head())

ts5 = ts2 + ts3
print(ts5.head())

pd.c