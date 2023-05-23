import sqlite3


def create_table():
    db = "./students.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    cmd = "CREATE TABLE IF Not EXISTS students (Name TEXT, Age INT)"
    c.execute(cmd)
    data = [("Robert", 10), ("Sally", 15), ("Matthew", 7)]
    c.executemany("INSERT INTO students VALUES (?, ?)", data)
    conn.commit()
    print("Students table created and 3 records added")


def view_all():
    db = "./students.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    cmd = "SELECT * FROM students"
    c.execute(cmd)
    allResults = c.fetchall()
    print(allResults)
    conn.close()


def show_single_record():
    db = "./students.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    varname = input("Please enter a name:")
    cmd = "SELECT * FROM students WHERE Name = ?"
    c.execute(cmd, (varname,))
    allResults = c.fetchall()
    print(allResults)
    conn.close()
    conn.close()


if __name__ == "__main__":
    view_all()
    show_single_record()
    show_single_record()
