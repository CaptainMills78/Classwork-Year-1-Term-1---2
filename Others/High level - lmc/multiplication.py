def while_multi():
    total = 0
    count = 0
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    while num2 - count > 0:
        total += num1
        count += 1
    print(total)
    return

def for_multi():
    total = 0
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    for x in range(0, num2):
        total += num1
    print(total)
    return

while_multi()
for_multi()
