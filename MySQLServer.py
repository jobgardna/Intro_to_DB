import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',       # Replace with your actual username
            password='your_password'    # Replace with your actual password
        )
        if connection.is_connected():
            try:
                cursor = connection.cursor()
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except mysql.connector.Error as e:
                print(f"Database creation failed: {e}")
            finally:
                cursor.close()
                connection.close()
                print("Connection closed.")

    except mysql.connector.Error as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    create_database()
