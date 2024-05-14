import mysql.connector

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        # Establish a database connection
        cnx = mysql.connector.connect(user='root', password='That08er',
                                      host='localhost', database='MyCodingTempleData')

        # Create a cursor object
        cursor = cnx.cursor()

        # Check if the member exists
        cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
        existing_member = cursor.fetchone()
        if not existing_member:
            print("Error: Member ID does not exist.")
            return

        # Insert the new workout session into the database
        cursor.execute("INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)",
                       (member_id, date, duration_minutes, calories_burned))

        # Commit the changes
        cnx.commit()

        print("Workout session added successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()



add_workout_session(1, '2024-05-14', 60, 300)
