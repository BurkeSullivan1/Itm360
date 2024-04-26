import mysql.connector
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

def db_connect():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Woodmoor101()',
        database='library'
    )

class User(UserMixin):
    def __init__(self, mno, password_hash=None):
        self.mno = mno
        self.password_hash = password_hash

    @staticmethod
    def get(user_id):
        conn = None  # Initialize conn to None
        try:
            conn = db_connect()
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT Mno, Password FROM member WHERE Mno = %s", (user_id,))
                result = cursor.fetchone()
                if result:
                    print(f"Retrieved Mno: {result['Mno']}, Password: {result['Password']}")  # Print retrieved values
                    return User(mno=result['Mno'], password_hash=result['Password'])
        except mysql.connector.Error as err:
            print(f"Database error during get: {err}")
        finally:
            if conn is not None:  # Check if conn is not None before attempting to close
                conn.close()
        return None

    def get_id(self):
        return str(self.mno)

    @staticmethod
    def authenticate(mno, password):
        user = User.get(mno)
        if user:
            is_valid = check_password_hash(user.password_hash, password)
            if is_valid:
                return user
            else:
                print("Debug: Password check failed with stored hash")
        else:
            print(f"Debug: No user found with Mno = {mno}")
        return None


    @staticmethod
    def create(mno, password):
        conn = db_connect()
        cursor = conn.cursor()
        hashed_password = generate_password_hash(password, method='scrypt')  # Specify the method as 'scrypt'
        print(f"Hash being stored for new user: {hashed_password}")  # Debug print
        try:
            cursor.execute("INSERT INTO member (Mno, Password) VALUES (%s, %s)", (mno, hashed_password))
            conn.commit()
            return User(mno=mno, password_hash=hashed_password)
        except mysql.connector.Error as err:
            print("Failed to insert member: {}".format(err))
        finally:
            cursor.close()
            conn.close()
        return None


