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

class player():
    def __init__(self, name):
        self.__name = name
        self.__score = 0
        self.__hand = []

    def view_hand(self):
        print(f"{self.__name}'s Hand:")
        for i in self.__hand:
            print(i.get_details())



    def recieve(self, givencard):
        self.__hand.append(givencard)


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
    gameDeck = deck()
    gameDeck.shuffle()
    name1 = str(input("Please enter Player 1's name:"))
    player1 = player(name1)
    comPlayer = player("Computer")
    player1.recieve(gameDeck.deal())
    player1.recieve(gameDeck.deal())
    comPlayer.recieve(gameDeck.deal())
    comPlayer.recieve(gameDeck.deal())
    player1.view_hand()
    comPlayer.view_hand()



if __name__ == "__main__":
    # notFound = False
    # deck1 = deck()
    # print(len(deck1.Cards))
    # deck1.shuffle()
    # for i in deck1.Cards:     # Test to ensure all cards are present
        # print(i.get_details())

    playGame()



