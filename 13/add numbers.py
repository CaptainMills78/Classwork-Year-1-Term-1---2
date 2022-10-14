def sum_up(n):
    total = 0
    for x in range(0, n+1):
        total += x
    return total


num = int(input("Please enter a number:"))
print("The result of the function is: "+str(sum_up(num)))
