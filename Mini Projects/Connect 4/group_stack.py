
def isEmpty(Empty_choice, sp):
    if sp[Empty_choice] == 0:
        return True
    else:
        return False


def isFull(sp, maxLength1):
    if sp == maxLength1:
        return True
    else:
        return False


def pushItem(item, Push_choice, group, sp, maxLength):
    if not isFull(sp, maxLength):
        group[Push_choice][sp] = item
        return True
    else:
        print("Error: Stack Overflow")
        return False


def popItem(Pop_choice, sp):
    if not isEmpty(Pop_choice, sp):
        sp[Pop_choice] -= 1
    else:
        print("Error: Stack Underflow")


def isStackValid(Stack_choice, minimum, maximum):
    if Stack_choice.isdigit():
        if minimum <= int(Stack_choice) <= maximum:
            valid = True
        else:
            valid = False
    else:
        valid = False
    return valid


def isOptionValid(Option_choice, minimum, maximum):
    if Option_choice.isdigit():
        if minimum <= int(Option_choice) <= maximum:
            valid = True
        else:
            valid = False
    else:
        valid = False
    return valid
