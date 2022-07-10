import mysql.connector

class database:
    def __init__(self, host, user,port,password) :
        self.mydb = mysql.connector.connect(
            host = "your_hostname",
            user = "root",
            port = 3306,
            password = "your_password"
        )

    def showdb(self):
        query = "show databases"
        cur = self.mydb.cursor()
        cur.execute(query)
        for index, db in  enumerate(cur):
            print(f"Database{index+1} = {db}")

    def create_db(self):
        try:
            query = "create database if not exists shyanukant"
            cur = self.mydb.cursor()
            cur.execute(query)
            print('cretaed')
        except Exception as e: 
            print(e)

    def deletedb(self):
        query = "drop database rathi"
        cur = self.mydb.cursor()
        cur.execute(query)
        print("Delete")

newdb = database()
# newdb.deletedb()
newdb.showdb()