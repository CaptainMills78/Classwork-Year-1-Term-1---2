def opAND(a, b):
    c = a & b
    return c

def opOR(a, b):
    c = a | b
    return c

def opXOR(a, b):
    c = a ^ b
    return c

def opOneComp(a):
    b = ~a
    return b

def opLeft(a, num):
    b = a << int(num)
    return b

def opRight(a, num):
    b = a >> int(num)
    return b


if __name__ == "__main__":
    print(opAND(12, 25))
    print(opOR(12, 25))
    print(opOneComp(12))
    print(opOneComp(25))
    print(opAND(opOneComp(12), 25))
    print(opOneComp(opAND(12, 25)))
    print(opXOR(12, 25))
    print(opOR(opAND(12, 25), opOneComp(25)))
    print(opOneComp(opXOR(12, 25)))
