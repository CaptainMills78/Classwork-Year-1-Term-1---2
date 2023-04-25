class Pet (object):
    def __new__(cls, *args, **kwargs):
        return super().__new__(Pet)

    def __init__(self, Name, Age, Number_of_Legs):
        self.name = Name
        self.age = Age
        self.no_o_legs = Number_of_Legs


    def description(self):
        return "Describe my self as : I am " + self.name + " I am " + str(self.age) + " years old"


    def speak(self, sound):
        return f"Listen to me ... I am speaking: {sound}"


#####  Pet 1 #####
myPet = Pet(Age=67, Number_of_Legs=4, Name="Max")
print("The name of pet 1 is "+myPet.name)
print(myPet.description())
print(myPet.speak("Hello there"))


#####  Pet 2 #####
myPet2 = Pet(Age=4, Number_of_Legs=2, Name="Bob")
print("The name of pet 2 is "+myPet2.name)
print(myPet2.description())
print(myPet2.speak("I am a different animal"))


# Changing Pet names

myPet.name = "Archie"
myPet2.name = "Kevin"
print("The name of pet 1 is "+myPet.name)   # Print new names
print("The name of pet 2 is "+myPet2.name)

