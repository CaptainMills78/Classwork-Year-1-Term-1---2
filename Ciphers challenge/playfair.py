def menu():
    grids = ""
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
        else:
            



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

print("hello world")
