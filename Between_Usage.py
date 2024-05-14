import mysql.connector

def get_members_in_age_range(start_age, end_age):
    try:
        # Establish a database connection
        cnx = mysql.connector.connect(user='ejones001', password='That08er',
                                      host='SASKE', database='MyCodingTempleData')

        # Create a cursor object
        cursor = cnx.cursor()

        # Execute SQL query using BETWEEN
        cursor.execute("SELECT name, age, trainer_id FROM Members WHERE age BETWEEN %s AND %s",
                       (start_age, end_age))

        # Fetch and print results
        members_in_range = cursor.fetchall()
        print("Members in Age Range:")
        for member in members_in_range:
            print(f"Name: {member[0]}, Age: {member[1]}, Trainer ID: {member[2]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()



get_members_in_age_range(25, 30)
