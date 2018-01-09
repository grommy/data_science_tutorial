import matplotlib.pyplot as plt
import pandas as pd

from sklearn import datasets

plt.style.use('ggplot')
iris = datasets.load_iris()

print(type(iris))
print(iris.keys())

print(type(iris.data), type(iris.target))

x = iris.data
y = iris.target

df = pd.DataFrame(x, columns=iris.feature_names)

print(df.head())

_ = pd.scatter_matrix(df, c=y, figsize=[8, 8], s=150, marker='D')
plt.show()
