
def occurenceCount(values, target):
    count = 0
    for x in range(len(values)):
        if values[x] == target:
            count += 1
    return count
