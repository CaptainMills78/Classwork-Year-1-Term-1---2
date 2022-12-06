import group_stack

board = [["0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0"]]
maxLength = 6
sps = [0, 0, 0, 0, 0, 0, 0]
running = True
r_counters = 0
b_counters = 0
r_name = ""
b_name = ""
last_added = 0


def get_details():
    global r_name, b_name
    r_name = str(input("Red Player: Please enter your name:"))
    b_name = str(input("Blue Player: Please enter your name:"))


def show_board():
    global board
    for y in range(6, 0, -1):
        for x in range(len(board)):
            print(board[x][y - 1], end=" ")
        print()
    return


def r_turn():
    global board, r_counters, r_name, last_added
    show_board()
    success_r = False
    while not success_r:
        r_place = str(input("Which column would you like to place a counter, " + r_name + "?"))
        if r_place.isdigit():
            r_place = int(r_place) - 1
            if group_stack.isStackValid(str(r_place), 0, 6):
                success_r = group_stack.pushItem("r", r_place, board, sps[r_place], maxLength)
        else:
            success_r = False
    r_counters += 1
    sps[r_place] += 1
    last_added = r_place
    return


def b_turn():
    global board, b_counters, b_name, last_added
    show_board()
    success_b = False
    while not success_b:
        b_place = str(input("Which column would you like to place a counter, " + b_name + "?"))
        if b_place.isdigit():
            b_place = int(b_place) - 1
            if group_stack.isStackValid(str(b_place), 0, 6):
                success_b = group_stack.pushItem("b", b_place, board, sps[b_place], maxLength)
        else:
            success_b = False
    b_counters += 1
    sps[b_place] += 1
    last_added = b_place
    return


def check_win(player):
    global board, last_added, sps
    count = 0
    for x in board[last_added]:
        if x == "0":
            pass
        elif x == player:
            count += 1
        else:
            count = 0
    if count >= 4:
        if player == "r":
            print("Red Player "+r_name+" has won!!!!")
        elif player == "b":
            print("Blue Player "+b_name+" has won!!!!")
        return True
    count = 0
    for y in range(maxLength):
        x = board[y][sps[last_added]-1]
        if x == "0":
            pass
        elif x == player:
            count += 1
        else:
            count = 0
    if count >= 4:
        if player == "r":
            print("Red Player "+r_name+" has won!!!!")
        elif player == "b":
            print("Blue Player "+b_name+" has won!!!!")
        return True
    return False


def rungame():
    global board, r_counters, b_counters, sps, r_name, b_name, last_added
    get_details()
    won = False
    while not won:
        r_turn()
        if r_counters >= 4:
            won = check_win("r")
        if not won:
            b_turn()
            if b_counters >= 4:
                won = check_win("b")
        if r_counters + b_counters == 42:
            print("This is a draw...")
            won = True
    print("Final board:")
    show_board()
    sps = [0, 0, 0, 0, 0, 0, 0]
    board = [["0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0"]]
    r_counters = 0
    b_counters = 0
    r_name = ""
    b_name = ""
    last_added = 0
