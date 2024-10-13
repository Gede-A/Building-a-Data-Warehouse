import pandas as pd
import psycopg2
from psycopg2 import sql

# Define your connection parameters
conn_params = {
    'host': 'localhost',
    'port': '3000',  # Default port for PostgreSQL
    'user': 'postgres',  
    'password': '123456',
    'dbname': 'dbt'
}

# Establish a connection to the PostgreSQL database
try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    print("Connected to the database successfully.")
except Exception as e:
    print(f"Error while connecting to PostgreSQL: {e}")
    exit()

# Load CSV file into a DataFrame
csv_file_path = 'data/raw/scraped.csv' 
data = pd.read_csv(csv_file_path)

# Optional: Check the DataFrame
print(data.head())

create_table_query = '''
CREATE TABLE IF NOT EXISTS gedebie (
    "Message ID" BIGINT PRIMARY KEY,
    "Sender" BIGINT,
    "Date" TIMESTAMPTZ,
    "Message" TEXT
);
'''
cursor.execute(create_table_query)
conn.commit()

table_name = 'gedebie';

# Insert DataFrame to PostgreSQL
for index, row in data.iterrows():
    # Create an insert query
    insert_query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
        sql.Identifier(table_name),
        sql.SQL(', ').join(map(sql.Identifier, data.columns)),
        sql.SQL(', ').join(sql.Placeholder() * len(row))
    )

    # Execute the query
    cursor.execute(insert_query, tuple(row))

# Commit the transaction
conn.commit()
print("Data inserted successfully.")

# Close the cursor and connection
cursor.close()
conn.close()
