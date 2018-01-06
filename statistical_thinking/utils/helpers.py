import numpy as np


class Permutation(object):

    @staticmethod
    def permutation_sample(data1, data2):
        """Generate a permutation sample from two data sets."""

        # Concatenate the data sets: data
        data = np.concatenate((data1, data2))

        # Permute the concatenated array: permuted_data
        permuted_data = np.random.permutation(data)

        # Split the permuted array into two: perm_sample_1, perm_sample_2
        perm_sample_1 = permuted_data[:len(data1)]
        perm_sample_2 = permuted_data[len(data1):]

        return perm_sample_1, perm_sample_2

    @classmethod
    def draw_perm_reps(cls, data_1, data_2, func, size=1):
        """Generate multiple permutation replicates."""

        # Initialize array of replicates: perm_replicates
        perm_replicates = np.empty(size)

        for i in range(size):
            # Generate permutation sample
            perm_sample_1, perm_sample_2 = cls.permutation_sample(data_1, data_2)

            # Compute the test statistic
            perm_replicates[i] = func(perm_sample_1, perm_sample_2)

        return perm_replicates


class Bootstrap(object):
    @staticmethod
    def bootstrap_replicate_1d(data, func):
        """Generate bootstrap replicate of 1D data."""
        bs_sample = np.random.choice(data, len(data))
        return func(bs_sample)

    @classmethod
    def draw_bs_reps(cls, data, func, size=1):
        """Draw bootstrap replicates."""

        # Initialize array of replicates: bs_replicates
        bs_replicates = np.empty(size)

        # Generate replicates
        for i in range(0, size):
            bs_replicates[i] = cls.bootstrap_replicate_1d(data, func)

        return bs_replicates


def ecdf(data):
        """Compute ECDF for a one-dimensional array of measurements."""

        # Number of data points: n
        n = len(data)

        # x-data for the ECDF: x
        x = np.sort(data)

        # y-data for the ECDF: y
        y = np.arange(1.0, 1.0+n) / n

        return x, y


def diff_of_means(a, b):
    return np.mean(a) - np.mean(b)
