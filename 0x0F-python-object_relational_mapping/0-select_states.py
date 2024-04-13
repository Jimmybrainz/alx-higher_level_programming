#!/usr/bin/python3

import MySQLdb
import sys


def list_states(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve the states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the database connection
    db.close()


# Check if the script is being run directly
if __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(sys.argv) == 4:
        # Extract the arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Call the function to list the states
        list_states(username, password, database)
