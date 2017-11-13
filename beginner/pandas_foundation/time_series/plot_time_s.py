import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../DataSets/weather_data_austin_2010.csv', parse_dates=True, index_col='Date')

# Plot the summer data
df.Temperature['2010-Jun':'2010-Aug'].plot(title='All')
plt.ylabel('Temp')
plt.show()
plt.clf()

# Plot the one week data
df.Temperature['2010-06-10':'2010-06-17'].plot(title='Weekly')
plt.show()
plt.clf()
