import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


path = "DataSets/house-votes-84.csv"
columns = ['party', 'infants', 'water', 'budget', 'physician', 'salvador',
           'religious', 'satellite', 'aid', 'missile', 'immigration', 'synfuels',
           'education', 'superfund', 'crime', 'duty_free_exports', 'eaa_rsa']
df = pd.read_csv(path, header=None, names=columns, na_values='?')
df1 = df.filter(items=['party', 'education'])
df1 = df1.dropna()
df1.replace({'education': {'n': 0, 'y': 1}}, inplace=True)

print(df1.head())

plt.figure()
sns.countplot(x='education', hue='party', data=df1, palette='RdBu')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()
