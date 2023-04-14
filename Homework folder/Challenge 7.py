import random
import time


def random_sym():
    num = random.randint(0, 5)
    if num == 0:
        symbol = "Cherry"
    elif num == 1:
        symbol = "Bell"
    elif num == 2:
        symbol = "Lemon"
    elif num == 3:
        symbol = "Orange"
    elif num == 4:
        symbol = "Star"
    elif num == 5:
        symbol = "Skull"
    return symbol


def sym2(credit):
    credit = credit + 0.50
    return credit


def sym3(credit):
    credit = credit + 1
    return credit


def bell3(credit):
    credit = credit + 5
    return credit


def skull3(credit):
    credit = credit - credit
    return credit


def skull2(credit):
    credit = credit - 1
    return credit


def check_roll(r, mon):
    if r[0] == "Skull" and r[1] == "Skull" and r[2] == "Skull":
        print("OH NO! 3 SKULLS!    You lost all of your credit.")
        mon = skull3(mon)
    elif (r[0] == r[1] and r[1] != r[2] and r[0] == "Skull") or (r[0] == r[2] and r[0] != r[1] and r[0] == "Skull") or (r[1] == r[2] and r[1] != r[0] and r[0] == "Skull"):
        print("Oh dear! 2 skulls!    You lost £1 in credit.")
        mon = sym2(mon)
    elif (r[0] == r[1] and r[1] != r[2]) or (r[0] == r[2] and r[0] != r[1]) or (r[1] == r[2] and r[1] != r[0]):
        print("Nice! 2 of a kind!    You earned 50p in credit.")
        mon = sym2(mon)
    elif (r[0] == r[1] and r[1] == r[2]) and r[0] == "Bell":
        print("NICE!  BELLS!!!!!!!!!   You earned £5 in credit!!!")
        mon = bell3(mon)
    elif r[0] == r[1] and r[1] == r[2]:
        print("Nice! 3 of a kind!    You earned £1 in credit!")
        mon = sym3(mon)
    else:
        print("Aww, nothing this time.")
    return mon


# Main code


money = 1.00
stop = False
time.sleep(0.5)
print("You have: £" + str(money))

while stop is False and money >= 0.20:
    roll = []
    print("Rolling...")
    time.sleep(1)
    money = money - 0.20
    for x in range(0, 3):
        roll.append(random_sym())
    for x in roll:
        time.sleep(0.2)
        print(x)
        time.sleep(0.2)
    money = check_roll(roll, money)
    print("You have: £" + str(round(money, 3)))
    if input("Would you like to stop now? Y/N").lower() == "y":
        stop = True
        print("Ok, it is time to stop.")
    else:
        print("Let's carry on!")
    if money < 0.2:
        print("You don't have enough money!")
