def linear(values, target):
    x = 0
    found = False
    position = -1
    while x < len(values) and not found:  # Need condition to finish once length has been reached to avoid
        # index-out-of-range error
        # Need not found condition unless duplication is possible - this will currently stop at finding one instance
        if values[x] == target:
            found = True
        else:
            x += 1
    if found:
        position = x
    return found, position


def findLargest(values):
    largest = values[0]
    pos = 0
    for x in range(len(values)):
        if values[x] > largest:
            largest = values[x]
            pos = x
    return largest, pos


def occurenceCount(values, target):
    count = 0
    for x in range(len(values)):
        if values[x] == target:
            count += 1
    return count
