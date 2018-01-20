import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso

# Read the CSV file into a DataFrame: df
df = pd.read_csv('../DataSets/gm_2008_region.csv')

# Create arrays for features and target variable
y = df.life.values
del df['life']
del df['Region']
df_columns = df.columns
X = df.values

# Instantiate a lasso regressor: lasso
lasso = Lasso(alpha=0.2, normalize=True)

# Fit the regressor to the data
lasso.fit(X, y)

# Compute and print the coefficients
lasso_coef = lasso.coef_
print(lasso_coef)


# Plot the coefficients
plt.plot(range(len(df_columns)), lasso_coef)
plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
plt.margins(0.02)
plt.show()
# HIV and Child_mortality are the most important as we see

