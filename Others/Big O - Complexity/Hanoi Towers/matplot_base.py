import matplotlib.pyplot as plt


def plotGraph(x, y, xTitle, yTitle, gTitle):
    plt.plot(x, y)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)
    plt.title(gTitle)
    plt.show()


if __name__ == "__main__":
    x = [0, 1, 2, 3, 4]
    y = [4, 3, 2, 1, 0]
    title = "Test"
    x_title = "x"
    y_title = "y"
    plotGraph(x, y, x_title, y_title, title)
