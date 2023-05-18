import sqlite3

class database():
    def __init__(self, filename="db_default_name"):    # Sets filename when database first created
        self.filename = filename+".db"

    def createTable(self):
        try:
            conn = sqlite3.connect(str(self.filename))

            conn.execute("""CREATE TABLE IF NOT EXISTS USERS
            (UserName   TEXT    PRIMARY KEY   NOT NULL,
            password    TEXT    NOT NULL);""")

            conn.close()
            return True
        except:
            return False

    def insertData(self, givenUser, givenPassword):
        try:
            conn = sqlite3.connect(str(self.filename))
            conn.execute("""insert into USERS (UserName, password) values (?, ?)""",
                         (givenUser, givenPassword))
            conn.commit()
            conn.close()
            return True
        except:
            return False

    def showAllRecords(self):
        try:
            conn = sqlite3.connect(str(self.filename))
            cursor = conn.execute("""SELECT UserName, password FROM USERS""")
            for row in cursor:
                print("User Name = ", row[0])
                print("Passwords = ", row[1], "\n")
            return True
        except:
            return False

    def deleteRecord(self, givenuser):
        try:
            conn = sqlite3.connect(str(self.filename))
            conn.execute("DELETE FROM USERS WHERE UserName = ?", (givenuser,))
            print("Deleted")
            conn.commit()
            conn.close()
            return True
        except:
            return False

    def updatePassword(self, givenUser, givenPassword):
        try:
            conn = sqlite3.connect(str(self.filename))
            conn.execute("""UPDATE USERS  SET password = ? WHERE UserName = ?""", (givenPassword, givenUser))
            conn.commit()
            conn.close()
            return True
        except:
            return False


db1 = database("test_accounts")

db1.insertData("A30265", "Sfc309879")
db1.showAllRecords()
db1.deleteRecord("A30255")
db1.updatePassword("A30265", "securePassword")


