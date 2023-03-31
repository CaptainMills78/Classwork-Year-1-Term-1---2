def encrypt(plainText, placeShift):
    initial = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
               "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22,
               "X": 23, "Y": 24, "Z": 25}
    if placeShift < 0:
        forwards = False
        placeShift = abs(placeShift)
    else:
        forwards = True
    cipherText = ""
    for x in plainText.upper():
        if x not in initial:
            cipherText += x
        elif forwards:
            newChar = (initial[x] + placeShift)%26
            for i in initial.keys():
                if initial[i] == newChar:
                    cipherText += i
        else:
            newChar = (initial[x] - placeShift) % 26
            for i in initial.keys():
                if initial[i] == newChar:
                    cipherText += i
    return cipherText


def decrypt(cipherText, placeShift):
    initial = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
               "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22,
               "X": 23, "Y": 24, "Z": 25}
    if placeShift < 0:
        forwards = True
        placeShift = abs(placeShift)
    else:
        forwards = False
    plainText = ""
    for x in cipherText.upper():
        if x not in initial:
            plainText += x
        elif forwards:
            newChar = (initial[x] + placeShift) % 26
            for i in initial.keys():
                if initial[i] == newChar:
                    plainText += i
        else:
            newChar = (initial[x] - placeShift) % 26
            for i in initial.keys():
                if initial[i] == newChar:
                    plainText += i
    return plainText


if __name__ == "__main__":
    text = input("Enter a string to encrypt")
    places = int(input("How many places would you like to shift by?"))
    print("Encrypted: "+str(encrypt(text, places)))
    print("Decrypted back: "+str(decrypt(encrypt(text, places), places)))
