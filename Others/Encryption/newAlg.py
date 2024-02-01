import random
def shiftChar(character, shift):
    newChar = ord(character)
    if 65 <= newChar <= 90:
        newChar += shift
        if newChar > 90:
            newChar -= 26
    elif 97 <= newChar <= 122:
        newChar += shift
        if newChar > 122:
            newChar -= 26
    return chr(newChar)


def convertCaesar(plainText, key):
    cipherText = ""
    for x in plainText:
        cipherText += shiftChar(x, key)
    return cipherText

def convertVernam(plaintext):
    pad = generatePad(len(plaintext))
    print("Pad: ", pad)
    cipher = ""
    for x in range(len(plaintext)):
        if plaintext[x] != " ":
            plainChar = plaintext[x].upper()
            key = ord(pad[x].upper()) - 64
            cipher += shiftChar(plainChar, key)
        else:
            cipher += " "
    return cipher


def generatePad(length):
    pad = ""
    for x in range(length):
        charVal = random.randint(1, 26)
        pad += chr(charVal+64)
    return pad

if __name__ == "__main__":
    print(convertVernam("Hello EveryONE"))
