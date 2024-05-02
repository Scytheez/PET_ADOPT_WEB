import mysql.connector

class conn:
    def __init__(self):
        self.db_conn = mysql.connector.connect(
            host='locahost',
            user='',
            password='',
            database='PET_ADOPT_SYS'
        )
        self.cursor = self.db_conn.cursor()

    