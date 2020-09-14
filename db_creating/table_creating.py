from db_creating.connection import cursor
from mysql.connector import Error


try:
    cursor.execute("CREATE TABLE IF NOT EXISTS course(id int(255) PRIMARY KEY AUTO_INCREMENT,"
                   "name char(255) NOT NULL , "
                   "buy char(255) NOT NULL, "
                   "sell char(255) NOT NULL, "
                   "date datetime NOT NULL )")
    print("[OK] Table created successful.")
except Error:
    print(f"[X] Error while creating table. {Error}")
