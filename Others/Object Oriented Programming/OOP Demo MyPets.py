# Demo on OOP
class Pets():
          def __init__(self , givenName, givenAge):
                    self.name = givenName
                    self.__age = givenAge  # age is private

          def describe(self):
                    return  self.name + " I am " + str(self.__age) + " years old"

                    
          def speak(self, sound):
                    print( self.name + " says " + sound)

                    
          def sleep(self): # all Pets sleep silently
                    print("Sleeping Silently")

          def ask(self, question):
                    return(question)

          def set_age(self, newAge):
              self.__age = newAge

          def get_age(self):
              return self.__age


class Dog(Pets):# dog inherits  all attributes and methods from Pets

          def __init__(self, givenspecies, givenname, givenage):
                    self.species = givenspecies
                    number_of_legs = 4  # all dogs have 4 legs
                    super().__init__(givenname, givenage)

          def bark(self):
                    print(" Woof .... Woof...Woof")
         
          
class Cat(Pets): # Cat also inherits  attributes and methods from pets

          def __init__(self, givenbread,givenname, givenage):
                    self.bread = givenbread
                    number_of_legs = 4  # all cats have 4 legs
                    super().__init__(givenname, givenage)

          def meow(self):
                    print(" Meow .... meow..... Meow")
                    
          def sleep(self):
                    print("my name is  " + self.name +
                          " I am closing my eyes slowly and ... Snore....Snore....Snore")

if __name__ == '__main__':                    
        myDog = Dog("Bull dog", "Max", 8)
        myCat = Cat("Birman Cat", "Felix", 3)

        #print("the dog: " +myDog.species + " ... \n" + myDog.describe(),
        #"\nthe cat: " +myCat.bread + " says ...\n  " + myCat.describe())
        #myDog.speak("hello everyone I can Bark .. ")
        #myDog.bark()
        #myDog.sleep()
        #myCat.meow()
        #myCat.sleep()
        #myDog.ask(myCat.meow())    # interaction
        #myCat.ask(myDog.bark())    # interaction

        ############################################
        # trying methods which are not exist
        #print(myDog.colour)
        #myDog.breathe()
        ############################################

        ############################################
       # using setter and getter
        #print("my age before is " + str(myDog.get_age()))
        #myDog.set_age(6)
        #print("now my age is " +str(myDog.get_age()))

        #############################################