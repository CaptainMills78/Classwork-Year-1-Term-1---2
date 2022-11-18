import random


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


def generate10():
    c = ""
    for x in range(10):
        c += str(random.randint(1, 9))
    return c


def generate11(c_base):
    total = getTotal(c_base)
    char11 = str(10 - (total % 10))
    return c_base + char11


def main():
    card_base = generate10()
    card_whole = generate11(card_base)
    print(card_whole)


# Main Code
main()
