import pandas as pd


airquality = pd.read_csv('DataSets/airquality.csv')
print(airquality.info())

airquality_no_duplicates = airquality.drop_duplicates()
print(airquality_no_duplicates.info())

# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality.Ozone.mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality.Ozone.fillna(value=oz_mean)

# Print the info of airquality
print(airquality.info())
