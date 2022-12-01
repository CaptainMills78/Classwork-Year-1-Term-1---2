group = [["", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", ""]]
sps = [0, 0, 0, 0, 0]
maxLengths = [len(group[0]), len(group[1]), len(group[2]), len(group[3]), len(group[4])]


def isEmpty(Empty_choice):
    global group, sps, maxLengths
    if sps[Empty_choice] == 0:
        return True
    else:
        return False


def isFull(Full_choice):
    global group, sps, maxLengths
    if sps[Full_choice] == maxLengths[Full_choice]:
        return True
    else:
        return False


def pushItem(item, Push_choice):
    global group, sps, maxLengths
    if not isFull(Push_choice):
        group[Push_choice][sps[Push_choice]] = item
        sps[Push_choice] += 1
    else:
        print("Error: Stack Overflow")


def popItem(Pop_choice):
    global group, sps, maxLengths
    if not isEmpty(Pop_choice):
        sps[Pop_choice] -= 1
    else:
        print("Error: Stack Underflow")


def isStackValid(Stack_choice):
    if Stack_choice.isdigit():
        if 1 <= int(Stack_choice) <= 5:
            valid = True
        else:
            valid = False
    else:
        valid = False
    return valid


def isOptionValid(Option_choice):
    if Option_choice.isdigit():
        if 1 <= int(Option_choice) <= 4:
            valid = True
        else:
            valid = False
    else:
        valid = False
    return valid


def main():
    global group, sps
    leave = False
    while not leave:
        valid1 = False
        valid2 = False
        while not valid2:
            Option_chosen = input("""-----------Welcome to the stack generator--------------
            Options:
            1. View Stack
            2. Push item
            3. Pop item
            4. Quit
            
            Please enter your choice:""")
            valid2 = isOptionValid(Option_chosen)
        Option_chosen = int(Option_chosen)
        if Option_chosen == 4:
            leave = True
        else:
            while not valid1:
                Stack_chosen = input("Choose the stack to use (1-5):")
                valid1 = isStackValid(Stack_chosen)
            Stack_chosen = int(Stack_chosen) - 1
            if Option_chosen == 1:
                for x in range(0, sps[Stack_chosen]):
                    print(group[Stack_chosen][x], end=", ")
                print("\n")
            elif Option_chosen == 2:
                to_push = input("Enter an item to push to your chosen stack:")
                pushItem(to_push, Stack_chosen)
            elif Option_chosen == 3:
                popItem(Stack_chosen)


main()
