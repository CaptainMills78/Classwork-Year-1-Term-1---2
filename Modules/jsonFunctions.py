import json

# Opens file and convers to python object
def jsonFileToPython(file_name):
    file = open(file_name, "r")
    data = json.load(file)
    return data

# Takes json string and converts to python object:
def jsonStringToPython(json_string):
    data = json.loads(json_string)
    return data

# Takes python object and converts to json string:
def pythonToJsonString(python_object):
    data = json.dumps(python_object)
    return data

# Takes python object and converts to json file:
def pythonToJsonFile(python_object, file_name):
    file = open(file_name, "w")
    json.dump(python_object, file)
    file.close()
    return

# Takes json string and 'pretty prints' it with specified indent and sort conditions:
def prettyPrint(json_string, indent_amount=4, sorting=True):
    data = json.loads(json_string)
    print(json.dumps(data, indent=indent_amount, sort_keys=sorting))
    return



