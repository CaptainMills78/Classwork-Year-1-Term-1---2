names = ["", "", "", "", "", "", "", "", ""]
sp = 0
maxLength = len(names)


def isEmpty():
    global names, sp, maxLength
    if sp == 0:
        return True
    else:
        return False


def isFull():
    global names, sp, maxLength
    if sp == maxLength:
        return True
    else:
        return False


def pushItem(item):
    global names, sp, maxLength
    if not isFull():
        names[sp] = item
        sp += 1
    else:
        print("Error: Stack Overflow")


def popItem():
    global names, sp, maxLength
    if not isEmpty():
        sp -= 1
    else:
        print("Error: Stack Underflow")


def main():
    global names, sp


main()