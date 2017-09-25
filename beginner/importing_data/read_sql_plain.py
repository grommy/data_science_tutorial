# Import necessary module
import pandas as pd
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///../DataSets/Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)

with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()
    
# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())
