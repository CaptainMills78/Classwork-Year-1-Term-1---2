
import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

person_dict = json.loads(person_string)

# Converts to json object, indents (by 4 spaces) and sorts keys in alphabetical order
print(json.dumps(person_dict, indent = 4, sort_keys = True))

# Prints as a json string in format
