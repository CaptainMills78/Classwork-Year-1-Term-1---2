def getTotal(card_no):
    total = 0
    for x in range(len(card_no)):
        if card_no[x].isdigit():
            if (x+1) % 2 != 0:
                total += int(card_no[x])
            else:
                temp = int(card_no[x]) * 2
                if temp > 9:
                    temp2 = 0
                    for y in str(temp):
                        temp2 += int(y)
                    temp = temp2
                total += temp
        else:
            total = 1
            print("Card number is not a number...")
            return total
    return total


def isValid(sum0):
    remainder = sum0 % 10
    if remainder == 0:
        return True
    else:
        return False


def main():
    count = 0
    valid = False
    while count < 3:
        number = str(input("Please enter your card number:"))
        tot = getTotal(number)
        valid = isValid(tot)
        if not valid:
            count += 1
            print("The card is invalid, try again.")
        else:
            count = 4
    if valid:
        print("The card is valid.")
    else:
        print("You have run out of attempts.")


# Main Code
main()
