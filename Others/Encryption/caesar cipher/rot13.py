initial = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
               "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22,
               "X": 23, "Y": 24, "Z": 25}

def encrypt(plainText):
    cipherText = ""
    for x in plainText.upper():
        if x not in initial:
            cipherText += x
        else:
            toAdd = (initial[x]+13)%26
            for i in initial.keys():
                if initial[i] == toAdd:
                    newChar = i
                    cipherText += newChar
    return cipherText


if __name__ == "__main__":
    plain = input("Enter your plaintext")
    print(encrypt(plain))
    print("Decrypted = "+encrypt(encrypt(plain)))
