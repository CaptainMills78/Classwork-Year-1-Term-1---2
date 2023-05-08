class Pet():
    # Constructor
    def __init__(self, Name, Age, Number_of_legs):
        self.name = Name    # Name of the object is passed name
        self.age = Age
        self.no_of_legs = Number_of_legs

    # Methods
    def description(self):
        return "Describe my self as: I am "+self.name


first_pet = Pet("Bob", 5, 4)
print(first_pet.description())
