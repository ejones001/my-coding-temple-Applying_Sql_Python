import mysql.connector

def update_member_age(member_id, new_age):
    try:
        # Establish a database connection
        cnx = mysql.connector.connect(user='ejones001', password='That08er',
                                      host='SASKE', database='MyCodingTempleData')

        # Create a cursor object
        cursor = cnx.cursor()

        # Check if the member exists
        cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
        existing_member = cursor.fetchone()
        if not existing_member:
            print("Error: Member ID does not exist.")
            return

        # Update the age of the member
        cursor.execute("UPDATE Members SET age = %s WHERE id = %s", (new_age, member_id))

        # Commit the changes
        cnx.commit()

        print("Member age updated successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()


update_member_age(1, 30)
