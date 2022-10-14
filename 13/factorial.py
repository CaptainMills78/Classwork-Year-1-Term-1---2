def factorial(n):
    total = 1
    for x in range(1, n+1):
        total *= x
    return total


def check(inp):
    if num == 0:
        fact = 1
    elif num > 0:
        fact = factorial(num)
    else:
        print("Invalid input.")
    return fact


# Main code
num = int(input("Please enter a number to find the factorial of:"))
f = check(num)
print(f)
