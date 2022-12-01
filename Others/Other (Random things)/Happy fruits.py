def check(num):
    while num != 1:
        total = 0
        for z in range(len(str(num))):
            y = int(str(num)[z]) ** 2
            total = total + y
        num = total
        if num == 4:
            return False
    return True


# Main code
happy = []
count = 0
number = int(input("Please input a whole number (positive):"))
check(number)
x = number
while count < 8:
    if check(x):
        happy.append(x)
        count = count + 1
    x = x + 1

print("The first 8 happy numbers from your number are:", happy)
