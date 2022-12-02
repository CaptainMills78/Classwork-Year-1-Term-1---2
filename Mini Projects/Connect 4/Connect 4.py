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


def get_details():
    global r_name, b_name
    r_name = str(input("Red Player: Please enter your name:"))
    b_name = str(input("Blue Player: Please enter your name:"))


def isFull(Full_choice):
    global board, sps, maxLength
    if sps[Full_choice] == maxLength:
        return True
    else:
        return False


def show_board():
    global board
    for y in range(6, 0, -1):
        for x in range(len(board)):
            print(board[x][y-1], end=" ")
        print()
    return


def pushItem(item, Push_choice):
    global board, sps, maxLength
    if not isFull(Push_choice):
        board[Push_choice][sps[Push_choice]] = item
        sps[Push_choice] += 1
        return True
    else:
        print("Error: Stack Overflow")
        return False


def r_turn():
    global board, r_counters, r_name
    show_board()
    success_r = False
    while not success_r:
        r_place = int(input("Which column would you like to place a counter, "+r_name+"?")) - 1
        success_r = pushItem("r", r_place)
    r_counters += 1
    return


def b_turn():
    global board, b_counters, b_name
    show_board()
    success_b = False
    while not success_b:
        b_place = int(input("Which column would you like to place a counter, "+b_name+"?")) - 1
        success_b = pushItem("b", b_place)
    b_counters += 1
    return


def check_win():
    global board
    pass


def game():
    global board, r_counters, b_counters
    get_details()
    won = False
    while not won:
        r_turn()
        if r_counters >= 4:
            won = check_win()
        b_turn()
        if b_counters >= 4:
            won = check_win()


def main():
    game()
    to_return = str(input("Would you like to play again? (Y/N)")).upper()
    if to_return == "Y":
        return True
    elif to_return == "N":
        return False
    else:
        print("Not clear... Playing again")
        return True


while running:
    running = main()
