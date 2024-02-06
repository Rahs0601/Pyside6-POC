import pandas as pd
from sqlalchemy import create_engine
connection_string = r"mssql+pyodbc://sa:pctadmin$1234@WIN10-TEST\SQLEXPRESS2019/BASELINE?driver=ODBC Driver 17 for SQL Server"
engine = create_engine(connection_string)
def gettable():
    # Create a SQLAlchemy engine
    sql_query = 'SELECT table_name = t.name FROM sys.tables t INNER JOIN sys.schemas s ON t.schema_id = s.schema_id'

    # Use pandas to read data from SQL into a DataFrame
    df = pd.read_sql(sql_query, engine)



    # Perform any data manipulation or analysis as needed on the DataFrame

    # Save the DataFrame back to SQL (replace 'new_table' with your desired table name)
    # df.to_sql(name='new_table', con=engine, index=False, if_exists='replace')
    df.to_csv('MachineInformation.csv', index=False)
    print(f'Data has been successfully exported to MachineInformation.csv')
    # Close the SQLAlchemy engine
    engine.dispose()
    return list(df['table_name'])

# print(gettable())


def getData(table):
    sql_query = f'SELECT * FROM {table}'
    df = pd.read_sql(sql_query, engine)
    df.to_csv(f'{table}.csv', index=False)
    print(f'Data has been successfully exported to {table}.csv')
    # Close the SQLAlchemy engine
    engine.dispose()
    return df

for table in gettable():
    print(table)
    print(getData(table))
