# Import numpy as np
import numpy as np
import matplotlib.pyplot as plt
# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# Use randint() to simulate a dice
print(np.random.randint(1, 7))

# -------------------------
np.random.seed(123)
random_walk = [0]

for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1, 7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step += 1
    else:
        step += np.random.randint(1, 7)

    random_walk.append(step)

# Plot random_walk

plt.plot(random_walk)
# Show the plot
plt.show()
