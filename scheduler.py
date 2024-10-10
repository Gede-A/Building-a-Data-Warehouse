# storage.py
import mysql.connector

def store_to_db(df, table_name='telegram_messages'):
    connection = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database'
    )
    
    cursor = connection.cursor()
    
    for _, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (MessageID, Sender, Date, Message) 
            VALUES (%s, %s, %s, %s)
        """, (row['Message ID'], row['Sender'], row['Date'], row['Message']))
    
    connection.commit()
    connection.close()
