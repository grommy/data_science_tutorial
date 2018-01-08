import matplotlib.pyplot as plt
import numpy as np

# Make scatter plot of 1975 data
from statistical_thinking.case_study.data import bl_1975, bd_1975, bl_2012, bd_2012
from statistical_thinking.utils.helpers import Bootstrap

# _ = plt.plot(bl_1975, bd_1975, marker='.',
#              linestyle='none', color='blue', alpha=0.5)
#
# # Make scatter plot of 2012 data
# _ = plt.plot(bl_2012, bd_2012, marker='.',
#              linestyle='none', color='red', alpha=0.5)
#
# # Label axes and make legend
# _ = plt.xlabel('beak length (mm)')
# _ = plt.ylabel('beak depth (mm)')
# _ = plt.legend(('1975', '2012'), loc='upper left')
#
# # Show the plot
# plt.show()


# Compute the linear regressions
slope_1975, intercept_1975 = np.polyfit(bl_1975, bd_1975, 1)
slope_2012, intercept_2012 = np.polyfit(bl_2012, bd_2012, 1)
# Perform pairs bootstrap for the linear regressions
bs_slope_reps_1975, bs_intercept_reps_1975 = \
    Bootstrap.draw_bs_pairs_linreg(bl_1975, bd_1975, size=100)
bs_slope_reps_2012, bs_intercept_reps_2012 = \
    Bootstrap.draw_bs_pairs_linreg(bl_2012, bd_2012, size=100)


# Compute confidence intervals of slopes
slope_conf_int_1975 = np.percentile(bs_slope_reps_1975, [2.5, 97.5])
intercept_conf_int_1975 = np.percentile(bs_intercept_reps_1975, [2.5, 97.5])

slope_conf_int_2012 = np.percentile(bs_slope_reps_2012, [2.5, 97.5])
intercept_conf_int_2012 = np.percentile(bs_intercept_reps_2012, [2.5, 97.5])


# Print the results
print('1975: slope =', slope_1975,
      'conf int =', slope_conf_int_1975)
print('1975: intercept =', intercept_1975,
      'conf int =', intercept_conf_int_1975)
print('2012: slope =', slope_2012,
      'conf int =', slope_conf_int_2012)
print('2012: intercept =', intercept_2012,
      'conf int =', intercept_conf_int_2012)

# Make scatter plot of 1975 data
_ = plt.plot(bl_1975, bd_1975, marker='.',
             linestyle='none', color='blue', alpha=0.5)

# Make scatter plot of 2012 data
_ = plt.plot(bl_2012, bd_2012, marker='.',
             linestyle='none', color='red', alpha=0.5)

# Label axes and make legend
_ = plt.xlabel('beak length (mm)')
_ = plt.ylabel('beak depth (mm)')
_ = plt.legend(('1975', '2012'), loc='upper left')

# Generate x-values for bootstrap lines: x
x = np.array([10, 17])

# Plot the bootstrap lines
for i in range(100):
    plt.plot(x, bs_slope_reps_1975[i]*x + bs_intercept_reps_1975[i],
             linewidth=0.5, alpha=0.2, color='blue')
    plt.plot(x, bs_slope_reps_2012[i]*x + bs_intercept_reps_2012[i],
             linewidth=0.5, alpha=0.2, color='red')

# Draw the plot again
plt.show()