import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Joranx'
        )

        if connection.is_connected():
            try:
                cursor = connection.cursor()
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Error while creating database: {e}")
            finally:
                cursor.close()
                connection.close()
                print("MySQL connection closed.")
        else:
            print("Failed to connect to MySQL server.")

    except Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_database()
