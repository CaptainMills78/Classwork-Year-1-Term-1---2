car_park_base = []
for x in range(10):
    row =[]
    for y in range(6):
        row.append("empty")
    car_park_base.append(row)

def menu(car_park):
    print("""WELCOME TO THE CARPARK
    what would you like to do?
    1. 'Park a car'
    2. 'View Car park'
    3. Exit
    
    Enter choice here:""", end="")
    option = str(input())

    match option:
        case 1:
            pass
        case 2:
            pass
        case 3:
            return True
        case _:
            return False
