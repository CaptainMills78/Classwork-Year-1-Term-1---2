def in_details():
    name = input("Please enter your full name:")
    phone = str(input("Please enter your phone number:"))
    reg = input("Please enter your car registration (if there is none, enter blank):")
    if reg != "":
        year = str(input("Please enter the year that your car was registered:"))
    else:
        year = ""
    valid = check_det(name, phone, reg, year)


def check_det(n, p, r, y):
    if r == "" or int(y) < 2001:
        return True
    else:
        if r[0]