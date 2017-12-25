import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statistical_thinking.utils.helpers import Bootstrap
from statistical_thinking.testing_hypothesis.data import frog_data

df = pd.DataFrame.from_dict(frog_data)

# Make bee swarm plot
_ = sns.swarmplot(x="ID", y="impact_force", data=df)

# Label axes
_ = plt.xlabel('frog')
_ = plt.ylabel('impact force (N)')

# Show the plot
plt.show()

# Null hypothesis: force_a has mean equal to the mean of force_b
# (we don't rely on fact that distribution is the same)
force_a = df[df.ID == 'A']['impact_force'].values
force_b = df[df.ID == 'B']['impact_force'].values


def diff_of_means(x, y):
    return np.mean(x) - np.mean(y)


empirical_diff_means = diff_of_means(force_a, force_b)

# Compute mean of all forces: mean_force
forces_concat = np.concatenate((force_a, force_b))
mean_force = np.mean(forces_concat)

# Generate shifted arrays
force_a_shifted = force_a - np.mean(force_a) + mean_force
force_b_shifted = force_b - np.mean(force_b) + mean_force

# Compute 10,000 bootstrap replicates from shifted arrays
bs_replicates_a = Bootstrap.draw_bs_reps(force_a_shifted, np.mean, size=10000)
bs_replicates_b = Bootstrap.draw_bs_reps(force_b_shifted, np.mean, size=10000)

# Get replicates of difference of means: bs_replicates
bs_replicates = bs_replicates_a - bs_replicates_b

# Compute and print p-value: p
p = float(np.sum(bs_replicates >= empirical_diff_means)) / len(bs_replicates)
print('p-value =', p)
# bs_replicates should contain around zero mean_diff as its created from permutations
# so, if p is really low - that means that empirical_diff_means is not 0 statistically
