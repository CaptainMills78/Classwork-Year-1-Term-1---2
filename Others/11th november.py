names = ["Ben", "Adam", "John", "Ben", "Maddi", "John", "Smith", "Maddi"]
nameCount = {}
for name in names:
    if name not in nameCount:
        nameCount[name] = 1
    else:
        nameCount[name] += 1
print(nameCount)
