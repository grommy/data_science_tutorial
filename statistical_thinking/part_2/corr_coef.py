import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

swing_states = pd.read_csv("../DataSets/2008_swing_states.csv")

df_filter = swing_states['state'] == 'FL'
df = swing_states[df_filter]
dem_share = df['dem_share']
total_votes = df['total_votes']

# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(total_votes, dem_share)
# Extract covariance
total_dem_cov = covariance_matrix[0, 1]
print(total_dem_cov)

pearson = np.corrcoef(total_votes, dem_share)
print(pearson[0, 1])

_ = plt.plot(total_votes/1000, dem_share, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('total_votes')
plt.ylabel('dem_share')

plt.show()

