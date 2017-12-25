import numpy as np
import pandas as pd

from statistical_thinking.testing_hypothesis.data import frog_data

df = pd.DataFrame.from_dict(frog_data)
# Null hypothesis: force_a have the same distribution as force_b(mean_a is equal to mean_b)
force_a = df[df.ID == 'A']['impact_force'].values
force_b = df[df.ID == 'B']['impact_force'].values


def diff_of_means(x, y):
    return np.mean(x) - np.mean(y)

# Compute difference of mean impact force from experiment: empirical_diff_means
empirical_diff_means = diff_of_means(force_a, force_b)

# Concatenate forces: forces_concat
forces_concat = np.concatenate((force_a, force_b))

# Initialize bootstrap replicates: bs_replicates
bs_replicates = np.empty(10000, dtype=float)

for i in range(10000):
    # Generate bootstrap sample
    bs_sample = np.random.choice(forces_concat, size=len(forces_concat))

    # Compute replicate
    bs_replicates[i] = diff_of_means(bs_sample[:len(force_a)],
                                     bs_sample[len(force_a):])

# Compute and print p-value: p
p = float(np.sum(bs_replicates >= empirical_diff_means)) / len(bs_replicates)
print('p-value =', p)
# bs_replicates should contain around zero mean_diff as its created from permutations
# so, if p is really low - that means that empirical_diff_means is not 0 statistically
