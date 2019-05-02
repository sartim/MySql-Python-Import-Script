"""
Creating MySQL connection
"""

# Interface for MySQL Database
import mysql.connector

# For connection error handling
from mysql.connector import errorcode


def connect():
    # Establish a MySQl connection
    db = None
    try:
        db = mysql.connector.connect(user='username', password='password', host='host', database='database')
        return db
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        # Close connection when an exception has occurred
        db.close()
