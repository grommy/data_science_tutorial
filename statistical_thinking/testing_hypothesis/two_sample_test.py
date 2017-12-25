import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statistical_thinking.utils.helpers import Permutation
from statistical_thinking.testing_hypothesis.data import frog_data

df = pd.DataFrame.from_dict(frog_data)

# Make bee swarm plot
_ = sns.swarmplot(x="ID", y="impact_force", data=df)

# Label axes
_ = plt.xlabel('frog')
_ = plt.ylabel('impact force (N)')

# Show the plot
plt.show()

# Null hypothesis: force_a have the same distribution as force_b(mean_a is equal to mean_b)
force_a = df[df.ID == 'A']['impact_force'].values
force_b = df[df.ID == 'B']['impact_force'].values


def diff_of_means(x, y):
    return np.mean(x) - np.mean(y)

# Compute difference of mean impact force from experiment: empirical_diff_means
empirical_diff_means = diff_of_means(force_a, force_b)

# Draw 10,000 permutation replicates: perm_replicates
perm_replicates = Permutation.draw_perm_reps(force_a, force_b, diff_of_means, size=10000)

# Compute p-value: p
p = (np.sum(perm_replicates >= empirical_diff_means) + 0.0) / len(perm_replicates)

# Print the result
print('p-value that mean_a is equal to mean_b = {}'.format(p))
