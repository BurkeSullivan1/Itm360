#### Data base connection file

import mysql.connector
import bcrypt # password encryption

####### Create database first ################

import mysql.connector
from mysql.connector import Error

def create_database_and_table():
    connection = None
    try:
        # Establish a connection to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Woodmoor101()'
        )
        cursor = connection.cursor()

        # Create the database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS Insurance")
        connection.commit()  # Commit the transaction to make sure the database is created

        # Ensure that we're operating in the newly created or existing database
        cursor.execute("USE Insurance")

        # Create the table if it does not exist
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            insurance_type ENUM('Whole Life', 'Term-Life') NOT NULL,
            age INT
        );
        '''
        cursor.execute(create_table_query)
        connection.commit()  # Commit the changes to ensure the table is created/checked
        print("Table 'users' checked or created successfully")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the cursor and connection properly
        if connection is not None and connection.is_connected():
            if 'cursor' in locals():
                cursor.close()  # Close the cursor before the connection
            connection.close()
            print("MySQL connection is closed")



create_database_and_table()

def get_user_details(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT id, username, password, insurance_type, age FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user_details = cursor.fetchone()
    cursor.close()
    conn.close()
    return user_details


##### Get database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Woodmoor101()",
        database="Insurance"
    )
# add info to database from signup page
def create_user(email, password, insurance_type,age):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # Database interaction logic to insert the new user
    conn = get_db_connection()
    cursor = conn.cursor()
    # insert into database
    query = "INSERT INTO users (username, password, insurance_type, age) VALUES (%s, %s, %s, %s)"
    # try - error handling -
    try:
        cursor.execute(query, (email, hashed_password, insurance_type, age))
        conn.commit()
        print("User created successfully.")
    except mysql.connector.Error as err:
        raise Exception(f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()
# check database for authentication
def check_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    # Update your query to include the age field
    query = "SELECT id, password, insurance_type, age FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user_record = cursor.fetchone()
    cursor.close()
    conn.close()
    # Return insurance type and age for logged-in user
    if user_record and bcrypt.checkpw(password.encode('utf-8'), user_record['password'].encode('utf-8')):
        # Now also return the age
        return {
            'id': user_record['id'],
            'insurance_type': user_record['insurance_type'],
            'age': user_record['age']  # Ensure age is included
        }
        return None

# update plan
def update_user_plan(user_id, new_plan):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET insurance_type = %s WHERE id = %s", (new_plan, user_id))
        conn.commit()
    except mysql.connector.Error as error:
        conn.rollback()  # rollback if any exception occurred
        print(f"Failed updating record: {error}")
    finally:
        cursor.close()
        conn.close()
