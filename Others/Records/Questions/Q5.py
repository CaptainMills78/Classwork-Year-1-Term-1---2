baseArray = [["","","",""],
             ["","","",""],
             ["","","",""],
             ["","","",""],
             ["","","",""],
             ["","","",""]
             ]


def define_grid(baseA, o_coord_x, o_coord_y):
    for y in range(len(baseA)):
        for x in range(len(baseA[y])):
            if o_coord_x-1 == x and o_coord_y-1 == y:
                baseA[y][x] = "O"
            else:
                baseA[y][x] = "x"
    return baseA


def print_grid(array):
    x = int(input("Enter an x coordinate between 1 and 4:"))
    while not 1 <= x <= 4:
        print("x not in valid range...")
        x = int(input("Enter an x coordinate between 1 and 4:"))
    y = int(input("Enter an y coordinate between 1 and 6:"))
    while not 1 <= y <= 6:
        print("y not in valid range...")
        y = int(input("Enter an x coordinate between 1 and 6:"))
    grid = define_grid(array, x, y)
    for i in grid:
        for j in i:
            print(str(j), end="  ")
        print("")


print_grid(baseArray)


