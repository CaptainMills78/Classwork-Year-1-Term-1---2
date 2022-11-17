def getTotal(card_no):
    total = 0
    for x in range(len(card_no)):
        if (x + 1) % 2 != 0:
            total += int(card_no[x])
        else:
            temp = int(card_no[x]) * 2
            if temp > 9:
                temp2 = 0
                for y in str(temp):
                    temp2 += int(y)
                temp = temp2
            total += temp
    return total


def check(card):
    if len(card) != 11:
        print("This card number is an unacceptable length.")
        return False
    if not card.isdigit():
        print("There is an unacceptable character in this card.")
        return False
    return True


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
        number = str(input("Please enter your card number to check it, or 'x' to quit:"))
        if number == "x":
            print("Quiting...")
            return
        basic_check = check(number)
        if basic_check:
            tot = getTotal(number)
            valid = isValid(tot)
        else:
            valid = False
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
