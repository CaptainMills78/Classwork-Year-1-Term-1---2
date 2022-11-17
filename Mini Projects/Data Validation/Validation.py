def IsValid():
    date = enter()
    l_valid = lengthCheck(date)
    f_valid = formatCheck(date)
    year_valid = rangeCheck(date[6:], 2022, 1600)
    if year_valid:
        leap_year = leapCheck(date[6:])
    else:
        leap_year = False
    month_valid = rangeCheck(date[3:4], 12, 1)
    if date[3:4] == "02" and leap_year:
        day_valid = rangeCheck(date[0:1], 29, 1)
    elif date[3:4] == "02" and not leap_year:
        day_valid = rangeCheck(date[0:1], 28, 1)
    elif date[3:4] == "04" or date[3:4] == "06" or date[3:4] == "09" or date[3:4] == "11":
        day_valid = rangeCheck(date[0:1], 30, 1)
    else:
        day_valid = rangeCheck(date[0:1], 31, 1)
    print(l_valid, f_valid, year_valid, leap_year, month_valid, day_valid)
    if l_valid and f_valid and year_valid and month_valid and day_valid:
        return True
    else:
        return False


def enter():
    date = str(input("Please enter a date in the format DD/MM/YYYY"))
    return date


def formatCheck(fd):
    for x in range(0, 10):
        match x:
            case 0 | 1 | 3 | 4 | 6 | 7 | 8 | 9:
                if fd[x].isdigit():
                    pass
                else:
                    return False
            case 2 | 5:
                if fd[x] == "/":
                    pass
                else:
                    return False
    return True


def lengthCheck(ld):
    length = len(ld)
    if length == 10:
        return True
    else:
        return False


def rangeCheck(data, maximum, minimum):
    if int(minimum) <= int(data) <= maximum:
        return True
    else:
        return False


def leapCheck(year):
    year = int(year)
    if (year % 100 != 0 and year % 400) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


# Main Code
valid = IsValid()
print(valid)