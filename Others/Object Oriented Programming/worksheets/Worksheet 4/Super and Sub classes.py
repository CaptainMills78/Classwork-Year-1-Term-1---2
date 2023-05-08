class Pets:
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age

    def description(self):
        return f"{self.name}: I am {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class Dog(Pets):
    number_of_legs = 4
    def __init__(self, species, name, age):
        self.species = species
        super().__init__(name, age)

    def bark(self):
        print("Woof... woof... woof")

    def sniff(self, something):
        if something == "food":
            print("I can smell food, yum!")
        else:
            print(f"Sniff... Sniff...  {something} ...")

class Cat(Pets):
    pass

class Fish(Pets):
    pass


dog_1 = Dog("Cavalier", "Bob", 5)
dog_2 = Dog("Golden Retriever", "Max", 3)
cat_1 = Cat("Missy", 1)
fish_1 = Fish("Splash", 1)

print(dog_1.description())
print(dog_1.speak("Hello ... "))
dog_1.bark()
dog_2.sniff("food")
dog_1.sniff("Grass")

print(dog_2.description())
print(cat_1.description())
print(fish_1.description())

dog_list = []
dog_spec = ["Bulldog", "Pug", "Shih tzu"]
names = ["Bud", "Poppy", "Otis"]
ages = [12, 3, 6]
words = ["FOOD!", "BALL!", "SQUIRREL!"]

for x in range(len(names)):
    dog_list.append(Dog(dog_spec[x], names[x], ages[x]))
    print(dog_list[x].description())
    dog_list[x].speak(words[x])
    print()