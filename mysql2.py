# mysql database
import mysql.connector as connector

# we can try access the database when making the connection
class database:
    def __init__(self) :
        
        self.mydb = connector.connect(
            host = "your_hostname",
            port = 3306,
            user = "root",
            password = "your_password",
            database = "shyanukant"
            )
    
    def create_table(self, table):
        query = f"create table {table} (id int not null auto_increment primary key, name varchar(50), phone varchar(12))"
        cur = self.mydb.cursor()
        cur.execute(query)

    
    def tableForeignKey(self, table, otherTable, col1, col2, otherTablecol):
        query = f"create table {table}({col1} int, {col2} int, foreign key({col1}) references {otherTable}({otherTablecol})) "
        cur = self.mydb.cursor()
        cur.execute(query)

    def renameTable(self, table, table2):
        query = f"alter table {table} rename to {table2}"
        cur = self.mydb.cursor()
        cur.execute(query)

    def showAllTable(self):
        cur = self.mydb.cursor()
        cur.execute("show tables")
        for index, table in enumerate(cur):
            print(f" Table {index+1} : ",table)

    def insert_data(self, table, Name, Phone):
        query = f"insert into {table}(name, phone) values ('{Name}', {Phone})"
        cur = self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
      

    def showTable(self, table):
        query = f"select * from {table}"
        cur = self.mydb.cursor()
        cur.execute(query)
        # if we want to row of data use fetchall method , if want to first row, use fetchone() method
        total = cur.fetchall()
        for db in total:
            print("\nId    : ",db[0])
            print("Name  : ",db[1])
            print("Phone : ",db[2], "\n")
        
    def deleteRow(self, table, cname, value):
        query = f"delete from {table} where {cname}='{value}'"
        cur = self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()

    def updateValue(self,table,cname,value,value2):
        
        query = f"update {table} set {cname}='{value2}' where {cname}='{value}'"
        cur = self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
        

    def order(self, table, cname):
        query = f"select * from {table} order by {cname} desc"
        cur = self.mydb.cursor()
        cur.execute(query)
        for table in cur:
            print(table)

    def secondWord(self, table, cname, cname2, word):
        query = f"select {cname} from {table} where {cname2} like '_{word}%'"
        cur = self.mydb.cursor()
        cur.execute(query)
        for value in cur:
            print(value)

    def showLImit(self, table, limit):
        query = f"select * from {table} limit {limit}"
        cur = self.mydb.cursor()
        cur.execute(query)
        for value in cur:
            print(value)

    def showLimitOffset(self, table, limit, off):
        query = f"select * from {table} limit {limit} offset {off}"
        cur = self.mydb.cursor()
        cur.execute(query)
        for value in cur:
            print(value)


    def joinTables(self, table, table2, tableCol, table2Col):
        query = f"select {table}.{tableCol}, {table2}.{table2Col} from {table} inner join {table2} on {table}.id={table2}.id"
        cur = self.mydb.cursor()
        cur.execute(query)
        for value in cur:
            print(value)

if __name__ == "__main__":
    sr = database()
    # sr.create_table('rathi')
    # sr.tableForeignKey('myfamiiy','family','id','age','id')
    # sr.renameTable('myfamiiy','myfamily')
    # sr.showAllTable()
    # sr.insert_data('myfamily',4, 22)
    # sr.deleteRow('family','name','swati')
    sr.updateValue('family','name','roshan','roshan rathi')
    # sr.showTable('family')
    # sr.order('family', 'id')
    # sr.secondWord('family','name','name','o')
    # sr.showLImit('family',2)
    # sr.showLimitOffset('family',2,3)
    # sr.joinTables('family','myfamily','name','age')