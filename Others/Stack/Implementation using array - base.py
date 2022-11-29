group = ["", "", "", "", "", "", "", "", ""]
sps = 0
maxLengths = len(group)


def isEmpty():
    global group, sps, maxLengths
    if sp == 0:
        return True
    else:
        return False


def isFull():
    global group, sps, maxLengths
    if sp == maxLength:
        return True
    else:
        return False


def pushItem(item):
    global group, sps, maxLengths
    if not isFull():
        names[sp] = item
        sp += 1
    else:
        print("Error: Stack Overflow")


def popItem():
    global group, sps, maxLengths
    if not isEmpty():
        sp -= 1
    else:
        print("Error: Stack Underflow")


def main():
    global group, sps


main()