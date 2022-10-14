
def generate(num):
    binary = ""
    while num != 0:
        check1 = num // 2
        check2 = num % 2
        num = check1
        binary = str(check2)+binary
    return binary


# Main code


denary = int(input("Please enter a whole denary number:"))
bin_conversion = generate(denary)
print(bin_conversion)
