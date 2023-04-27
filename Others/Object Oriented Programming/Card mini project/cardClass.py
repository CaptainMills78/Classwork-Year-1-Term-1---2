import random

class card():
    def __init__(self, suit, rank):
        __regular = [2,3,4,5,6,7,8,9,10]
        match suit:
            case 1:
                self.__suit = "Diamonds"
            case 2:
                self.__suit = "Clubs"
            case 3:
                self.__suit = "Hearts"
            case 4:
                self.__suit = "Spades"
        match rank:
            case rank if rank in __regular:
                self.__rank = str(rank)
                self.__value = rank
            case 1:
                self.__rank = "Ace"
                self.__value = (1, 11)
            case 11:
                self.__rank = "Jack"
                self.__value = 10
            case 12:
                self.__rank = "Queen"
                self.__value = 10
            case 13:
                self.__rank = "King"
                self.__value = 10

    def get_details(self):
        return f"{self.__rank} of {self.__suit}, value = {self.__value}"

    def get_value(self):
        return self.__value

    def get_rank(self):
        return self.__rank


class player():
    def __init__(self, name):
        self.__name = name
        self.__score = 0
        self.__hand = []

    def add_score(self, state):
        if state == "WIN":
            self.__score += 2
        elif state == "DRAW":
            self.__score += 1

    def get_score(self):
        return self.__score

    def view_hand(self):

        print(f"{self.__name}'s Hand:")
        for i in self.__hand:
            print(i.get_details())
        print(f"Hand is worth: {self.hand_total()}")
        return self.hand_total()

    def hand_total(self):
        total = 0
        for i in self.__hand:
            if i.get_rank() == "Ace":
                if total + 11 > 21:
                    total += 1
                else:
                    total += 11
            else:
                total += i.get_value()
        return total

    def recieve(self, givencard):
        self.__hand.append(givencard)

    def clear_hand(self):
        self.__hand = []

    def get_name(self):
        return self.__name

    def get_hand(self):
        return self.__hand


class dealer(player):
    def __init__(self):
        super().__init__("Dealer")

    def view_card(self):
        print(f"Dealer's shown card: {super().get_hand()[0].get_details()}")
        return self.hand_total()


class deck():
    def __init__(self):
        self.Cards = []
        for x in range(4):  # Suits
            for y in range(13):  # Rank
                self.Cards.append(card(x + 1, y + 1))

    def shuffle(self):
        newDeck = []
        while len(newDeck) != len(self.Cards):
            i = self.Cards[random.randint(0,51)]
            if i not in newDeck:
                newDeck.append(i)
        self.Cards = newDeck

    def deal(self):
        giveCard = self.Cards.pop()
        return giveCard


def playGame():

    name1 = str(input("Please enter Player 1's name:"))
    player1 = player(name1)
    comPlayer = dealer()
    while player1.get_score() < 20 and comPlayer.get_score() < 20:
        gameRound(player1, comPlayer)
        player1.clear_hand()
        comPlayer.clear_hand()
        print(f"{player1.get_name()}'s score: {player1.get_score()}")
        print(f"{comPlayer.get_name()}'s score: {comPlayer.get_score()}")
    if player1.get_score() >= 20:
        print(f"{player1.get_name()} WINS!!!!")
    else:
        print(f"{comPlayer.get_name()} WINS!!!!")


def gameRound(Player, Dealer):
    gameDeck = deck()
    gameDeck.shuffle()
    Player.recieve(gameDeck.deal())
    Player.recieve(gameDeck.deal())
    Dealer.recieve(gameDeck.deal())
    Dealer.recieve(gameDeck.deal())
    playerTotal = Player.view_hand()
    dealerTotal = Dealer.view_card()
    if playerTotal == 21 and dealerTotal == 21:
        print("DRAW")
        Player.add_score("DRAW")
        Dealer.add_score("DRAW")
        return
    elif playerTotal == 21:
        print("WIN!")
        Player.add_score("WIN")
        return
    elif dealerTotal == 21:
        print("LOSS!")
        Dealer.add_score("WIN")
        return
    else:
        print("No immediate win...")
    end = False
    while not end:
        choice = ""
        while choice != "draw" and choice != "stick":
            choice = str(input("Draw or stick?")).lower()
        if choice == "draw":
            Player.recieve(gameDeck.deal())
            playerTotal = Player.view_hand()
            if playerTotal > 21:
                print(f"{Player.get_name()} has gone BUST!!")
                Dealer.add_score("WIN")
                return
        if choice == "stick":
            end = True
    print("Dealer's Turn!")
    Dealer.view_hand()
    while dealerTotal < 17:
        Dealer.recieve(gameDeck.deal())
        dealerTotal = Dealer.view_hand()
        if dealerTotal > 21:
            print(f"{Dealer.get_name()} has gone BUST!!")
            Player.add_score("WIN")
            return
    if playerTotal == 21 and dealerTotal == 21:
        print("DRAW")
        Player.add_score("DRAW")
        Dealer.add_score("DRAW")
        return
    elif playerTotal == 21:
        print("WIN!")
        Player.add_score("WIN")
        return
    elif dealerTotal == 21:
        print("LOSS!")
        Dealer.add_score("WIN")
        return
    else:
        if playerTotal > dealerTotal:
            print("WIN!")
            Player.add_score("WIN")
            return
        elif dealerTotal > playerTotal:
            print("LOSS!")
            Dealer.add_score("WIN")
            return
        else:
            print("DRAW")
            Player.add_score("DRAW")
            Dealer.add_score("DRAW")
            return














if __name__ == "__main__":
    # notFound = False
    # deck1 = deck()
    # print(len(deck1.Cards))
    # deck1.shuffle()
    # for i in deck1.Cards:     # Test to ensure all cards are present
        # print(i.get_details())

    playGame()



