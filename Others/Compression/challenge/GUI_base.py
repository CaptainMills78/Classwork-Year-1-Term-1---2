from tkinter import *
from tkinter import messagebox

import compOptions
import decompOptions


def createWindow():
    window = Tk()
    window.title("Welcome to the file compressor!")
    window.geometry('350x150')

    optionLabel = Label(window, text="What would you like to do?")
    optionLabel.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

    compButton = Button(window, text="Compress", width=12, command=lambda: compWindow(window))
    compButton.grid(row=2, column=1, sticky="W", padx=10, pady=10)

    decompButton = Button(window, text="Decompress", width=12, command=lambda: decompWindow(window))
    decompButton.grid(row=2, column=3, sticky="W", padx=10, pady=10)

    exitButton = Button(window, text="Close", width=12, command=quit)
    exitButton.grid(row=3, column=4, padx=10, pady=10)

    window.mainloop()


def decompWindow(w):
    w.destroy()
    window = Tk()
    window.title("Decompression options")
    instructions = Label(window, text="Please enter the name of the required file, and the method used to compress it.")
    instructions.grid(row=0, column=1, padx=10, pady=10)
    nameLabel = Label(window, text="Name of the compressed file (does not require extension):")
    nameLabel.grid(row=1, column=1, padx=10, pady=10)

    nameEntry = Entry(window, width=30)
    nameEntry.grid(row=1, column=2, padx=10, pady=10)

    comprOptions = ["zlib", "gzip", "bz2"]
    optLabel = Label(window, text="Compression method:")
    optLabel.grid(row=2, column=1, padx=10, pady=10)

    optValue = StringVar(window)
    optValue.set("Select an option")
    optMenu = OptionMenu(window, optValue, *comprOptions)
    optMenu.grid(row=2, column=2, padx=10, pady=10)

    backButton = Button(window, text="Back", command=lambda: back(window))
    backButton.grid(row=3, column=4, padx=10, pady=10)

    enterButton = Button(window, text="Enter", command=lambda: decompress(nameEntry, optValue, window))
    enterButton.grid(row=3, column=3, padx=10, pady=10)
    window.mainloop()


def decompress(name, option, w):
    fileName = name.get()
    fileText = b""
    if option.get() == "Select an option":
        messagebox.showinfo(message="Fill in all fields")
        return
    try:
        file = open((fileName + ".txt"), "rb")
    except:
        messagebox.showerror(title="File not found...", message="File not found. Check the input.")
        return
    for x in file:
        fileText += x

    file.close()
    if option.get() == "zlib":
        message = decompOptions.decompZlib(fileText).decode("utf-8")
        messagebox.showinfo(title="Message is...", message=message)
        success = True
    elif option.get() == "gzip":
        message = decompOptions.decompGzip(fileText).decode("utf-8")
        messagebox.showinfo(title="Message is...", message=message)
        success = True
    elif option.get() == "bz2":
        message = decompOptions.decompBz2(fileText).decode("utf-8")
        messagebox.showinfo(title="Message is...", message=message)
        success = True
    else:
        success = False
    if success:
        name.delete(0, 'end')
        msgBox = messagebox.askquestion(title="Continue?", message="Would you like to continue?")
        if msgBox == "no":
            back(w)
    else:
        messagebox.showerror(title="Something went wrong...", message="Something went wrong while decoding the file.")
    return


def compWindow(w):
    w.destroy()
    window = Tk()
    window.title("Compression options")

    instructions = Label(window, text="Please enter the name of the resulting file, the text to be compressed, and the method of compression.")
    instructions.grid(row=0, column=1, padx=10, pady=10)
    nameLabel = Label(window, text="Name of the compressed file:")
    nameLabel.grid(row=1, column=1, padx=10, pady=10)

    nameEntry = Entry(window, width=30)
    nameEntry.grid(row=1, column=2, padx=10, pady=10)

    textLabel = Label(window, text="Text to be compressed:")
    textLabel.grid(row=2, column=1, padx=10, pady=10)

    textEntry = Entry(window, width=30)
    textEntry.grid(row=2, column=2, padx=10, pady=10)

    comprOptions = ["zlib", "gzip", "bz2"]
    optLabel = Label(window, text="Compression method:")
    optLabel.grid(row=3, column=1, padx=10, pady=10)

    optValue = StringVar(window)
    optValue.set("Select an option")
    optMenu = OptionMenu(window, optValue, *comprOptions)
    optMenu.grid(row=3, column=2, padx=10, pady=10)

    backButton = Button(window, text="Back", command=lambda: back(window))
    backButton.grid(row=4, column=4, padx=10, pady=10)

    enterButton = Button(window, text="Enter", command=lambda: compress(nameEntry, textEntry, optValue, window))
    enterButton.grid(row=4, column=3, padx=10, pady=10)
    window.mainloop()


def compress(name, text, method, w):
    fileName = str(name.get())
    textToComp = str(text.get())
    methodToUse = str(method.get())
    if fileName is None or textToComp is None or methodToUse == "Select an option":
        messagebox.showinfo(title="Field Unfilled", message="There is a field left blank, please fill in all fields.")
        success = False
    elif method.get() == "zlib":
        fileText = compOptions.compZlib(textToComp)
        print(fileText)
        file = open((fileName + ".txt"), "wb")
        file.write(fileText)
        file.close()
        success = True
    elif method.get() == "gzip":
        fileText = compOptions.compGzip(textToComp)
        print(fileText)
        file = open((fileName + ".txt"), "wb")
        file.write(fileText)
        file.close()
        success = True
    elif method.get() == "bz2":
        fileText = compOptions.compBz2(textToComp)
        print(fileText)
        file = open((fileName + ".txt"), "wb")
        file.write(fileText)
        file.close()
        success = True
    else:
        messagebox.showinfo(title="Field Unfilled", message="Unknown error")
        success = False
    if success:
        messagebox.showinfo(title="Success!", message="Compressed file successfully stored.")
        clear(name, text)
    msgBox = messagebox.askquestion(title="continue...", message="Do you want to continue?")
    if msgBox == "no":
        back(w)
    return


def clear(e1, e2):
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.focus()
    return


def back(w):
    w.destroy()
    createWindow()


createWindow()
