import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statistical_thinking.case_study.data import finches_df as df

# Create bee swarm plot
from statistical_thinking.utils.helpers import ecdf, Bootstrap, diff_of_means

_ = sns.swarmplot(data=df, x='year', y='beak_depth')

# Label the axes
_ = plt.xlabel('year')
_ = plt.ylabel('beak depth (mm)')

# Show the plot
plt.show()

bd_1975 = df[df.year == 1975]['beak_depth']
bd_2012 = df[df.year == 2012]['beak_depth']

# Compute ECDFs
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

# Plot the ECDFs
_ = plt.plot(x_1975, y_1975, marker='.', linestyle='none')
_ = plt.plot(x_2012, y_2012, marker='.', linestyle='none')

# Set margins
plt.margins(0.02)

# Add axis labels and legend
_ = plt.xlabel('beak depth (mm)')
_ = plt.ylabel('ECDF')
_ = plt.legend(('1975', '2012'), loc='lower right')

# Show the plot
plt.show()

# Compute the difference of the sample means: mean_diff
mean_diff = diff_of_means(bd_2012, bd_1975)

# Get bootstrap replicates of means
bs_replicates_1975 = Bootstrap.draw_bs_reps(bd_1975, np.mean, size=10000)
bs_replicates_2012 = Bootstrap.draw_bs_reps(bd_2012, np.mean, size=10000)

# Compute samples of difference of means: bs_diff_replicates
bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975

# Compute 95% confidence interval: conf_int
conf_int = np.percentile(bs_diff_replicates, [2.5, 97.5])

# Print the results
print('difference of means =', mean_diff, 'mm')
print('95% confidence interval =', conf_int, 'mm')

# Testing the hypothesis that the means of beaks are equal (but can be from different distribution)
# Compute mean of combined data set: combined_mean
combined_mean = np.mean(np.concatenate((bd_1975, bd_2012)))

# Shift the samples
bd_1975_shifted = bd_1975 - np.mean(bd_1975) + combined_mean
bd_2012_shifted = bd_2012 - np.mean(bd_2012) + combined_mean

# Get bootstrap replicates of shifted data sets
bs_replicates_1975 = Bootstrap.draw_bs_reps(bd_1975_shifted, np.mean, size=10000)
bs_replicates_2012 = Bootstrap.draw_bs_reps(bd_2012_shifted, np.mean, size=10000)

# Compute replicates of difference of means: bs_diff_replicates
bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975

# Compute the p-value
p = np.sum(bs_diff_replicates >= mean_diff) / len(bs_diff_replicates)

# Print p-value
print('p =', p)

"""
We get a p-value of 0.0034, which suggests that there is a statistically significant difference. But remember: it is
very important to know how different they are! In the previous exercise, you got a difference of 0.2 mm between the
means. You should combine this with the statistical significance. Changing by 0.2 mm in 37 years is substantial
by evolutionary standards. If it kept changing at that rate, the beak depth would double in only 400 years.
"""
