import json

person_dict = {"name": "Bob", "languages": ["English", "French"], "numbers": (1, 2, 3)}

# Converts to json object
person_json = json.dumps(person_dict)

print(person_json)

# Writes json object to json file - can be done in one go if in correct format
file = open("person.json", "w")
file.write(person_json)
file.close()