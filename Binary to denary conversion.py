
def generate(num):
    total = 0
    for x in range(len(num)):
        if num[x] == "1":
            power = len(num) - (x+1)
            total = total + 2**power
    return total


# Main code


binary = input("Please enter a binary number:")
den_conversion = generate(binary)
print(den_conversion)
