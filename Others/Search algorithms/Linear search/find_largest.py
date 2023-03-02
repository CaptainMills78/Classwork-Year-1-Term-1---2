
def findLargest(values):
    largest = values[0]
    pos = 0
    for x in range(len(values)):
        if values[x] > largest:
            largest = values[x]
            pos = x
    return largest, pos
