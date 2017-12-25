import numpy as np
import pandas as pd
from statistical_thinking.utils.helpers import Bootstrap
from statistical_thinking.testing_hypothesis.data import frog_data

"""
NULL hypothesis: mean of force_b is statistically the same as MEAN_FORCE_C
"""
df = pd.DataFrame.from_dict(frog_data)
force_b = df[df.ID == 'B']['impact_force'].values

# Make an array of translated impact forces: translated_force_b
MEAN_FORCE_C = 0.55
translated_force_b = force_b - np.mean(force_b) + MEAN_FORCE_C

# Take bootstrap replicates of Frog B's translated impact forces: bs_replicates
bs_replicates = Bootstrap.draw_bs_reps(translated_force_b, np.mean, 10000)

# Compute fraction of replicates that are less than the observed Frog B force: p
p = float(np.sum(bs_replicates <= np.mean(force_b))) / 10000

# Print the p-value
# If p is too low or too high -- reject hypothesis
print('p = ', p)


import matplotlib.pyplot as plt

_ = plt.hist(bs_replicates, bins=50)
_ = plt.axvline(x=np.mean(force_b), color='red')

_ = plt.xlabel('mean')
_ = plt.ylabel('frequency')

plt.show()


