def q1():
    a1 = input("IR active? y/n").lower()
    b1 = input("Door magnet active? y/n").lower()
    if a1 == "y" or b1 == "y":
        print("Alarm on")
    else:
        print("Alarm off")


def q2():
    a2 = input("Active? y/n").lower()
    b2 = input("Active? y/n").lower()
    if a2 == "y" and b2 == "n":
        print("On")
    else:
        print("Off")


def q3():
    a3 = input("Active? y/n").lower()
    b3 = input("Active? y/n").lower()
    c3 = input("Active? y/n").lower()
    if (a3 == "y" or b3 == "y") and c3 == "n":
        print(True)
    else:
        print(False)


#q1()
q2()
q3()

