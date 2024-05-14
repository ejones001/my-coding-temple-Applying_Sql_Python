import mysql.connector

def add_member(id, name, age, trainer_id):
    try:
        # Establish a database connection
        cnx = mysql.connector.connect(user='ejones001', password='That08er',
                                      host='SASKE', database='MyCodingTempleData')

        # Create a cursor object
        cursor = cnx.cursor()

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
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()


add_member(1, "John Doe", 25, 101)
