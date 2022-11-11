airports = {}


def menu():
    print("""-------------------Welcome, what would you like to do?--------------
    1. Add Airport
    2. Search for Airport
    3. View the dictionary
    4. End (This will store the dictionary)""")
    user = int(input("Please enter what you would like to do?"))
    print(user)
    match user:
        case 1:
            addNew()
        case 2:
            search()
        case 3:
            print("Here is the dictionary.")
            print(airports)
        case 4:
            print("Saving...")
            return True
        case other:
            print("Invalid option, try again.")


def addNew():
    name = str(input("Enter the name of the airport. (Cannot be left empty):"))
    key = str(input("Enter the code of this airport (MUST 3 alphabetical characters long):")).upper()
    while len(name) == 0:
        name = str(input("Please enter the name of your airport again (not empty)"))
    while len(key) != 3 or key.isalpha() == False:
        key = str(input("Please enter the code of this airport (MUST 3 alphabetical characters long!!!!!):")).upper()
    airports[key] = name
    print("Airport is added to dictionary.")


def search():
    s = True
    while s:
        code = str(input("Please enter a code to search for:"))
        if code in airports:
            airport = airports[code]
            print("The airport for the entered code is: " + airport)
        else:
            print("Airport not found.")
        close = str(input("Would you like to return to menu? (y/n)")).lower()
        if close == "y":
            s = False
        elif close == "n":
            print("Ok, we shall start again.")
        else:
            print("Unclear, so we shall start again.")


def save():
    pass


end = False
while not end:
    end = menu()

save()
