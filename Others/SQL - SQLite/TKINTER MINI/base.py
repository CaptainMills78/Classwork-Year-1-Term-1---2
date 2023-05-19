import sqlite3
from tkinter import *
from tkinter import messagebox
import Modules.myValidation

def create_table():
    try:
        conn = sqlite3.connect("db_registered.db")
        conn.execute("""CREATE TABLE IF NOT EXISTS REGISTERED
        (userID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        DOB TEXT NOT NULL,
        address TEXT NOT NULL);""")
        conn.close()
        return True
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return False

def createBase():
    window = Tk()
    window.title("Enter Data...")
    window.geometry("400x200")
    lb_title = Label(window, text="Data Entry Form")
    lb_title.grid(row=0, column=0, columnspan=5)
    lb_name = Label(window, text="Name: ")
    lb_name.grid(row=1, column=0)
    ntry_name = Entry(window)
    ntry_name.grid(row=1, column=2, columnspan=3)

    lb_email = Label(window, text="Email: ")
    lb_email.grid(row=2, column=0)
    ntry_email = Entry(window)
    ntry_email.grid(row=2, column=2, columnspan=3)

    lb_DOB = Label(window, text="Date of Birth: ")
    lb_DOB.grid(row=3, column=0)
    ntry_DOB = Entry(window)
    ntry_DOB.grid(row=3, column=2, columnspan=3)

    lb_address = Label(window, text="Address: ")
    lb_address.grid(row=4, column=0)
    ntry_address = Entry(window)
    ntry_address.grid(row=4, column=2, columnspan=3)

    btn_exit = Button(window, text="Exit", command=quit)
    btn_exit.grid(row=6, column=0)

    btn_save = Button(window, text="Save", command=lambda: saveData(ntry_name.get(), ntry_email.get(), ntry_DOB.get(), ntry_address.get()))
    btn_save.grid(row=6, column=4)

    btn_view = Button(window, text="View", command=lambda: viewAll())
    btn_view.grid(row=6, column=2)

    btn_gotologin = Button(window, text="Login", command=lambda: login())
    btn_gotologin.grid(row=7, column=2)

    window.mainloop()

def login():
    pass

def saveData(name, email, DOB, postcode):
    if not Modules.myValidation.isValidString(name):
        messagebox.showerror("Error", "Name not valid")
        return False
    if not Modules.myValidation.isValidEmail(email):
        messagebox.showerror("Error", "Email not valid")
        return False
    if not Modules.myValidation.isValidDate(DOB):
        messagebox.showerror("Error", "Date not valid")
        return False
    if not Modules.myValidation.isValidPostCode(postcode):
        messagebox.showerror("Error", "Postcode not valid")
        return False
    try:
        conn = sqlite3.connect("db_registered.db")
        conn.execute("""insert into REGISTERED (name, email, DOB, address) values (?,?,?,?)""", (name, email, DOB, postcode))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data successfully inserted")
        return True
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return False

def viewAll():
    try:
        text_to_show = ""
        conn = sqlite3.connect("db_registered.db")
        cursor = conn.execute("""SELECT * FROM REGISTERED""")
        for x in cursor:
            text_to_show += f"""Name: {x[1]}, Email: {x[2]}, DOB: {x[3]}, Address: {x[4]}, \n"""
        conn.close()
        messagebox.showinfo("Success", text_to_show)
        return True
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return False

def updateEmail(newEmail, givenEmail):
    try:
        conn = sqlite3.connect("db_registered.db")
        conn.execute("""UPDATE REGISTERED SET email = ? WHERE email = ?""", (newEmail, givenEmail))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data successfully updated")
        return True
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return False

def deleteData(givenEmail):
    try:
        conn = sqlite3.connect("db_registered.db")
        conn.execute("""DELETE FROM REGISTERED WHERE email = ?""", (givenEmail,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data successfully deleted")
        return True
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return False



if __name__ == "__main__":
    create_table()
    createBase()
    deleteData("")

