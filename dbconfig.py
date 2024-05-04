import mysql.connector

class conn:
    def __init__(self):
        try:
            self.db_conn = mysql.connector.connect(
                host='localhost',
                user='ubunts',
                password='Changeme#123',
                database='PET_ADOPT_SYS'
            )
            print('success')
        except Exception as e:
            print('Error: ', e)

        self.cursor = self.db_conn.cursor()

    def adopt_form(self):
        pass

    def rehome_form(self):
        pass

if __name__ == '__main__':
    conn()