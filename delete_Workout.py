import mysql.connector

def delete_workout_session(session_id):
    try:
        # Establish a database connection
        cnx = mysql.connector.connect(user='root', password='That08er',
            host='localhost', database='mycodingtempledata')

        # Create a cursor object
        cursor = cnx.cursor()

        # Check if the session ID exists
        cursor.execute("SELECT * FROM WorkoutSessions WHERE session_id = %s", (session_id,))
        existing_session = cursor.fetchone()
        if not existing_session:
            print("Error: Session ID does not exist.")
            return

        # Delete the workout session
        cursor.execute("DELETE FROM WorkoutSessions WHERE session_id = %s", (session_id,))

        # Commit the changes
        cnx.commit()

        print("Workout session deleted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()



delete_workout_session(123)
