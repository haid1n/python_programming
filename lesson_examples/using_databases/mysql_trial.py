import os

import mysql.connector

# Establish the connection
try:
    connection = mysql.connector.connect(
        host="localhost",       # Replace with your MySQL server address
        user="root",   # Replace with your MySQL username
        password="@n1m34l1f3", # Replace with your MySQL password
        database="py_db_schema",  # Replace with your database name
    )

    if connection.is_connected():
        print("Successfully connected to the database!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")
