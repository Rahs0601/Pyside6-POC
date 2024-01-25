import sqlite3
import pandas as pd

# Connect to the SQLite database
db_path = "DB\DB_Sqlite_Raw_String.db"  # Replace with your SQLite database file path
conn = sqlite3.connect(db_path)

query = 'SELECT * FROM TPM_Production_String'

# Read data from SQLite database into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Store the DataFrame into a CSV file (replace 'output_file.csv' with your desired file name)
csv_file_path = 'productionData.csv'
df.to_csv(csv_file_path, index=False)

print(f'Data has been successfully exported to {csv_file_path}')
