import mysql.connector
from mysql.connector import errorcode

def add_member(id, name, age, trainer_id):
    try:
        # Establish a database connection
        cnx = mysql.connector.connect(user='root', password='That08er',
                                      host='localhost', database='mycodingtempledata')

        # Create a cursor object
        with cnx.cursor() as cursor:
            # Check if the member ID already exists
            cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
            existing_member = cursor.fetchone()
            if existing_member:
                print("Error: Member ID already exists.")
                return

            # Insert the new member into the database
            cursor.execute("INSERT INTO Members (id, name, age, trainer_id) VALUES (%s, %s, %s, %s)",
                           (id, name, age, trainer_id))

            # Commit the changes
            cnx.commit()

            print("Member added successfully.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied, check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # Ensure the connection is closed
        if cnx.is_connected():
            cnx.close()


add_member(1, "John Doe", 25,1)
