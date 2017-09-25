# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///../DataSets/Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("Select * from Album", engine)

# Print head of DataFrame
print(df.head())
