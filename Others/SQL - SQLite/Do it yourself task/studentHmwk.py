import sqlite3
import Modules.myValidation


def create_table():
    try:
        conn = sqlite3.connect("db_hmwk.db")
        conn.execute("""CREATE TABLE IF NOT EXISTS HOMEWORK
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(15) NOT NULL,
        subject VARCHAR(10) NOT NULL,
        dueDate TEXT NOT NULL);""")
        conn.close()
        return True
    except Exception as e:
        print(e)
        print("Table not made")
        return False


def insertData(title, subject, due):
    if not Modules.myValidation.isValidLength(title, 15, 2):
        print("Title too long, ensure it is less than 15 characters.")
        return False
    if not Modules.myValidation.isValidLength(subject, 10, 2):
        print("Subject name too long...")
        return False
    if not Modules.myValidation.isValidDate(due):
        print("Date not valid...")
        return False
    try:
        conn = sqlite3.connect("db_hmwk.db")
        conn.execute("""insert into HOMEWORK (title, subject, dueDate) values (?,?,?)""", (title, subject, due))
        conn.commit()
        conn.close()
        print("Data successfully inserted")
        return True

    except Exception as e:
        print("Error in inserting the data...")
        print(e)
        return False

def viewAll():
    try:
        conn = sqlite3.connect("db_hmwk.db")
        cursor = conn.execute("""SELECT * FROM HOMEWORK""")
        for x in cursor:
            print(f"""Title: {x[1]} 
            Subject: {x[2]}
            Due Date: {x[3]}""")
        conn.close()
        return True
    except Exception as e:
        print("Error in viewing the data...")
        print(e)
        return False

def searchSpecific(date):
    if not Modules.myValidation.isValidDate(date):
        print("Date not valid...")
        return False
    try:
        conn = sqlite3.connect("db_hmwk.db")
        cursor = conn.execute("""SELECT * FROM HOMEWORK WHERE dueDate = ?""", (date,))
        for x in cursor:
            print(f"""Title: {x[1]} 
            Subject: {x[2]}
            Due Date: {x[3]}""")
        conn.close()
        return True
    except Exception as e:
        print("Error in viewing the data...")
        print(e)
        return False

if __name__ == "__main__":
    create_table()
    insertData("Comp", "Sci", "07/11/2035")
    insertData("NormalTitle", "Comp", "05/12/2035")
    insertData("LongerTitle", "Comp", "05/12/2035")
    insertData("NormalTitle", "LongerSubject", "05/12/2035")
    viewAll()
    searchSpecific("07/11/2035")
