# Demo on OOP
class Pets():  # Write the master class then test before continuing - if this doesn't work, the subclasses won't work
    def __init__(self, givenName, givenAge):
        self.name = givenName  # name is public
        self.__age = givenAge  # age is private  -  can only be accessed within the class
        # If accessed outside of the class, it will be seen as undefined - print(myPet.age) --> error

    def describe(self):
        return self.name + " I am " + str(self.__age) + " years old"

    def speak(self, sound):  # Sound can be text
        print(self.name + " says " + sound)  # Sound is not an attribute, so does not need self.____

    def sleep(self):  # all Pets sleep silently by default
        print("Sleeping Silently")

    def ask(self, question):  # question is not an attribute
        return (question)  # Nothing will happen - nothing is done with the question

    # Encapsulation functions:

    def set_age(self, newAge):  # Allows the changing of the age attribute - Setter
        self.__age = newAge  # Have to pass the new value to change to - attribute set to the new value
        # Conditions for values put here (e.g. if newAge > 20:)

    def get_age(self):  # Allows reading of the age attribute - Getter
        return self.__age  # Returns the value of the attribute - must be caught by a variable / other function to be
        # used


class Dog(Pets):  # dog inherits  all attributes and methods from Pets

    def __init__(self, givenspecies, givenname,
                 givenage):  # givenname / givenage not spelled same as super class arguments
        self.species = givenspecies
        number_of_legs = 4  # all dogs have 4 legs, so set as a constant
        super().__init__(givenname, givenage)  # Create a Pet, then make it a Dog

    def bark(self):
        print(" Woof .... Woof...Woof")


class Cat(Pets):  # Cat also inherits  attributes and methods from pets

    def __init__(self, givenbread, givenname, givenage):
        self.bread = givenbread
        number_of_legs = 4  # all cats have 4 legs, so set as a constant
        super().__init__(givenname, givenage)

    def meow(self):
        print(" Meow .... meow..... Meow")

    def sleep(self):  # This will override the sleep method from the super class for ONLY the CAT
        print("my name is  " + self.name +
              " I am closing my eyes slowly and ... Snore....Snore....Snore")  # myCat.sleep() != myDog.sleep()


if __name__ == '__main__':
    myDog = Dog("Bull dog", "Max", 8)
    myCat = Cat("Birman Cat", "Felix", 3)

    print("the dog: " + myDog.species + " ... \n" + myDog.describe(),
          "\nthe cat: " + myCat.bread + " says ...\n  " + myCat.describe())
    myDog.speak("hello everyone I can Bark .. ")
    myDog.bark()
    myDog.sleep()
    myCat.meow()
    myCat.sleep()
    myDog.ask(myCat.meow())  # interaction - Dog asks cat to meow
    myCat.ask(myDog.bark())  # interaction - Cat asks dog to bark         #
    # Interactions must be done in terms of the methods known to the objects

    ############################################
    # trying methods which are not exist
    # print(myDog.colour)
    # myDog.breathe()
    ############################################

    ############################################
    # using setter and getter
    print("my age before is " + str(myDog.get_age()))
    myDog.set_age(6)
    print("now my age is " + str(myDog.get_age()))
    #############################################
