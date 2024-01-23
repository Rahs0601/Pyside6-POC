import pandas as pd
from sqlalchemy import create_engine

# Set up your MSSQL connection parameters
connection_string = r"mssql+pyodbc://sa:pctadmin$1234@WIN10-TEST\SQLEXPRESS2019/BASELINE?driver=ODBC Driver 17 for SQL Server"

# Create a SQLAlchemy engine
engine = create_engine(connection_string)

# Define your SQL query
sql_query = 'SELECT * FROM MachineInformation'

# Use pandas to read data from SQL into a DataFrame
df = pd.read_sql(sql_query, engine)

# Perform any data manipulation or analysis as needed on the DataFrame

# Save the DataFrame back to SQL (replace 'new_table' with your desired table name)
# df.to_sql(name='new_table', con=engine, index=False, if_exists='replace')
df.to_csv('MachineInformation.csv', index=False)
print(f'Data has been successfully exported to MachineInformation.csv')
# Close the SQLAlchemy engine
engine.dispose()
