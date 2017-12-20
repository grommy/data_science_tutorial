"""
https://en.wikipedia.org/wiki/Anscombe%27s_quartet
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import array

anscombe_x = [array([10., 8., 13., 9., 11., 14., 6., 4., 12., 7., 5.]),
              array([10., 8., 13., 9., 11., 14., 6., 4., 12., 7., 5.]),
              array([10., 8., 13., 9., 11., 14., 6., 4., 12., 7., 5.]),
              array([8., 8., 8., 8., 8., 8., 8., 19., 8., 8., 8.])]

anscombe_y = [array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26,
                     10.84, 4.82, 5.68]),
              array([9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13,
                     7.26, 4.74]),
              array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39,
                     8.15, 6.42, 5.73]),
              array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5,
                     5.56, 7.91, 6.89])]

# Iterate through x,y pairs
for x, y in zip(anscombe_x, anscombe_y):
    # Compute the slope and intercept: a, b
    _ = plt.plot(x, y, marker='.', linestyle='none')
    plt.show()
    a, b = np.polyfit(x, y, deg=1)

    # Print the result
    print('slope:', a, 'intercept:', b)
