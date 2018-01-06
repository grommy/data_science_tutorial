import numpy as np

from statistical_thinking.regression.fertility_data import illiteracy, fertility


def pearson_r(a, b):
    return np.corrcoef(a, b)[0, 1]


# Compute observed correlation: r_obs
r_obs = pearson_r(illiteracy, fertility)

# Initialize permutation replicates: perm_replicates
perm_replicates = np.empty(10000)

# Draw replicates
for i in range(10000):
    # Permute illiteracy measurments: illiteracy_permuted
    illiteracy_permuted = np.random.permutation(illiteracy)

    # Compute Pearson correlation
    perm_replicates[i] = pearson_r(illiteracy_permuted, fertility)

# Compute p-value: p
p = np.sum(perm_replicates >= r_obs) / len(perm_replicates)
print('p-val =', p)
"You got a p-value of zero. In hacker statistics, this means that your p-value is very low, " \
    "since you never got a single replicate in the 10,000 you took that had a Pearson correlation greater " \
    "than the observed one. You could try increasing the number of replicates you take to continue to move " \
    "the upper bound on your p-value lower and lower."
