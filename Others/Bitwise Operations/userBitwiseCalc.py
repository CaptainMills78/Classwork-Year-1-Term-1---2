import bitwiseOperations as bitOp



def menu():
    stop = False
    while not stop:
        print("""
        Welcome to the bitwise calculator:
        
        Please Select an Option:
        1. AND
        2. OR
        3. XOR
        4. One's Complement
        5. Left Shift
        6. Right Shift
        7. Quit""")
        choice = int(input("Please select an Option:"))
        if 1 <= choice <= 7:
            match choice:
                case 1:
                    a = int(input("Please enter a number to perform the operation on:"))
                    b = int(input("And now a second:"))
                    result = bitOp.opAND(a, b)
                    print(result)
                case 2:
                    a = int(input("Please enter a number to perform the operation on:"))
                    b = int(input("And now a second:"))
                    result = bitOp.opOR(a, b)
                    print(result)
                case 3:
                    a = int(input("Please enter a number to perform the operation on:"))
                    b = int(input("And now a second:"))
                    result = bitOp.opXOR(a, b)
                    print(result)
                case 4:
                    a = int(input("Please enter a number to perform the operation on:"))
                    result = bitOp.opOneComp(a)
                    print(result)
                case 5:
                    a = int(input("Please enter a number to perform the operation on:"))
                    num = int(input("How many places will the number be shifted by?"))
                    result = bitOp.opLeft(a, num)
                    print(result)
                case 6:
                    a = int(input("Please enter a number to perform the operation on:"))
                    num = int(input("How many places will the number be shifted by?"))
                    result = bitOp.opRight(a, num)
                    print(result)
                case _:
                    stop = True


if __name__ == "__main__":
    menu()