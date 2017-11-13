import datetime
import pandas as pd
import matplotlib.pyplot as plt

file_name = '../DataSets/weather_data_austin_2010.csv'
# READ AND PARSE
# Prepare a format string: time_format
time_format = '%Y%m%d %H:%M'
df = pd.read_csv(file_name, parse_dates=['Date'], index_col='Date',
                  date_parser=lambda x: datetime.datetime.strptime(x, time_format))

# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-Aug-01':'2010-Aug-15']
print(type(unsmoothed))

# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling(window=24).mean()

# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed': smoothed, 'unsmoothed': unsmoothed})

# Plot both smoothed and unsmoothed data using august.plot().
august.plot()
plt.show()


