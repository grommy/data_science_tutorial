import pandas as pd
import matplotlib.pyplot as plt

d = {'IBM':  [153.3099,  161.9400,  160.5,  171.2899,  169.649,  162.6600,  161.9,
              147.8899,  144.97,  140.080,  139.4,  137.6199],
     'AAPL': [117.160004,  128.46,  124.430,  125.150002,  130.279999,  125.4300,
              121.300003,  112.760002,  110.300003,  119.5,  118.300003,  105.260002],
     'Month': ['Jan',  'Feb',  'Mar',  'Apr',  'May',  'Jun',  'Jul',  'Aug',  'Sep',  'Oct',  'Nov',  'Dec']}

df = pd.DataFrame(d)

# Create a list of y-axis column names: y_columns
y_columns = ['AAPL', 'IBM']

# Generate a line plot
df.plot(x='Month', y=y_columns)

# Add the title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()
