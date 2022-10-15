def calculatePercentSlope(delta_x, delta_h):
    slope = (delta_h / delta_x)
    percentage = slope * 100
    return percentage


def detail():
    change_x = int(input("What is the overall horizontal distance travelled over the slope?"))
    change_h = int(input("What is the overall vertical distance travelled over the slope?"))
    print("The slope percent is "+str(calculatePercentSlope(change_x, change_h))+" degrees.")
    return


detail()
