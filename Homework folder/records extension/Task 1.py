import random
countries = []
file = open("goals.txt", "r")

for line in file:
    found = False
    data = line.split(";")
    country = data[1]
    for x in countries:
        if x[0] == country:
            x[1] += 1
            found = True
    if not found:
        countries.append([country, 1])


file.close()

country1 = random.choice(countries)
country2 = random.choice(countries)

while country2 == country1:
    country2 = random.choice(countries)
print(f"""Choices are:
{country1[0]}
{country2[0]}

Which has a higher score?
""")
userChoice = str(input(""))
while userChoice != country1[0] and userChoice != country2[0]:
    print("Not a valid country... Try again.")
    userChoice = str(input(""))

if country1[1] >= country2[1] and userChoice == country1[0]:
    print("Correct!")
elif country2[1] >= country1[1] and userChoice == country2[0]:
    print("Correct!")
else:
    print("Incorrect...")
