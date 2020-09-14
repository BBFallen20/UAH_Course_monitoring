import mysql.connector
from mysql.connector import Error


try:
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='parsing_db',
        autocommit=True
    )
    print("[OK] Database connection successful.")
except Error:
    print("[X] Database connection failed.")
    database = None

cursor = database.cursor()



