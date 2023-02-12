# Embedding Graphs into Tkinter
from matplotlib.figure import Figure    # Imports needed
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *


def plot():
    fig = Figure(figsize = (5,5), dpi=100)    # Creating Figure
    # setting the x - coordinates
    x = [0, 2, 6,10, 100]
    # setting the corresponding y - coordinates
    y = [0, 3, 9, 13.5, 45]

    # Creating the plot
    plot1 = fig.add_subplot(111)
    plot1.plot(x, y)   # Creating the plot
    C = FigureCanvasTkAgg(fig, master= window) # Creating canvas to put it on
    C.draw()
    C.get_tk_widget().pack()   # Putting the canvas onto the window
    toolbar = NavigationToolbar2Tk(C, window)
    toolbar.update()


window = Tk()    # Creating the window
window.title("Plotting in tkinter")
window.geometry("500x500")

plot_button = Button(window, height=2, width=10, text="plot", command=plot)    # Creating the plot button
plot_button.pack()

window.mainloop()
