from tkinter import *

def createGUI():
    window = Tk()
    window.title("Welcome to the BMI calculator!")
    window.geometry('800x220')
    welcomeLabel = Label(window, text="Welcome to my BMI calculator!")
    welcomeLabel.config(font=("Courier", 14))
    welcomeLabel.grid(row=0, column=1, columnspan=3, sticky="W", padx=10, pady=10)
    weightLabel = Label(window, text="Weight in KG")
    weightLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")
    heightLabel = Label(window, text="Height in Meters")
    heightLabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    helpLabel = Label(window, text="Enter height (m) and weight (kg)")
    helpLabel.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    weightEntry = Entry(window, width=30)
    weightEntry.grid(row=1, column=1, padx=10, pady=10)
    heightEntry = Entry(window, width=30)
    heightEntry.grid(row=2, column=1, padx=10, pady=10)

    exitButton = Button(window, text="Close", width=12, command=quit)
    exitButton.grid(row=0, column=4, padx=10, pady=10)

    clearButton = Button(window, text="Clear", width=12,command=lambda: clear(weightEntry, heightEntry))
    clearButton.grid(row=4, column=0, padx=10, pady=10)

    calcButton = Button(window, text = "Calculate", width = 12, command= lambda: calcBMI(window, weightEntry, heightEntry))
    calcButton.grid(row=4, column=1)
    weightEntry.focus()
    window.mainloop()


def calcBMI(f, w, h):
    h = float(h.get())
    w = float(w.get())
    bmi = w/(h**2)
    bmi = round(bmi, 2)
    result = "Your BMI is "+ str(bmi)
    messagebox.showinfo(title= "BMI Value", message= result)
    msgBox = messagebox.askquestion(title="continue...", message= "Do you want to continue?")
    if msgBox == "yes":
        f.destroy()
        createGUI()
    else:
        quit()

def clear(e1, e2):
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.focus()
    return


createGUI()