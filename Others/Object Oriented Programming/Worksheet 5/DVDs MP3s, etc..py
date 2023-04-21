class item(object):

    def __init__(self, givenName, givenDes, givenPri):
        self.name = givenName
        self.description = givenDes
        self.price = givenPri

    def viewFullDescription(self):
        print("Item Description: " + str(self.name) + ", " + str(self.description) + ", £" + str(self.price))

    def addToShoppingBasket(self):
        print("Added to Shopping Basket")

    def removeFromShoppingBasket(self):
        print("Removed from ShoppingBasket")


class mp3(item):

    def __init__(self, givenname, givendes, givenpri, givenartist, givenduration):
        self.artist = givenartist
        self.duration = givenduration
        super().__init__(givenname, givendes, givenpri)

    def play(self):
        print("Playing mp3...")

    def download(self):
        print("Downloading...")

    def viewFullDescription(self):
        print(f"MP3: {self.name}, About: {self.description}, {self.duration} minutes long, £{self.price}. By Artist: {self.artist}.")


class dvd(item):

    def __init__(self, givencert, givendur, givenactors, givenname, givendes, givenpri):
        self.certificate = givencert
        self.duration = givendur
        self.actors = givenactors
        super().__init__(givenname, givendes, givenpri)

    def viewTrailer(self):
        print("Showing trailer")

    def viewFullDescription(self):
        print(f"DVD: {self.name}. About: {self.description}, {self.duration} minutes long. Cost: £{self.price} Cast: {self.actors}")


class book(item):

    def __init__(self, givennumberpages, givengenre, givenauthor, givenname, givendes, givenpri):
        self.genre = givengenre
        self.NumberOfPages = givennumberpages
        self.author = givenauthor
        super().__init__(givenname, givendes, givenpri)

    def previewContent(self):
        print("Here is the preview content:")

    def viewFullDescription(self):
        print(f"Book: {self.name} by {self.author}. About: {self.description}, {self.NumberOfPages} Pages Long. £{self.price}")


if __name__ == "__main__":
    dvdArray = [
        dvd(givencert="P3", givenname="Nemo", givendes="A fish finds his son", givendur="1hr 30 mins", givenpri=10.50,
            givenactors="Ellen Degeneres"),
        dvd(givencert="P2", givenname="Dory", givendes="A fish finds their parents", givendur="1hr 20 mins",
            givenpri=11.50, givenactors="Ellen Degeneres"),
        dvd(givencert="P1", givenname="UP", givendes="A boy finds his bird", givendur="1hr 40 mins", givenpri=9.50,
            givenactors="Dog")
        ]
    mp3Array = [
        mp3(givenname="My Time", givendes="Falling...", givenpri=2.44, givenartist="Bo en", givenduration="3 mins"),
        mp3(givenname="golden hour", givendes="Piano", givenpri=1.22, givenartist="JVK", givenduration="2 mins"),
        mp3(givenname="Shine", givendes="Let it Shine!", givenpri=0.99, givenartist="Take That", givenduration="4 mins")
        ]
    bookArray = [
        book(givennumberpages=121, givenpri=12.50, givendes="Compass is found that can detect dusty areas", givenname="Northen Lights",
             givengenre="Fantasy", givenauthor="Phillip Pullman"),
        book(givenpri=9.50, givendes="Schoolboy tries to survive life", givenname="A Diary of a Wimpy Kid",
             givengenre="Slice of Life", givenauthor="Greg", givennumberpages=98),
        book(givenpri=15.50, givendes="Find out stuff about the universe!", givenname="Element in the room",
             givengenre="Informative", givenauthor="Steve Mould", givennumberpages=276)
        ]

    for x in dvdArray:
        x.viewFullDescription()
    for x in mp3Array:
        x.viewFullDescription()
    for x in bookArray:
        x.viewFullDescription()
    myItem = item(givenName="Banana", givenDes="Yellow object", givenPri=5.67)
    myItem.viewFullDescription()    # Works as intended
    bookArray[0].viewFullDescription() # Currently with error, attribute not found - name, description
