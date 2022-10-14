def quadSolver():
    a = float(input("Enter a:"))     #Cannot be 0 or alphabet - breaks code
    b = float(input("Enter b:"))     #Cannot be alphabet
    c = float(input("Enter c:"))     #Cannot be alphabet
    d = b * b - 4 * a * c

    if d == 0:
        X1 = -b / (2 * a)
        X2 = X1
        print("The roots are:", X1, X2)

    elif d > 0:
        X1 = (-b + d ** 0.5) / (2 * a)
        X2 = (-b - d ** 0.5) / (2 * a)
        print(X1, X2)

    else:
        print("There is no real value.")


# Main Code

choice = input("Would you like to solve an equation? Y/N").lower()
while choice == "y":
    print("Ok...")
    quadSolver()
    choice = input("Would you like to solve another equation? Y/N").lower()
print("Thank you for using my app!")

