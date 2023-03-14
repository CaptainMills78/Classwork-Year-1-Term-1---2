def menu():
    grids = ""
    stop = False
    while stop == False:
        mode = input("""
        ---------------WELCOME-----------------------
        Please choose an option:
        1. Create grids (Type C)
        2. Encrypt (Type E)
        3. Decrypt (Type D)
        4. Quit (Type Q)""").upper()
        if mode == "C" or mode == 1:
            grids = create_grid()
        elif mode == "E" or mode == 2:
            if grids == "":
                print("You have not set up any grids, we will do that now...")
                grids = create_grid()

            to_encrypt = (input("Please enter a word to encrypt:")).lower()
            if len(to_encrypt) % 2 == 1:
                to_encrypt += "x"
            encrypted = encrypt(to_encrypt, grids)
            print("The result is: " + str(encrypted))
        elif mode == "Q":
            stop = True
        elif mode == "D":
            if grids == "":
                print("You have not set up any grids, we will do that now...")
                grids = create_grid()

            to_decrypt = (input("Please enter a word to decrypt:")).lower()
            decrypted = decrypt(to_decrypt, grids)
            print("The result is: "+ str(decrypted))



def encrypt(word, grid_set):
    print(word)
    grid_rows = rows(grid_set)
    result = ""
    for x in range(0, len(word), 2):
        to_add = find_pair(word[x], word[x + 1], grid_rows)
        if to_add != False:
            result += to_add
        else:
            return "Error: Result Not Calculated."
    return result


def decrypt(word, grid_set):
    word = encrypt(word, grid_set)
    if word == "Error: Result Not Calculated.":
        return word
    elif word[-1] == "x":
        word = word[:-1]
        return word


def rows(grids_sets):
    seperated = ""
    for y in range(0, len(grids_sets)):
        for x in range(0, (len(grids_sets[y]) // 5)):
            row = grids_sets[y][5 * x:5 * (x + 1)]
            seperated += row + "     "
        seperated += " "
    return seperated


def find_pair(letter1, letter2, grids):
    encoded1pos = "unset"
    encoded2pos = "unset"
    x = 0
    seperate_grids = grids.split("      ")
    while encoded1pos == "unset" and x < len(seperate_grids[0]):
        if seperate_grids[0][x] == letter1:
            encoded1pos = x
        x += 1
    x = 0
    while encoded2pos == "unset" and x < len(seperate_grids[1]):
        if seperate_grids[1][x] == letter2:
            encoded2pos = x
        x += 1
    if encoded2pos == "unset" or encoded2pos == "unset":
        print("Error with encryption")
        return False
    else:
        if abs(encoded2pos - encoded1pos) > 5:
            row_diff = (encoded2pos - encoded1pos) // 5
            encoded3pos = encoded1pos + 5+(5 * row_diff)
            encoded4pos = encoded2pos - ((5 * row_diff) + 5)
        else:
            if seperate_grids[0][encoded1pos + 1] == " ":
                encoded3pos = encoded1pos + 6
            else:
                encoded3pos = encoded1pos + 1
            if seperate_grids[1][encoded2pos + 1] == " ":
                encoded4pos = encoded2pos + 6
            else:
                encoded4pos = encoded2pos + 1
        return seperate_grids[0][encoded3pos] + seperate_grids[1][encoded4pos]


def secret1(word):
    word = word + "abcdefghijklmnoprstuvwxyz"
    grid1 = ""
    for x in range(len(word)):
        if word[x] not in grid1:
            grid1 = grid1 + word[x]
    return grid1


def secret2(word):
    word = word + "abcdefghikjlmnoprstuvwxyz"
    grid2 = ""
    reverse = ""
    for x in range(len(word)):
        if word[x] not in reverse:
            reverse = reverse + word[x]
    for x in range(1, len(reverse) + 1):
        grid2 = grid2 + reverse[-1 * x]
    return grid2


def prin_grid(grid):
    for x in range(0, (len(grid) // 5)):
        print(grid[5 * x:5 * (x + 1)])
    return


def create_grid():
    grid1st = secret1(input("Please enter the first secret word:").lower())
    grid2nd = secret2(input("Please enter the 2nd word").lower())
    print("")
    prin_grid(grid1st)
    print("")
    prin_grid(grid2nd)
    grids = [grid1st, grid2nd]
    return grids


# Main code

menu()
