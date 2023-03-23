import json

person = '{"name":"Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

# Output whole dictionary - {'name': 'Bob', 'languages': ['English', 'French']}
print(person_dict)

# Output name - Bob
print(person_dict["name"])

# Output languages - ['English', 'French']
print(person_dict["languages"])