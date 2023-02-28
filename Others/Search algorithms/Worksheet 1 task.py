def search(values, target):
    found = False
    for x in range(len(values)):
        if values[x] == target:
            found = True
    return found


test = [1,2,32,8,17,19,42,13,0]
print(search(test, 3))
print(search(test, 1))
print(search(test, 0))
print(search(test, 19))
