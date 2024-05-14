import mysql.connector

def count_members_per_trainer():
    try:
        # Establish a database connection
        cnx = mysql.connector.connect(user='root', password='That08er',
                                      host='localhost', database='MyCodingTempleData')

        # Create a cursor object
        cursor = cnx.cursor()

        # Execute SQL query using COUNT and GROUP BY
        cursor.execute("SELECT trainer_id, COUNT(*) FROM Members GROUP BY trainer_id")

        # Fetch and print results
        trainer_member_counts = {row[0]: row[1] for row in cursor.fetchall()}
        print("Members per Trainer:", trainer_member_counts)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()

count_members_per_trainer()
