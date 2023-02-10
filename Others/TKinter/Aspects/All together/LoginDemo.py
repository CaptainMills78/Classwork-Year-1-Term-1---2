from tkinter import *
from tkinter import messagebox


def back(wx):  # Destroys current window
    wx.destroy()
    main()


def main():
    # code for the main menu
    # from this window, I can go to log in or signin or exit

    win1 = Tk()  # Creates main window and sets dimensions and title
    win1.title("Welcome")
    win1.geometry("400x180")

    titleLabel = Label(win1, text=" Welcome to TKINTER programming")  # Create title label
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    exitButton = Button(win1, text="Exit", width=12, command=quit)  # Button closes main window
    exitButton.grid(row=1, column=0, padx=10, pady=30)

    loginButton = Button(win1, text="Login", width=12, command=lambda: login(win1))  # Opens login window
    loginButton.grid(row=1, column=1, padx=10, pady=10)

    signinButton = Button(win1, text="Sign in", width=12, command=lambda: signin(
        win1))  # Opens sign in window - Passes current window into the function
    signinButton.grid(row=1, column=2, padx=10, pady=10)

    mainloop()


def login(w):
    # code to create login screen
    w.destroy()
    win2 = Tk()
    win2.title("Log in... ")
    win2.geometry("400x180")

    titleLabel = Label(win2, text="Please complete all fields")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", padx=10, pady=10)

    userLabel = Label(win2, text="User name")
    userLabel.grid(row=1, column=0, sticky="W", padx=10, pady=10)

    userField = Entry(win2, width=20)
    userField.grid(row=1, column = 1, sticky="SNEW", padx=10, pady=10)

    passLabel = Label(win2, text="Password")
    passLabel.grid(row=2, column=0, sticky="W", padx=10, pady=10)

    passField = Entry(win2, show="*", width=20)
    passField.grid(row=2, column=1, sticky="SNEW", padx=10, pady=10)

    backButton = Button(win2, text="Back", command=lambda: back(win2))  # Destroys current window and returns to main
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    enterButton = Button(win2, text="Enter", command=lambda: menu(win2, userField, passField))
    enterButton.grid(row=4, column=3, sticky="SNEW", padx=10, pady=10)
    mainloop()


def signin(w):
    w.destroy()  # Takes current window and destroys it
    win3 = Tk()  # Creates sign-in window
    win3.title("Sign in ... ")
    win3.geometry("400x180")

    titleLabel = Label(win3, text=" Please complete all fields ")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    userLabel = Label(win3, text="User name")
    userLabel.grid(row=1, column=0, sticky="W", padx=10, pady=10)

    userField = Entry(win3, width=20)
    userField.grid(row=1, column=1, sticky="SNEW", padx=10, pady=10)

    passLabel = Label(win3, text="Password")
    passLabel.grid(row=2, column=0, sticky="W", padx=10, pady=10)

    passField = Entry(win3, show="*", width=20)
    passField.grid(row=2, column=1, sticky="SNEW", padx=10, pady=10)

    passLabel2 = Label(win3, text="Re-Type Password")
    passLabel2.grid(row=3, column=0, sticky="W", padx=10, pady=10)

    passField2 = Entry(win3, show="*", width=20)
    passField2.grid(row=3, column=1, sticky="SNEW", padx=10, pady=10)

    backButton = Button(win3, text="Back", command=lambda: back(win3))  # Destroys current window and returns to main
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    enterButton = Button(win3, text="Enter", command=lambda: showSignIn(win3, userField, passField, passField2))
    enterButton.grid(row=4, column=3, sticky="SNEW", padx=10, pady=10)

    mainloop()


def menu(w, u, p):
    # code for creating the application's menu
    if check(u.get(), p.get()):
        w.destroy()
        win4 = Tk()
        win4.title("Welcome to the Menu!")
        win4.geometry("500x500")

        titleLabel = Label(win4, text="You have logged in!")
        titleLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        menubar = Menu(win4)  # Base menu
        win4.config(menu=menubar)  # Set the menu as the base

        file_menu = Menu(menubar)  # Add a file tab onto base menu
        file_menu.add_command(label="Exit", command=lambda: back(win4), )  # Add a command to tab
        menubar.add_cascade(label="File", menu=file_menu, underline=0)

        mainloop()
    else:
        msgBox = messagebox.askquestion(title="No match", message="Would you like to retry?", icon="error")
        if msgBox == "yes":
            login(w)
        else:
            back(w)
    pass


def check(uName, pWord):
    names = ""
    file = open(r"Users.txt", "r")
    for x in file:
        names += str(x)
    names = names.split(";")
    file.close()
    for x in names:
        x = x.split(", ")
        if x[0] == uName:
            if x[1] == pWord:
                return True
    return False


def checkSignIn(u, p, p2):
    if str(u) == "":
        return False
    if str(p) == str(p2):
        file = open(r"Users.txt", "a")
        file.write(str(u)+", "+str(p)+";")
        file.close()
        return True
    pass


def showSignIn(w, u, p, p2):
    if checkSignIn(u.get(), p.get(), p2.get()):
        messagebox.showinfo(title= "Sign in Successful", message="Sign in successful, try your login:")
        back(w)
    else:
        msgBox = messagebox.askquestion("Return?", message="Sign in failed, retry?")
        if msgBox == "yes":
            signin(w)
        else:
            back(w)
    return


if __name__ == "__main__":
    main()
