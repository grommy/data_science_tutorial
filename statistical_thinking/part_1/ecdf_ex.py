import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1.0, 1.0+n) / n

    return x, y

swing_states = pd.read_csv("../DataSets/2008_swing_states.csv")

df_filter = swing_states['state'] == 'PA'
df = swing_states[df_filter]


# Compute ECDF for versicolor data: x_vers, y_vers
x_dem_v, y_dem_v = ecdf(df.dem_votes)
x_total_v, y_total_v = ecdf(df.total_votes)


# Generate plot
sns.set()

dem_v_plt = plt.plot(x_dem_v, y_dem_v, marker='.', linestyle='none', label="dem_votes")
total_v_plt = plt.plot(x_total_v, y_total_v, marker='.', linestyle='none', label="total_votes")

# Make the margins nice
plt.margins(0.02)

# Label the axes
plt.xlabel('votes')
plt.ylabel('ECDF')
plt.legend()


# Display the plot
plt.show()
