import json

file = open("person.json", "r")
data = json.load(file)
file.close()
print(data)
print(data["name"])
