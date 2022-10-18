def in_details():
    year = ""
    name = input("Please enter your full name:")
    phone = str(input("Please enter your phone number:"))
    reg = input("Please enter your car registration (if there is none, enter blank):")
    if reg != "":
        year = int(input("Please enter the year that your car was registered:"))
    if year == "":
        valid = True
    else:
        valid = check_det(reg, year)
    if len(reg) > 8:
        print("This regestration is too long.")
        valid = False
    if valid == True:
        to_input = name + ", " + phone + ", " + reg + ";" + "\n"
        f = open("registered.txt", "a")
        f.write(to_input)
        f.close()
        print("Registration Complete")
    elif valid == False:
        pass
    else:
        print("The following digits are incorrect:")
        for i in valid:
            print(str(i + 1))


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


in_details()
