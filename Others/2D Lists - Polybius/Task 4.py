square = [[0, 1, 2, 3, 4, 5],
          [1, "A", "B", "C", "D", "E"],
          [2, "F", "G", "H", "I", "J"],
          [3, "K", "L", "M", "N", "O"],
          [4, "P", "Q", "R", "S", "T"],
          [5, "U", "V", "W", "X", "Y"],
          [6, "Z", "?", " ", "@", "."]]


def display(square1):
    for x in range(len(square1)):
        row = ""
        for y in range(len(square1[x])):
            row += str(square1[x][y])
            row += " | "
        print(row)
        print("-----------------------")
    pass


def check(to_check):
    for x in str(to_check):
        if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ? @.":
            pass
        else:
            print("The plaintext includes unsupported characters...")
            print("Quitting...")
            import sys
            sys.exit()


def encrypt(plain, square1):
    plain = plain.upper()
    check(plain)
    crypto = ""
    for x in plain:
        for y in range(len(square1)):
            for z in range(len(square1[y])):
                if x == square1[y][z] and x == plain[-1]:
                    element = str(y) + str(z)
                    crypto += element
                elif x == square1[y][z]:
                    element = str(y) + str(z) + ", "
                    crypto += element
                else:
                    pass
    return crypto


def main():
    code = input(" Enter Message (the plaintext) ...  ")
    print("The Cryptogram is ... " + str(encrypt(code, square)))


display(square)
main()
