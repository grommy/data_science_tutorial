import datetime
import pandas as pd

file_name = '../DataSets/weather_data_austin_2010.csv'
# READ AND PARSE
# Prepare a format string: time_format
time_format = '%Y%m%d %H:%M'
df = pd.read_csv(file_name, parse_dates=['Date'], index_col='Date',
                 date_parser=lambda x: datetime.datetime.strptime(x, time_format))
print(df.head())

# Extract the August 2010 data: august
august = df['Temperature']['2010-August']

# Resample to daily data, aggregating by max: daily_highs
daily_highs_obj = august.resample('D')
print(type(daily_highs_obj))
daily_highs = daily_highs_obj.mean()

# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = daily_highs.rolling(window=7).mean()
print(daily_highs_smoothed)
