def menu():
    print("""
    -----------------------Welcome to the Binary Calculator-----------------------
    What would you like to do?
    1. Binary to Denary conversion...
    2. Denary to Binary conversion...
    3. Denary to Hexadecimal...
    4. Hexadecimal to Denary...
    5. Binary to Hexadecimal...
    6. Hexadecimal to Binary...
    7. Quit""")
    get = int(input("Please enter an option:"))
    if get == 7:
        return False
    else:
        check(get)
        return True


def check(mode):
    if mode == 1:
        bin_in = input("Please enter a binary number:")
        answer = bin_den(bin_in)
    elif mode == 2:
        den_in = int(input("Please enter a denary number:"))
        answer = den_bin(den_in)
    elif mode == 3:
        den_in = int(input("Please enter a denary number:"))
        answer = den_hex(den_in)
    elif mode == 4:
        hex_in = input("Please enter a hexadecimal number:").lower()
        answer = hex_den(hex_in)
    elif mode == 5:
        bin_in = input("Please enter a binary number:")
        answer = bin_hex(bin_in)
    elif mode == 6:
        hex_in = input("Please enter a hexadecimal number:")
        answer = hex_bin(hex_in)
    else:
        print("Invalid input")
        answer = "No answer"
    print("The result is: " + str(answer))


def den_bin(inp):
    binary = ""
    while inp != 0:
        check1 = inp // 2
        check2 = inp % 2
        inp = check1
        binary = str(check2) + binary
    return binary


def bin_den(inp2):
    total = 0
    for x in range(len(inp2)):
        if inp2[x] == "1":
            power = len(inp2) - (x + 1)
            total = total + 2 ** power
    return total


# def den_hex(inp3):
    #

# def hex_den(inp4):
    # Use for hexadecimal to denary

# def bin_hex(inp5):
    # Use for binary to hexadecimal

# def hex_bin(inp6):
    # Use for hexadecimal to binary

# Main code

main_loop = True
while main_loop:
    main_loop = menu()
print("Bye!")
