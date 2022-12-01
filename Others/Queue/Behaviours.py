array = ["", "", "", "", "", "", "", "", "", ""]
TP = 0
HP = 0
max_length = 10


# Common:


def is_empty():
    if HP == TP:
        return True
    else:
        return False


# Linear - Cannot reuse indexes:


def is_full_linear():
    if TP == max_length:
        return True
    else:
        return False


# Non-Linear - Can reuse indexes:


def is_full_nonlinear():
    if TP == HP-1 or (HP == 0 and TP == max_length):
        return True
    else:
        return False


def push_nonlinear():
    global TP, HP, max_length
    item = 65
    if is_full_nonlinear():
        print("Queue Overflow")
    else:
        array[TP] = item
        TP += 1
        if TP > max_length:
            TP = 0


def pop_nonlinear():
    global TP, HP, max_length
    if is_empty():
        print("Queue Underflow")
    else:
        print(array[HP])
        HP += 1
        if HP > max_length:
            HP = 0
