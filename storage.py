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

# Create the table if it does not exist
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

# Insert DataFrame into PostgreSQL with ON CONFLICT to handle duplicates
table_name = 'gedebie'

for index, row in data.iterrows():
    # Create an insert query with ON CONFLICT to skip duplicates
    insert_query = sql.SQL("""
        INSERT INTO {} ({}) 
        VALUES ({}) 
        ON CONFLICT ("Message ID") DO NOTHING
    """).format(
        sql.Identifier(table_name),
        sql.SQL(', ').join(map(sql.Identifier, data.columns)),
        sql.SQL(', ').join(sql.Placeholder() for _ in range(len(row)))
    )

    # Execute the query
    cursor.execute(insert_query, tuple(row))

# Commit the transaction
conn.commit()
print("Data inserted successfully.")

# Alter table to add new columns
altertable = '''
ALTER TABLE gedebie
ADD COLUMN image_name VARCHAR(255),
ADD COLUMN class_id INTEGER,
ADD COLUMN confidence FLOAT,
ADD COLUMN bbox TEXT;
'''
cursor.execute(altertable)

# Commit and close the database connection
conn.commit()
cursor.close()
conn.close()
print("Table structure updated successfully.")
