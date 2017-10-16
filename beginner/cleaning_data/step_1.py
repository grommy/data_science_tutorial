# Import pandas
import pandas as pd
import matplotlib.pyplot as plt

# Read the file into a DataFrame: df
df = pd.read_csv('DataSets/dob_job_application_filings_subset.csv')

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

df_subset = df[['Job #', 'Doc #', 'Borough', 'Initial Cost', 'Total Est. Fee',
                'Existing Zoning Sqft', 'Proposed Zoning Sqft', 'Enlargement SQ Footage', 'Street Frontage',
                'ExistingNo. of Stories', 'Proposed No. of Stories', 'Existing Height', 'Proposed Height']]
# # Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())

# Print the info of df_subset
print(df_subset.info())

print(df_subset.describe())

# # FIND THE OUTLIERS
#
# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)
# Display the histogram
plt.show()

print(df[['Initial Cost']].head())
df["initial_cost"] = df["Initial Cost"].apply(lambda x: float(x[1:]) if x else None)
print(df[['initial_cost']].head())
print(df['initial_cost'].value_counts(dropna=False))

# Create the boxplot
df.boxplot(column='initial_cost', by='Borough', rot=90)
# Display the plot
plt.show()

# Create and display the first scatter plot
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()
# Create and display the second scatter plot
df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()
