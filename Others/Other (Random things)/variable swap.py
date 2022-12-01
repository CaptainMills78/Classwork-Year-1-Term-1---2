def swap1():
    a = 9
    b = 7
    temp = 0

    temp = a
    a = b
    b = temp

    print(a)
    print(b)


def swap2():
    x = 6
    y = 5

    x = x ^ y
    y = x ^ y
    x = x ^ y

    print(x, y)


swap2()