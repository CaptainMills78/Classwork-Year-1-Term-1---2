import sqlite3

def create_db():
    conn = sqlite3.connect("test.db")
    conn.close()

def create_table():
    conn = sqlite3.connect("test.db")
    conn.execute("""CREATE TABLE COMPANY
    (staffID INT PRIMARY KEY    NOT NULL,
    name   TEXT NOT NULL,
    room   INT  NOT NULL,
    address CHAR(50),
    salary  REAL);""")
    print("Table created")
    conn.close()


create_table()