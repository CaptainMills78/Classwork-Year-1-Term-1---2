import game

running = True


def main():
    game.rungame()
    to_return = str(input("Would you like to play again? (Y/N)")).upper()
    if to_return == "Y":
        return True
    elif to_return == "N":
        return False
    else:
        print("Not clear... Playing again")
        return True


if __name__ == "__main__":
    while running:
        running = main()
