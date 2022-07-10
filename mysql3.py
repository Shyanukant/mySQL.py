from mysql2 import database

def dbApp():
    db = database()
    while True:
        
        print("*********WELCOME********")
        print("\nPress 1 for show Data")
        print("Press 2 for insert Data")
        print("Press 3 for delete Data")
        print("Press 4 for update Data")
        print("Press 5 for exit\n")

        try:
            choice = int(input())
            
            if choice == 1:
                #show table
                global table
                table = input("Enter the Table Name : ")
                db.showTable(table)

            elif choice == 2:
                #insert data into table
                table = input("Enter the table : ")
                name = input("Enter the Name : ")
                phone = input("Enter the Phone : ")
                db.insert_data(table, name, phone)
                
            elif choice == 3:
                #delete data into table
                table = input("Enter the table : ")
                cname = input("Enter the Column : ")
                value = input("Enter the value of Column : ")
                db.deleteRow(table, cname, value)

            elif choice == 4:
                #update data into table
                table = input("Enter the table : ")
                cname = input("Enter the Column Name Where You want to Change :  ")
                value = input("Enter the old value that you want to change :  ")
                value2 = input("Enter the new value that you update : ")
                db.updateValue(table, cname,value,value2)

            elif choice == 5:
                break
            else:
                print("Invalid input")
        except Exception as e:
            print(e)
            print("Invalid Details")

if __name__ == "__main__":
    dbApp()