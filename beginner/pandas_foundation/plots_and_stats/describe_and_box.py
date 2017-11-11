import pandas as pd
import matplotlib.pyplot as plt

d = {'fare': [211.33750000000001,
              151.55000000000001,
              151.55000000000001,
              151.55000000000001,
              151.55000000000001,
              26.550000000000001,
              77.958299999999994,
              0.0,
              51.479199999999999,
              49.504199999999997,
              227.52500000000001,
              227.52500000000001,
              69.299999999999997,
              78.849999999999994,
              30.0,
              25.925000000000001,
              247.52080000000001,
              247.52080000000001,
              76.291700000000006,
              75.241699999999994]
     }

df = pd.DataFrame(d)
# Print summary statistics of the fare column with .describe()
print(df.fare.describe())

# Generate a box plot of the fare column
df.fare.plot(kind='box')

# Show the plot
plt.show()
