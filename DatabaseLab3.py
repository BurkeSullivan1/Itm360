### Burke Sullivan

###Libary database - ADD,DELETE,SEARCH,UPDATE BOOK Libary

# Lab 3 Database
import mysql.connector
### Create database - connection
def create_database():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Woodmoor101()'
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS library")
    cursor.close()
    conn.close()
# Connect to database function
def db_connect():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Woodmoor101()',
        database='library'
    )
### Create tables function to create tables in SQL
def create_tables():
    commands = [
        """
        CREATE TABLE IF NOT EXISTS Bookrecord (
            Bno INT PRIMARY KEY,
            Bname VARCHAR(20),
            Auth VARCHAR(20),
            Price INT,
            Publ VARCHAR(20),
            Qty INT,
            Date_of_Purchase DATE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Member (
            Mno INT PRIMARY KEY,
            Mname VARCHAR(20),
            Date_of_Membership DATE,
            Addr VARCHAR(24),
            Mob VARCHAR(10)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Issue (
            Bno INT,
            Mno INT,
            d_o_issue DATE,
            d_o_ret DATE,
            FOREIGN KEY (Bno) REFERENCES Bookrecord(Bno),
            FOREIGN KEY (Mno) REFERENCES Member(Mno)
        );
        """
    ]

    try:
        conn = db_connect()
        cursor = conn.cursor()

        for command in commands:
            cursor.execute(command)

        conn.commit()
        print("Tables created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        conn.close()

## ADD Book function
def addBook():
    try:
        conn = db_connect()
        cursor = conn.cursor()

        print("Enter book details:")
        bno = int(input("Book Number (Bno): "))
        bname = input("Book Name (bname): ")
        auth = input("Author (Auth): ")
        price = int(input("Price: "))
        publ = input("Publisher (Publ): ")
        qty = int(input("Quantity (Qty): "))
        date_of_purchase = input("Date of Purchase (YYYY-MM-DD): ")
        # Insert info in libary - %S - using paramertized queries
        query = """INSERT INTO Bookrecord (Bno, bname, Auth, Price, Publ, Qty, Date_of_Purchase)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (bno, bname, auth, price, publ, qty, date_of_purchase))
        conn.commit()
        print("Book added successfully.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()
#### Delete book function
def deleteBook():
    try:
        conn = db_connect()
        cursor = conn.cursor()

        bno = int(input("Enter Book Number to delete: "))  # Convert input to int
        query = "DELETE FROM Bookrecord WHERE Bno = %s"
        cursor.execute(query, (bno,))
        conn.commit()

        if cursor.rowcount > 0:
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()

### Search book function
def searchBook():
    # catch and handle errors
    try:
        # Assign variable to database connection
        conn = db_connect()
        cursor = conn.cursor()

        bno = input("Enter Book Number to search: ")
        query = "SELECT * FROM Bookrecord WHERE Bno = %s"
        cursor.execute(query, (bno,))
        book = cursor.fetchone()

        if book:
            print("Book Details:", book)
        else:
            print("Book not found.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()
# Update book function
def updateBook():
    # Catch and handle errors
    try:
        # assign db_connect() object to variable
        conn = db_connect()
        cursor = conn.cursor()
        # Enter details to update
        bno = int(input("Enter Book Number (Bno) to update: "))
        print("Enter new details:")
        bname = input("Book Name (bname): ")
        auth = input("Author (Auth): ")
        price = int(input("Price: "))
        publ = input("Publisher (Publ): ")
        qty = int(input("Quantity (Qty): "))
        date_of_purchase = input("Date of Purchase (YYYY-MM-DD): ")
        #Update function - updates table in book record
        query = """UPDATE Bookrecord
                       SET bname = %s, Auth = %s, Price = %s, Publ = %s, Qty = %s, Date_of_Purchase = %s
                       WHERE Bno = %s"""
        cursor.execute(query, (bname, auth, price, publ, qty, date_of_purchase, bno))
        conn.commit()
        # rowcount function in cursor counts if any rows were changed
        if cursor.rowcount > 0:
            print("Book updated successfully.")
        else:
            print("Book not found.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()

### ERROR handling with table errors
def drop_tables():
    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS Issue;")
        cursor.execute("DROP TABLE IF EXISTS Member;")
        cursor.execute("DROP TABLE IF EXISTS Bookrecord;")
        print("Tables dropped successfully.")
    except Exception as e:
        print(f"An error occurred while dropping tables: {e}")
    finally:
        conn.close()

#### RUNNING PROGRAM
if __name__ == "__main__":
    #Initialize the database and tables
    create_database()
    drop_tables()
    create_tables()

    #menu for user actions
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            addBook()
        elif choice == '2':
            deleteBook()
        elif choice == '3':
            searchBook()
        elif choice == '4':
            updateBook()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
