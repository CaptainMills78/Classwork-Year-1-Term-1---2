def num_in():
    num = 10000                                                                   #Sets the limit to start the loop
    while num >= 10000:                                                           #Loop
        num = int(input("Please give a positive number that is below 10,000:"))   #Allows input
        if num >= 10000:
            print("That is not a valid number.") #Allows to try again while letting the user know why

    return num


def factors(number):
    facts = 0
    for x in range(1, 10001):
        if number % x == 0 and x != number:
            print(x)
            facts = facts + x
    return facts


# Main Code

num1 = num_in()
num2 = num_in()

num1fact = factors(num1)
num2fact = factors(num2)

if num1fact == num2 and num2fact == num1:
    print("This number is amicable!")
else:
    print("This is not amicable.")
