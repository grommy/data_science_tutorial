import datetime
import pandas as pd

file_name = '../DataSets/weather_data_austin_2010.csv'
# READ AND PARSE
# Prepare a format string: time_format
time_format = '%Y%m%d %H:%M'
df = pd.read_csv(file_name, parse_dates=['Date'], index_col='Date',
                  date_parser=lambda x: datetime.datetime.strptime(x, time_format))
print(df.head())

# Downsample to 6 hour data and aggregate by mean: df1
df1 = df.Temperature.resample('6h').mean()
print(df1)

# Downsample to daily data and count the number of data points: df2
df2 = df.Temperature.resample('D')
print(df2.head())

# Extract temperature data for August: august
august = df.Temperature.loc['2010-August']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()
print(august_highs)

# Extract temperature data for February: february
february_daily = df.loc['2010-February'].resample('D', how='mean')
print(february_daily.head())

# Downsample to obtain the daily lowest temperatures in February: february_lows
print(february_daily.loc['2010-02-03', 'Temperature'])
