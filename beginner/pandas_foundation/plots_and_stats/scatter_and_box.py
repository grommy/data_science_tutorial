import matplotlib.pyplot as plt
import pandas as pd

d = {
    'mpg': [18.0, 15.0, 18.0, 16.0, 17.0, 15.0, 14.0, 14.0, 14.0, 15.0],
    'hp': [130, 165, 150, 150, 140, 198, 220, 215, 225, 190],
    'weight': [3504, 3693, 3436, 3433, 3449, 4341, 4354, 4312, 4425, 3850],
}

df = pd.DataFrame(d)
sizes = [51.12044694,  56.78387977,  49.15557238,  49.06977358,
         49.52823321,  78.4595872,  78.93021696,  77.41479205,
         81.52541106,  61.71459825]

# Generate a scatter plot
df.plot(kind='scatter', x='hp', y='mpg', s=sizes)

# Add the title
plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()

# Make a list of the column names to be plotted: cols
cols = ['weight', 'mpg']

# Generate the box plots
df[cols].plot(kind='box', subplots=True)

# Display the plot
plt.show()
