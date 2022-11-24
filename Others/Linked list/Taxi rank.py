head = 0


def in_details():
    year = 2006
    reg = input("Please enter your car registration (if there is none, enter blank):")
    if len(reg) != 8:
        print("This registration is not the right length.")
        valid = False
    if year == "":
        valid = True
    else:
        valid = check_det(reg, year)
    if valid:
        return reg
    else:
        print("Not a valid reg number, taking back to menu...")


def check_det(r, y):
    incorrect_digit = []
    if y < 2001:
        return True
    else:
        for x in range(0, 8):
            d = r[x]
            if x == 0 or x == 1:
                if d in "ABCDEFGHJKLMNOPRSTUVWXYZ":
                    pass
                else:
                    incorrect_digit.append(x)
            if x in range(5, 8):
                if d in "ABCDEFGHJKLMNOPRSTUVWXY":
                    pass
                else:
                    incorrect_digit.append(x)
            if x in range(2, 4):
                if d in "0123456789":
                    pass
                else:
                    incorrect_digit.append(x)
            if x == 4:
                if d == " ":
                    pass
                else:
                    incorrect_digit.append(x)
        if len(incorrect_digit) == 0:
            return True
        else:
            return incorrect_digit


def setRank():
    r = [["", 66],
         ["", 66],
         ["", 66],
         ["", 66],
         ["", 66],
         ["", 66],
         ["", 66],
         ["", 66],
         ["", 66],
         ["", 66]]
    return r


def addTaxi(rank, reg, head1):
    pointer = head1
    while pointer >= 0:
        if rank[pointer][1] == 66:
            rank[pointer][0] = reg
            rank[pointer][1] = pointer + 1
            pointer = -1
        else:
            pointer += 1
    return rank


def leavingTaxi(rank1, head2):
    pointer1 = head2
    while pointer1 >= 0:
        if rank1[pointer1][1] != 66:
            rank1[pointer1][1] = 66
            pointer1 = -1
        else:
            pointer1 += 1
    return rank1


def output_rank(to_print):
    print("Current Taxi Rank:")
    for x in range(len(to_print), 0, -1):
        if to_print[x-1][1] != 66:
            print((to_print[x-1][0]), end=", ")
        else:
            print("Empty", end=", ")
    print("\n")


def main():
    taxi_rank = setRank()
    quitting = "n"
    while quitting != "y":
        choice = str(input("""-----------------WELCOME TO THE TAXI RANK-------------------------
        HERE ARE YOUR OPTIONS:
        1. ADD TAXI
        2. REMOVE TAXI
        3. PRINT RANK
        4. QUIT
        
        ENTER YOUR CHOICE:"""))
        if not choice.isdigit():
            print("Not a valid choice...")
        elif int(choice) == 1:
            registration = in_details()
            if registration is None:
                pass
            else:
                taxi_rank = addTaxi(taxi_rank, registration, head)
        elif int(choice) == 2:
            taxi_rank = leavingTaxi(taxi_rank, head)
        elif int(choice) == 3:
            output_rank(taxi_rank)
        elif int(choice) == 4:
            quitting = "y"
        else:
            print("Not a valid choice...")


main()
