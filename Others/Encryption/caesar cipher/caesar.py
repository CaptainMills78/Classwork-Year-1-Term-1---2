def encrypt(plainText, placeShift):
    initial = {"A":0, "B":1, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
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
    initial = {"A": 0, "B": 1, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
               "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
               "X": 24, "Y": 25, "Z": 26}
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
