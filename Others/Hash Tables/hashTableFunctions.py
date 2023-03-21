def midSquare(item):
    num = int(item) ** 2
    if len(str(num)) == 1:
        digits = num
    else:
        digits = int(str(num)[(len(str(num)) // 2) - 1] + str(num)[(len(str(num)) // 2)])
    return digits


def simpleMod(item, length):
    digit = item % length
    return digit


def digitFolding():
    pass


def createHash(l, length, chaining=True):
    # Create hash table of specified length using items from list 'l'.
    # Handle collisions via chaining or linear probing (chaining by default).
    hashTable = []
    for x in range(length):
        hashTable.append("")
    for x in l:
        pos = simpleMod(midSquare(x), length)
        while hashTable[pos] != "":
            if chaining:
                pass
            else:
                pos += 1
        hashTable[pos] = x
    return hashTable



if __name__ == "__main__":
    list2 = [12, 456, 3]
    hashT = createHash(list2, 11, False)
    print(hashT)
