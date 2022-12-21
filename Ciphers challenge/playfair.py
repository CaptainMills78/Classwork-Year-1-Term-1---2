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

            to_encrypt = input("Please enter a word to encrypt:")
            if len(to_encrypt) % 2 == 1:
                to_encrypt += "x"
            encrypted = encrypt(to_encrypt, grids)
            print("The result is: " + str(encrypted))
        elif mode == "Q":
            stop = True


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
    seperate_grids = grids.split("      ")
    for x in range(0, len(seperate_grids[0])):
        if seperate_grids[0][x] == letter1:
            encoded1pos = x
    for x in range(0, len(seperate_grids[1])):
        if seperate_grids[1][x] == letter2:
            encoded2pos = x
    if encoded2pos == "unset" or encoded2pos == "unset":
        print("Error with encryption")
        return False
    else:
        if encoded2pos - encoded1pos > 5 or encoded2pos - encoded1pos < -5:
            row_diff = (encoded2pos - encoded1pos) // 5
            encoded3pos = encoded1pos + (5 * row_diff)
            encoded4pos = encoded2pos - (5 * row_diff)
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
    grid1st = secret1(input("Please enter the first secret word:"))
    grid2nd = secret2(input("Please enter the 2nd word"))
    print("")
    prin_grid(grid1st)
    print("")
    prin_grid(grid2nd)
    grids = [grid1st, grid2nd]
    return grids


# Main code

menu()
