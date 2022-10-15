def calculateArchWidth(l, num):
    archWidth = l / num
    return archWidth


def detail():
    length = int(input("How long is your line of arches?"))
    arches = int(input("How many arches are there?"))
    print("The arches are "+str(calculateArchWidth(length, arches))+" metres wide.")
    return


detail()
