# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statistical_thinking.regression.fertility_data import fertility, illiteracy

# illiteracy = np.array(range(0, 101))
# fertility = illiteracy * 2 + 1 + np.random.randint(-1, 7, size=101)

# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Perform a linear regression using np.polyfit(): a, b
z = np.polyfit(illiteracy, fertility, deg=1)
print(z)
a, b = z

# Print the results to the screen
print('slope =', a, 'children per woman / percent illiterate')
print('intercept =', b, 'children per woman')

# Make theoretical line to plot
x = np.array([0, 100])
y = a * x + b

# Add regression line to your plot
_ = plt.plot(x, y)

# Draw the plot
plt.show()


# Optimizing RSS 
# Specify slopes to consider: a_vals
a_vals = np.linspace(0, 4, 200)

# Initialize sum of square of residuals: rss
rss = np.empty_like(a_vals)

# Compute sum of square of residuals for each value of a_vals
for i, a in enumerate(a_vals):
    rss[i] = np.sum((fertility - a*illiteracy - b)**2)

# Plot the RSS
plt.plot(a_vals, rss, '-')
plt.xlabel('slope (children per woman / percent illiterate)')
plt.ylabel('sum of square of residuals')

plt.show()
