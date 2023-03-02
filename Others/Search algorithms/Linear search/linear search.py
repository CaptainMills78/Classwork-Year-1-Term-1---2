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


if __name__ == "__main__":
    l = [1, 3, 7, 43, 12, 87, 4]
    presence, pos = linear(l, int(input("Please enter a target")))
    print("Item in List? - "+str(presence))
    if presence:
        print("Position at +")
