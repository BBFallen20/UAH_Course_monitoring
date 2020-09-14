from mysql.connector import Error
from db_creating.connection import cursor
import parse.requesting
import datetime


class Controller:
    def __init__(self):
        self.control = cursor
        self.data = parse.requesting.Requester().get_page()
    
    def table_inserting(self):
        sql = "INSERT INTO course(name, buy, sell, date) VALUES (%s, %s, %s, %s)"
        for i in range(len(self.data)):
            val = (self.data[i]['title'], self.data[i]['buy'], self.data[i]['sell'], datetime.datetime.now())
            try:
                self.control.execute(sql, val)
            except Error:
                print(f"[X] Error with inserting to table. {Error}")
                return 0
        print("[OK] Data inserted.")


Controller().table_inserting()
