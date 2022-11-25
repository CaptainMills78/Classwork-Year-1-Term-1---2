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


def swap_driver(rank5, reg1, reg2):
    found1 = False
    found2 = False
    for x in range(len(rank5)):
        if rank5[x][0] != reg1 and rank5[x][0] != reg2:
            pass
        elif rank5[x][0] == reg1:
            found1 = True
            eleLoc1 = x
        elif rank5[x][0] == reg2:
            found2 = True
            eleLoc2 = x
    if not found1 or not found2:
        print("Registrations not found...")
        return rank5
    else:
        rank5[eleLoc1][0] = reg2
        rank5[eleLoc2][0] = reg1
        return rank5


def addTaxi(rank, reg, head1):
    pointer = head1
    while pointer >= 0:
        if rank[pointer][1] == 66:
            rank[pointer][0] = reg
            rank[pointer][1] = determine_next(rank)
            pointer = -1
        else:
            pointer += 1
    return rank


def determine_next(rank3):
    next_point = 0
    for x in rank3:
        if x[1] != 66 and x[1] > next_point:
            next_point = x[1]
    return next_point+1


def leavingAny(rank4, leaving):
    done1 = False
    for x in range(len(rank4)):
        if done1 == True and rank4[x][1] != 66:
            rank4[x][1] -= 1
        elif rank4[x][0] == leaving:
            rank4[x][1] = 66
            done1 = True
        else:
            pass
    if not done1:
        print("Taxi not found...")
    return rank4


def leavingHead(rank1, head2):
    done = False
    pointer1 = head2
    while pointer1 <= 9 or done == False:
        if rank1[pointer1][1] != 66:
            rank1[pointer1][1] = 66
            done = True
            pointer1 += 1
        else:
            pointer1 += 1
    if done:
        for x in range(pointer1, len(rank1)):
            if rank1[x][1] != 66:
                rank1[x][1] -= 1
    return rank1


def output_rank(to_sort):
    print(to_sort)
    to_print = sorted(to_sort, key= lambda x: int(x[1]), reverse= True)
    print("Current Taxi Rank:")
    for x in to_print:
        if x[1] == 66:
            print("Empty", end=", ")
        else:
            print(x[0], end=", ")
    print("\n")


def main():
    taxi_rank = setRank()
    quitting = "n"
    while quitting != "y":
        choice = str(input("""-----------------WELCOME TO THE TAXI RANK-------------------------
        HERE ARE YOUR OPTIONS:
        1. ADD TAXI
        2. REMOVE HEAD TAXI
        3. REMOVE ANY TAXI
        4. SWAP DRIVER
        5. PRINT RANK
        6. QUIT
        
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
            taxi_rank = leavingHead(taxi_rank, head)
        elif int(choice) == 3:
            leaving_taxi = str(input("Please enter the leaving taxi"))
            taxi_rank = leavingAny(taxi_rank, leaving_taxi)
        elif int(choice) == 4:
            regist1 = str(input("Please enter the registration of one swapping driver:"))
            regist2 = str(input("Please enter the other driver:"))
            taxi_rank = swap_driver(taxi_rank, regist1, regist2)
        elif int(choice) == 5:
            output_rank(taxi_rank)
        elif int(choice) == 6:
            quitting = "y"
        else:
            print("Not a valid choice...")


main()
