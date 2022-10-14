def in_details():
    name = input("Please enter your full name:")
    phone = str(input("Please enter your phone number:"))
    reg = input("Please enter your car registration (if there is none, enter blank):")
    if reg != "":
        year = str(input("Please enter the year that your car was registered:"))
    else:
        year = ""
