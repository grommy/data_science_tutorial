import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


path = "../DataSets/house-votes-84.csv"
columns = ['party', 'infants', 'water', 'budget', 'physician', 'salvador',
           'religious', 'satellite', 'aid', 'missile', 'immigration', 'synfuels',
           'education', 'superfund', 'crime', 'duty_free_exports', 'eaa_rsa']
df = pd.read_csv(path, header=None, names=columns, na_values='?')

# df1 = df.filter(items=['party', 'education', 'satellite', 'missile'])
# df1 = df1.dropna()
# df1.replace({'n': 0, 'y': 1}, inplace=True)
df = df.dropna()
df.replace({'n': 0, 'y': 1}, inplace=True)
print(df.head())


# Make exploratory analysis
plt.figure()
sns.countplot(x='education', hue='party', data=df, palette='RdBu')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()

# plt.figure()
# sns.countplot(x='satellite', hue='party', data=df1, palette='RdBu')
# plt.xticks([0, 1], ['No', 'Yes'])
# plt.show()
#
# plt.figure()
# sns.countplot(x='missile', hue='party', data=df1, palette='RdBu')
# plt.xticks([0, 1], ['No', 'Yes'])
# plt.show()


# Fit Model
# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X, y)

X_new_data = {0: {0: 0.58433993246353499},
 1: {0: 0.92579886214384999},
 2: {0: 0.48661677606418097},
 3: {0: 0.40741366101272314},
 4: {0: 0.71455285087565568},
 5: {0: 0.16648805988816751},
 6: {0: 0.92534119005907489},
 7: {0: 0.55470393849124511},
 8: {0: 0.28867341901724786},
 9: {0: 0.94474486918850853},
 10: {0: 0.19124395314857445},
 11: {0: 0.60013882585083844},
 12: {0: 0.96959091923754737},
 13: {0: 0.45830981214670918},
 14: {0: 0.8026848369967865},
 15: {0: 0.17221445348856035}}

X_new = pd.DataFrame.from_dict(X_new_data)
print(X_new.head())

new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))
