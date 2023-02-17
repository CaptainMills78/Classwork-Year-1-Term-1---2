def linear(values, target):
    x = 0
    found = False
    while x < len(values) and found == False:
        if values[x] == target:
            found = True
        else:
            x += 1
    print("In List? - "+str(found))
    if found:
        print("Target at position: " + str(x))


if __name__ == "__main__":
    l = [1, 3, 7, 43, 12, 87, 4]
    linear(l, int(input("Please enter a target")))
