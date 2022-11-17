def getTotal(card_no):
    total = 70  # Test algorithm
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
        number = str("Please enter your card number:")
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
