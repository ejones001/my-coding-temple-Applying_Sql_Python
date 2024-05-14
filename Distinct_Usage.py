import mysql.connector

def list_distinct_trainers():
    try:
        # Establish a database connection
        cnx = mysql.connector.connect(user='ejones001', password='That08er',
                                      host='SASKE', database='MyCodingTempleData')

        # Create a cursor object
        cursor = cnx.cursor()

        # Execute SQL query using DISTINCT
        cursor.execute("SELECT DISTINCT trainer_id FROM Members")

        # Fetch and print results
        trainers = [row[0] for row in cursor.fetchall()]
        print("Distinct Trainers:", trainers)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()


list_distinct_trainers()
